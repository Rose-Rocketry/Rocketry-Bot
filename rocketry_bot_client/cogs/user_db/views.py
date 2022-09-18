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
    """A view designed for role selection. This may overwrite the value of the option."""
    # TODO Make options as part of the constructor.
    def __init__(self, roles: List[discord.SelectOption]):
        super().__init__()
        selection_box = discord.ui.Select()
        self.role_options = []

        for i in range(0, min(len(roles), 25)):
            selection_box.append_option(roles[i])
            self.role_options.append(discord.Object(roles[i].value))

        selection_box.max_values = len(roles)
        selection_box.callback = self.handle_update
        self.selection_box = selection_box
        self.add_item(selection_box)
    
    async def handle_update(self, interaction: discord.Interaction):
        #List of roles that the user has
        await interaction.user.remove_roles(self.role_options)

        await interaction.response.send_message()