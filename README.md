# Discord Time & Weather Bot

A Discord bot that tells the time and weather using slash commands or text commands.

## Setup

1. Clone this repository.
2. Install dependencies:
   ```
   pip install discord.py python-dotenv requests
   ```
3. Insert your bot token and OpenWeatherMap API key into a new file called `mySecrets.env`:
   ```
   DISCORD_TOKEN="your_discord_token_here"
   API_KEY="your_openweathermap_api_key_here"
   ```

## Usage

- `/time` — Shows the current server time.
- `/weather <city>[,State][,Country]` — Shows the weather for the specified city. Example: `/weather London` or `/weather San Francisco,CA,US`
- `/sensor` — Reads temperature and humidity from a DHT11 sensor (requires Raspberry Pi with sensor connected).
- `/help` — Shows help information.

> **Note:**  
> The bot currently responds to both slash commands and text commands typed in the chat (e.g., `/time`, `/weather ...`).  
> Slash command registration may require inviting the bot with the correct permissions and waiting for Discord to sync commands.

## Hardware Requirements

- To use the `/sensor` command, you need a Raspberry Pi with a DHT11 sensor connected to GPIO4.
- **Raspberry Pi**: Any model with GPIO support (e.g., Raspberry Pi 3, 4, Zero).
- **DHT11 Sensor**: Digital temperature and humidity sensor.
- **Wiring**:
  - Connect the DHT11 data pin to GPIO4 (physical pin 7) on the Raspberry Pi.
  - Connect the VCC pin of the DHT11 to 3.3V or 5V on the Pi.
  - Connect the GND pin of the DHT11 to a ground pin on the Pi.
  - (Optional) Use a 10kΩ pull-up resistor between the data and VCC pins for stable readings.
- **Libraries**:
  - `RPi.GPIO` and `dht11` Python libraries must be installed on the Raspberry Pi for sensor support.
- **Note**: The `/sensor` command will only work when the bot is running on a Raspberry Pi with the DHT11 sensor properly connected and the required libraries installed.

## Future Plans

**Bot functionality:**
- `/gpt`: Pass forward the chat message to GPT

**Skill:**
- Send images from bot to server

**Cleaning up / Maintaining code:**
- Add ability to add more slash commands and keep code clean (e.g., route `on_message` to slash-command-specific functions)
