# File: filter_system.py

import discord
from discord.ext import commands
import json

class FilterSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Check message content for inappropriate words
        if self.filter_message(message.content):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")
    
    def filter_message(self, message):
        with open("config/filters.json", "r") as file:
            filters = json.load(file)
        
        for word in filters['words']:
            if word.lower() in message.lower():
                return True
        
        return False

def setup(bot):
    bot.add_cog(FilterSystem(bot))