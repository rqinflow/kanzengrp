import json
import discord
from discord.ext import commands
from discord.utils import get
import datetime
import random

class Unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.unlocked_items = {}

def get_user_coins(user_id):
    coins_dict = {
        1234567890: 500,  # Example user ID and coin balance
        # Add more user ID and coin balance pairs as needed
    }
    return coins_dict.get(user_id, 0)  # Return the user's coin balance, or 0 if not found

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        coins = random.randint(1, 1000)
        xp = random.randint(1, 500)
        await ctx.send(f"You found {coins} coins!")

        if random.random() < 0.5:
            channel = self.bot.get_channel(1125999933149949982)
            await channel.send(f"{ctx.author.mention} found {xp} XP!")

    @commands.command()
    async def shop(self, ctx):
        embed = discord.Embed(title="Shop", description="Welcome to the shop!")
        embed.add_field(name="XP", value="Price: 100 coins", inline=False)
        embed.add_field(name="Emoji", value="Price: 200 coins", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def buy(self, ctx, item: str):
        if item.lower() == "xp":
            coins = 100
            if coins <= get_user_coins(ctx.author.id):
                # Deduct coins from user's balance
                # Perform other logic for buying XP
                await ctx.send(f"{ctx.author.mention} bought XP!")
            else:
                await ctx.send("Insufficient coins!")

async def setup(bot):
    await bot.add_cog(Unlock(bot))
