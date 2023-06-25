import json
import random
import discord
from discord.ext import commands




class editing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def addaudio(self, ctx, link: str):
        try:
            with open('audios.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(link)

        with open('audios.json', 'w') as file:
            json.dump(data, file, indent=4)

        await ctx.reply("The audio was added successfully!")

    @commands.command()
    async def audios(self, ctx):
        try:
            with open('audios.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        if len(data) > 0:
            selected_link = random.choice(data)
            await ctx.reply(selected_link)
        else:
            await ctx.reply("No one has added an audio yet! Be the first to add an audio by using the command `+addaudio (soundcloud link)`.")



async def setup(bot):
    await bot.add_cog(editing(bot))