"""Views for the user_db cog"""
import logging
from select import select
from typing import List
import discord
from discord import ui
import aiohttp
import os
import re

logger = logging.getLogger('discord')

class MemberNameEmailModal(discord.ui.Modal, title="Membership Data"):
    """Where our members can put their information securely and easily"""
    name = ui.TextInput(label='First and Last name')
    email = ui.TextInput(label='Rose Email', placeholder="xyler123@rose-hulman.edu")
    
    def __init__(self, active_role: int, aspiring_role: int):
        super().__init__()
        self.active_role = active_role
        self.aspiring_role = aspiring_role

    # pylint: disable=arguments-differ
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        """Interaction on error"""
        await interaction.response.send_message(f"Oops! Something went wrong. {error}", ephemeral=True)
        logger.warning(error)

    # pylint: disable=arguments-differ
    async def on_submit(self, interaction: discord.Interaction):
        """ On Submit if not already an active member, add them to the DB """
        user = interaction.user
        response_code = 0
        cookies = {}
        async with aiohttp.ClientSession() as session:
            csrf_token = ''
            async with session.get("http://localhost:8000/attendance/update_member/") as response:
                text = await response.text()
                csrf_token = re.search(r"<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"(\w+)\">", text).group(1)
                cookies = response.cookies
            async with session.post(
                "http://localhost:8000/attendance/update_member/",
                cookies = cookies,
                data={
                    'full_name':self.name, 'email': self.email, 'snowflake': interaction.user.id,
                    'user':'discord_bot', 'password': os.environ['AUTHPASS'], 'csrfmiddlewaretoken':csrf_token
                }
            ) as response:
                response_code = response.status

        if response_code != 200:
            return await interaction.response.send_message(
                f"Failed to update your information. Response from server: HTTP{response_code}", ephemeral=True
            )
            
        #If not an active member
        if user.get_role(int(self.active_role)) is None:
            # Give aspiring member role.
            user.add_roles(int(self.aspiring_role))
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