import json
from discord.ext import commands

class custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.custom_commands = {}  # Dictionary to store custom commands

        # Load custom commands from JSON file
        self.load_custom_commands()

    def load_custom_commands(self):
        try:
            with open("custom.json", "r") as file:
                self.custom_commands = json.load(file)
        except FileNotFoundError:
            self.custom_commands = {}

    def save_custom_commands(self):
        with open("custom.json", "w") as file:
            json.dump(self.custom_commands, file)

    @commands.command()
    @commands.guild_only()  # Make the command only work in guilds (servers)
    @commands.has_permissions(manage_guild=True)  # Make the command only accessible by users with 'manage_guild' permission
    async def newcmd(self, ctx, command_name, command_response):
        # Check if the command is being executed in the desired server
        if ctx.guild.id != 1121841073673736215:
            return

        # Add the custom command to the dictionary
        self.custom_commands[command_name.lower()] = command_response

        # Save the updated custom commands to JSON file
        self.save_custom_commands()

        await ctx.send(f"Custom command '{command_name}' has been added!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # Check if the message is a custom command
        content = message.content.lower()
        if content in self.custom_commands:
            response = self.custom_commands[content]
            await message.channel.send(response)

    @commands.command()
    async def removecmd(self, ctx, command_name):
        server_id = str(ctx.guild.id)
        custom_commands = {}

        try:
            with open("custom.json", "r") as file:
                custom_commands = json.load(file)
        except FileNotFoundError:
            pass

        if server_id in custom_commands and command_name in custom_commands[server_id]:
            del custom_commands[server_id][command_name]
            with open("custom.json", "w") as file:
                json.dump(custom_commands, file, indent=4)
            await ctx.send(f"The custom command `{command_name}` has been removed.")
        else:
            await ctx.send(f"The custom command `{command_name}` does not exist.")



async def setup(bot):
    await bot.add_cog(custom(bot))