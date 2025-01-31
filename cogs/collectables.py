import json
import discord
from discord.ext import commands
from discord.utils import get
import datetime
import random
import sqlite3

"""class Unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('bot.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS user_data (user_id INTEGER PRIMARY KEY, coins INTEGER)')
        self.conn.commit()

    @commands.command()
    async def daily(self, ctx):
        coins = random.randint(1, 1000)
        xp = random.randint(1, 500)
        await ctx.send(f"You found <:coin:1127703632389865682> {coins}")

        if random.random() < 0.5:
            channel = self.bot.get_channel(1125999933149949982)
            await channel.send(f"{ctx.author.mention} found {xp} XP!")

        self.update_user_coins(ctx.author.id, coins)
        self.update_user_xp(ctx.author.id, xp)

    @commands.command()
    async def shop(self, ctx):
        embed = discord.Embed(title="Shop", description="Welcome to the shop!")
        embed.add_field(name="XP", value="Price: <:coin:1127703632389865682> 100", inline=False)
        embed.add_field(name="Emoji", value="Price: <:coin:1127703632389865682> 200", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def buy(self, ctx, item: str):
        coins = self.get_user_coins(ctx.author.id)
        if item.lower() == "xp":
            price = 100
            if coins >= price:
                coins -= price
                self.update_user_coins(ctx.author.id, coins)
                await ctx.send(f"{ctx.author.mention} bought XP!")
                channel = self.bot.get_channel(1125999933149949982)
                await channel.send(f"{ctx.author.mention} bought {price} XP!")
            else:
                await ctx.send("Insufficient coins!")
        elif item.lower() == "emoji":
            price = 200
            if coins >= price:
                coins -= price
                self.update_user_coins(ctx.author.id, coins)
                # Perform logic for buying emoji
                await ctx.send(f"{ctx.author.mention} bought an emoji!")
            else:
                await ctx.send("Insufficient coins!")
        else:
            await ctx.send("Item not found in the shop!")

    @commands.command()
    async def balance(self, ctx):
        coins = self.get_user_coins(ctx.author.id)
        await ctx.send(f"{ctx.author.mention} has obtained a total of <:coin:1127703632389865682> {coins}.")

    @commands.command()
    @commands.is_owner()
    async def resetcoins(self, ctx):
        self.cursor.execute("UPDATE user_data SET coins = 0")
        self.conn.commit()
        await ctx.send("All user coins have been reset.")

    @commands.command()
    @commands.is_owner()
    async def givecoins(self, ctx, member: discord.Member, amount: int):
        self.update_user_coins(member.id, amount)
        await ctx.send(f"Gave {amount} coins to {member.mention}.")

    @commands.command()
    @commands.is_owner()
    async def removecoins(self, ctx, member: discord.Member, amount: int):
        current_coins = self.get_user_coins(member.id)
        if current_coins >= amount:
            self.update_user_coins(member.id, -amount)
            await ctx.send(f"Removed {amount} coins from {member.mention}.")
        else:
            await ctx.send("Insufficient coins!")

    def get_user_coins(self, user_id):
        self.cursor.execute("SELECT coins FROM user_data WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0

    def update_user_coins(self, user_id, coins):
        current_coins = self.get_user_coins(user_id)
        total_coins = current_coins + coins
        self.cursor.execute("INSERT OR REPLACE INTO user_data (user_id, coins) VALUES (?, ?)", (user_id, total_coins))
        self.conn.commit()

    def update_user_xp(self, user_id, xp):
        # Perform logic for updating XP
        pass"""


async def setup(bot):
    await bot.add_cog(Unlock(bot))
