import discord
import os
import datetime
from dotenv import load_dotenv

# Load environment variables from mySecrets.env
load_dotenv('mySecrets.env')
token = os.getenv('DISCORD_TOKEN')

if not token:
    print("No Discord token found. Please set the DISCORD_TOKEN environment variable.")
    exit(1)

# Define the client class BEFORE creating an instance
class MyClient(discord.Client):
    def __init__(self, *, intents):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync commands with Discord
        await self.tree.sync()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel_id = 1372335534940098727  
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send('Bot connected!')
    else:
        print("Channel not found.")

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.author == client.user:
        return  # skip messages from the bot itself
    if message.content.lower() == "/time":
        now = datetime.datetime.now()
        formatted = now.strftime("%D %H:%M:%S")
        await message.channel.send(f"Current server time: {formatted}")
    elif message.content.startswith(f"<@{client.user.id}>"):
        await message.channel.send('Hello there, You are talking to me!')

@client.tree.command(name="time", description="Get the current server time")
async def time_command(interaction: discord.Interaction):
    x = datetime.datetime.now()
    y = x.strftime("%D %H:%M:%S")
    await interaction.response.send_message(f"time:{y}")

try:
    client.run(token)
except Exception as e:
    print(f"An error occurred: {e}")
