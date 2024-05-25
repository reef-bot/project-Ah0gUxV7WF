# File: bot.py

import discord
from discord.ext import commands
import json
import asyncio
import requests
import re

# Import other necessary files
from command_system import CommandSystem
from filter_system import FilterSystem
from logger import Logger
from update_system import UpdateSystem

# Load configuration files
with open('../config/config.json', 'r') as config_file:
    config = json.load(config_file)

with open('../config/filters.json', 'r') as filters_file:
    filters = json.load(filters_file)

# Initialize bot
intents = discord.Intents.default()
intents.all()
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# Initialize systems
command_system = CommandSystem(bot, config)
filter_system = FilterSystem(bot, filters)
logger = Logger()
update_system = UpdateSystem(bot)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Event: Message is received
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Run message through filter system
    await filter_system.run_filters(message)

    await bot.process_commands(message)

# Add commands to the bot
command_system.add_commands()

# Run the bot
bot.run(config['token'])