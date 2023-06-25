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

    @commands.command()
    async def effects(self, ctx):
        choices = ["4-Color Gradient", "S_HalfTone", "Gradient Ramp", "S_PseudoColor", "S_FlysEyeHex", "S_WipeTiles", "S_EdgeRays", "S_WipeMoire", "S_WipeDots", "S_WipePixelate", "S_WipePlasma", "S_WipeFlux", "S_GlowDist", "S_Glint", "Glow", "Turbulent Displace", "Wave Warp", "BCC lens blur OBS", "Invert", "Exposure", "BCC Cross Glitch", "BCC LED", "Omino Diffuse", "Omino Squares", "Grid"]
        raneffect = random.choice(choices)
        await ctx.reply(raneffect)

    @commands.command()
    async def transition(self, ctx):
        choices = ["Warp Fisheye", "Zoom in", "Zoom out", "Inside Cube", "Ink Splash", "Split Cube", "Polaroid Pop Up", "CC scale wipe", "3D flip", "3D tunnel", "Tile Scramble", "do something with a cube, dont be lazy", "idfk... look at someone's edits take inspo from them (GIVE THEM IB CREDITS THOUGH)", "rotation", "slide down", "slide right", "slide left", "slide up", "slide somewhere", "3D flip into a cube", "i can't think of anything... do the command again"]
        raneffect = random.choice(choices)
        await ctx.reply(raneffect)

async def setup(bot):
    await bot.add_cog(editing(bot))