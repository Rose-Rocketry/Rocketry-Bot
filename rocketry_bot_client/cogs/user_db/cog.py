"""Handles user database"""
import logging
import discord
from discord import app_commands
from discord.ext import commands

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

@app_commands.guild_only()
class MemberManagement(commands.Cog):
    """A cog for handling the membership DB"""
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="update-profile", description="Update your profile")
    async def update_profile(self, interaction: discord.Interaction):
        """Securely update your Rocketry Profile information."""
        await interaction.response.send_modal(MemberNameEmailModal())

    

    @app_commands.command(name="select_projects", description="Add yourself to the projects that interest you!")
    async def setup_role_markers(self, interaction: discord.Interaction):
        """Create a role selector for a group of related roles."""
        view =  RoleSelectionView(project_options, self.handle_project_selection)
        await interaction.channel.send("__TEST__: What Projects Interest You?:",view=view)
        print("Sent views")
        await interaction.response.send_message("Warning this command is a WIP", ephemeral=True)

async def setup(bot):
    """Sets up bot with cog"""
    print("Loading USERDB")
    await bot.add_cog(
        MemberManagement(bot),
         guilds=[ROCKETRY_GUILD]
    )
