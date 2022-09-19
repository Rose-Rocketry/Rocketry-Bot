"""Handles user database"""
import logging
import discord
from discord import app_commands
from discord.ext import commands
import aiohttp
import json

from .views import MemberNameEmailModal, RoleSelectionView

logger = logging.getLogger('user_db')

ROCKETRY_GUILD = discord.Object(id=728794908852224093)

project_options = [
    discord.SelectOption(label="USLI", value=1011074585917128826, emoji="🚀"),
    discord.SelectOption(label="Aspiring L1 :orange:", description="Build your own rocket 🤯", value=1016055798092267650, emoji="🟠"),
    discord.SelectOption(label="Aspiring L2 :blue:", value=1016056041856835594, emoji="🔵"),
    discord.SelectOption(label="RPL", description="Rose Propulsion Laboratory", value=863504938332061726, emoji="🔥"),
    discord.SelectOption(label="Concrete Rocket", value=967931020022272000, emoji="🥌"),
]

class GuildNotFoundError(Exception):
    """Guild is not found error."""

async def get_guild_settings(guild_id):
    """Gets the guild settings from our database"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8000/attendance/guild_settings/{guild_id}") as response:
            if response.status != 200:
                raise GuildNotFoundError()

            return json.loads(await response.text())

@app_commands.guild_only()
class MemberManagement(commands.Cog):
    """A cog for handling the membership DB"""
    def __init__(self, bot):
        self.bot = bot
        self.background_task = bot.loop.create_task()

    async def task_check(self):
        """Periodically checks for tasks in the database."""
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            pass

    async def cog_unload(self):
        self.background_task.cancel()

    @app_commands.command(name="update-profile", description="Update your profile")
    async def update_profile(self, interaction: discord.Interaction):
        """Securely update your Rocketry Profile information."""
        guild_settings = {}
        try:
            guild_settings = await get_guild_settings(interaction.guild.id)
        except GuildNotFoundError:
            return await interaction.response.send_message("This guild is not registered. Contact the creator for help.", ephemeral=True)
        
        modal = MemberNameEmailModal(guild_settings["active_member_snowflake"], guild_settings["aspiring_member_snowflake"])
        return await interaction.response.send_modal(modal)

    @app_commands.command(name="select_projects", description="Add yourself to the projects that interest you!")
    async def setup_role_markers(self, interaction: discord.Interaction):
        """Create a role selector for a group of related roles."""
        view = RoleSelectionView(project_options)
        await interaction.channel.send("__TEST__: What Projects Interest You?:",view=view)
        print("Sent views")
        await interaction.response.send_message("Warning this command is a WIP", ephemeral=True)

async def setup(bot):
    """Sets up bot with cog"""
    print("Loading USERDB")
    cog = MemberManagement(bot)
    await bot.add_cog(
        cog,
        guilds=[ROCKETRY_GUILD]
    )
    
