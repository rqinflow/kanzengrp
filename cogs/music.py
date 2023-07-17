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
        # Check if the command author is in a voice channel
        if ctx.author.voice is None:
            return await ctx.send("You must be in a voice channel to use this command.")

        # Get the voice channel ID
        channel_id = 1055799905978957854  # Replace with the desired voice channel ID
    
        try:
            # Attempt to retrieve the voice channel
            channel = await self.bot.fetch_channel(channel_id)
        except discord.NotFound:
            return await ctx.send("The specified voice channel was not found.")

        # Check if the bot is already in a voice channel
        if ctx.guild.voice_client is not None:
            return await ctx.send("I am already connected to a voice channel.")

        # Connect to the voice channel
        try:
            voice_client = await channel.connect()
        except discord.Forbidden:
            return await ctx.send("I don't have permission to join that voice channel.")
        except discord.ClientException:
            return await ctx.send("I am already connected to a voice channel.")

        await ctx.send(f"I have joined the voice channel: {channel.name}")


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