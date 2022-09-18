"""Module for building the Rosie Rocketeer Client"""
import logging
import discord
from discord.ext import commands
from discord import app_commands

ROCKETRY_GUILD = discord.Object(id=728794908852224093)

logger = logging.getLogger('rosie')

class RosieClient(commands.Bot):
    """The class for Rosie Rocketeer Client"""
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        super().__init__(command_prefix='/',intents=intents, *args, **kwargs)

    async def on_ready(self):
        """Things to do when readied"""
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('--------')

    async def setup_hook(self) -> None:
        """Setup the server control task here"""
        await self.load_extension('cogs.user_db.cog')
        await self.tree.sync(guild=ROCKETRY_GUILD)

    async def host_background_task(self):
        """Updates bot with tasks that need to be assigned
        TODO: Setup event loop on web-base
        """
        await self.wait_until_ready()

DEFAULT_ROSIE = RosieClient()

@DEFAULT_ROSIE.tree.command(guild=ROCKETRY_GUILD)
async def reload_cogs(interaction: discord.Interaction):
    """Reloads the user_db cog"""
    testers = [352258945995243525]
    if interaction.user.id not in testers:
        logger.info("User %s failed test.", interaction.user)
        return await interaction.respond.send_message("You can't do that :7")

    try:
        await DEFAULT_ROSIE.reload_extension('cogs.user_db.cog')
        await interaction.response.send_message("Successfully reloaded", ephemeral=True)
        await DEFAULT_ROSIE.tree.sync()
    except discord.ext.commands.ExtensionFailed as error:
        print("Failed to reload extension")
        logging.error(error)
        await interaction.response.send_message("Falied to reload", ephemeral=True)
