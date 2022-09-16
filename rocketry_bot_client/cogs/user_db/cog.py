"""Handles user database"""
from typing import List
import logging
import discord
from discord import app_commands
from discord.ext import commands

from .views import MemberNameEmailModal, RoleSelectionView

logger = logging.getLogger('user_db')

ROCKETRY_GUILD = discord.Object(id=728794908852224093)

@app_commands.guild_only()
class MemberManagement(commands.Cog):
    """A cog for handling the membership DB"""
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="update-profile", description="Update your profile")
    async def update_profile(self, interaction: discord.Interaction):
        """Securely update your Rocketry Profile information."""
        await interaction.response.send_modal(MemberNameEmailModal())

    @app_commands.command(name="setup_roles", description="Add by roles")
    async def setup_role_markers(self, interaction: discord.Interaction):
        """Create a role selector for a group of related roles."""
        view =  RoleSelectionView()
        await interaction.channel.send("test",view=view)
        print("Sent views")
        await interaction.response.send_message("Warning this command is a WIP", ephemeral=True)

async def setup(bot):
    """Sets up bot with cog"""
    print("Loading USERDB")
    await bot.add_cog(
        MemberManagement(bot),
         guilds=[ROCKETRY_GUILD]
    )
