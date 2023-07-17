import discord
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play_song', help='To play a song')
    async def play(self, ctx, url):
        server = ctx.guild
        voice_client = server.voice_client
        async with ctx.typing():
            voice_client.play(discord.FFmpegPCMAudio(url))
        await ctx.send('Now playing: {}'.format(url))

    @commands.command(name='join', help='Tells the bot to join the voice channel')
    async def join(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None

        if not voice_channel:
            return await ctx.send("You must be in a voice channel to use this command.")

        voice_client = ctx.guild.voice_client

        if voice_client and voice_client.channel == voice_channel:
            return await ctx.send("I'm already in your voice channel.")

        try:
            await voice_channel.connect()
            await ctx.send(f"I have joined the voice channel: {voice_channel.name}")
        except discord.errors.Forbidden:
            await ctx.send("I don't have permission to join your voice channel.")
        except Exception as e:
            await ctx.send(f"An error occurred while joining the voice channel: {str(e)}")




    @commands.command(name='pause', help='This command pauses the song')
    async def pause(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

    @commands.command(name='resume', help='Resumes the song')
    async def resume(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_paused():
            voice_client.resume()
        else:
            await ctx.send("The bot was not playing anything before this. Use play_song command")

    @commands.command(name='leave', help='To make the bot leave the voice channel')
    async def leave(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command(name='stop', help='Stops the song')
    async def stop(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(Music(bot))