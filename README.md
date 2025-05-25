# Discord Time & Weather Bot

A Discord bot that tells the time and weather using slash commands.

## Setup

1. Clone this repository.
2. Install dependencies:
   ```
   pip install discord.py
   ```
3. Insert your bot token and OpenWeatherMap API key into a new file called `mySecrets.env`:
   ```
   DISCORD_TOKEN="your_discord_token_here"
   API_KEY="your_openweathermap_api_key_here"
   ```

## Usage

- `/time` — Shows the current server time.
- `/weather [city][State][Country]` — Shows the weather for the specified city.
- `/help` — Shows help information.

## Future Plans

**Bot functionality:**
- `/gpt`: Pass forward the chat message to GPT

**Skill:**
- Send images from bot to server

**Cleaning up / Maintaining code:**
- Add ability to add more slash commands and keep code clean (e.g., route `on_message` to slash-command-specific functions)
