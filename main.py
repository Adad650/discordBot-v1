import discord
import os
import datetime
from dotenv import load_dotenv
import re
import requests
import botWeatherAPI
import dht11Sensor

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

    match strMsg:
       
        case str() if re.match(r"/time(.*)", strMsg):
            x = datetime.datetime.now()
            y = x.strftime("%D %H:%M:%S")
            await message.channel.send(f"Hello {message.author} Current server time: {y} ")

        case str() if re.match(r"/weather (.*)", strMsg):
            city = re.findall(r"/weather(.*)", strMsg)
            if city:
                result = botWeatherAPI.getWeather(city)
                await message.channel.send(result)
            else:
                await message.channel.send("Please provide a city name after the /weather command.")

        case str() if re.match(r"/help(.*)", strMsg):
            await message.channel.send('Commands: /time, /weather, /help')

        case str() if re.match(fr"<@{client.user.id}>(.*)", strMsg):
            await message.channel.send('Hello there, You are talking to me the bot')
        case str() if re.match(r"/sensor(.*)", strMsg):
            try:
                dht11Sensor.getTemperatureAndHumidity()
                await message.channel.send("Sensor data retrieved successfully.")
            except Exception as e:
                await message.channel.send(f"An error occurred while retrieving sensor data: {e}")


        case _:
            print ("Unknown command")

try:
    client.run(token)
except Exception as e:
    print(f"An error occurred: {e}")
    