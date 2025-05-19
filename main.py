import discord
import os
import datetime
from dotenv import load_dotenv
import re

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
    strMsg = str(message.content)
    if message.author == client.user:
        return
    if strMsg.startswith("/time"):
        x = datetime.datetime.now()
        y = x.strftime("%D %H:%M:%S")
        extractedMsg = re.findall(r"/time\s(.*)", strMsg)
        await message.channel.send(f"Hello {message.author} Current server time: {y} Im gonna call you {extractedMsg}")
    elif message.content.startswith(f"<{client.user.id}>"):
        await message.channel.send('Hello there, You are talking to me!')


try:
    client.run(token)
except Exception as e:
    print(f"An error occurred: {e}")
