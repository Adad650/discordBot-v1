import discord
import os
import datetime
import re
from dotenv import load_dotenv

# Load environment variables from token.env
load_dotenv('mySecrets.env')
token = os.getenv('DISCORD_TOKEN')
try:
    if not token:
        raise ValueError("No Discord token found. Please set the DISCORD_TOKEN environment variable.")
except ValueError as e:
    print(e)
    exit(1)

# create a new discord client
try:
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
except exception as e:
    print(f"Got an error: {e}")
    exit()


# define the on-ready event
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel_id = 1372335534940098727  # Replace with your channel ID
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send('Bot connected!')
    else:
        print("Channel not found.")

# define the on-message event
# This event is triggered when a message is sent in a channel
@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.author == client.user:
        print("Message from self, skipping")
        return
    if message.content.startswith(f'<@{client.user.id}> time'):
        x = datetime.datetime.now()
        y = (x.strftime("%D %H:%M:%S"))
        await message.channel.send(y)
    elif message.content.startswith(f"<@{client.user.id}>"):
         await message.channel.send('Hello there, You are talking to me!')

    #else: 
        #await message.channel.send('Hello there')

# now finally run the bot
try:
    client.run(token)
except Exception as e:
    print(f"An error occurred: {e}")


# 