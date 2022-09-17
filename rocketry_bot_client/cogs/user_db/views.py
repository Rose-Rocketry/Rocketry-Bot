"""Views for the user_db cog"""
from select import select
from typing import List
import discord
from discord import ui

class MemberNameEmailModal(discord.ui.Modal, title="Membership Data"):
    """Where our members can put their information securely and easily"""
    name = ui.TextInput(label='First and Last name')

    email = ui.TextInput(label='Rose Email', placeholder="xyler123@rose-hulman.edu")

    # pylint: disable=arguments-differ
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        """Interaction on error"""
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        print(error.__traceback__)

    # pylint: disable=arguments-differ
    async def on_submit(self, interaction: discord.Interaction):
        """ On Submit if not already an active member, add them to the DB """
        user = interaction.user
        #If not an active member
        if user.get_role(772985856461504514) is None:
            user.add_roles(748717724863299596)
            await interaction.response.send_message("Welcome to Rose-Rocketry!", ephemeral=True)
        else:
            await interaction.response.send_message("Updated your information!", ephemeral=True)

class RoleSelectionView(discord.ui.View):
    """A view designed for role selection"""
    # TODO Make options as part of the constructor.
    def __init__(self):
        super().__init__()
        selection_box = discord.ui.Select()
        selection_box.add_option(label="USLI")
        selection_box.add_option(label="Aspiring L1",)
        selection_box.add_option(label="Aspiring L2")
        selection_box.add_option(label="RPL")
        selection_box.add_option(label="CubeSAT")
        selection_box.max_values = len(selection_box.options)
        selection_box.callback = self.role_selected
        self.selection_box = selection_box
        self.add_item(selection_box)
    
    async def role_selected(self, interaction: discord.Interaction):
        """Handles when a role is selected"""
        await interaction.response.send_message("Shoot")
        self.selection_box.add_option("biscuit")