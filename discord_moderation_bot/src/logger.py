# logger.py

import logging

# Create a custom logger
logger = logging.getLogger('discord_moderation_bot')
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('moderation_bot.log')

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add them to the handlers
console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)