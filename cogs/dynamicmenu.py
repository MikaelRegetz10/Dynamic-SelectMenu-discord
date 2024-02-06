import discord
from discord.ext import commands
from discord import app_commands
import models.queries as queires


class DynamicSelectMenu(discord.ui.Select):
    def __init__(self, options, placeholder):
        super().__init__(placeholder=placeholder, options=options)

    def update_options(self, new_pag_options):
        self.options = new_pag_options

    def update_placeholder(self, new_placeholder):
        self.placeholder = new_placeholder

    async def callback(self, interaction: discord.Interaction):
        """
        your script
        """
        pass


class DynamicMenuConfig(discord.ui.View):
    def __init__(self, options):
        super().__init__(timeout=None)
        self.pagina = 0
        self.options = options
        self.max_pag = len(options) - 1
        self.placeholder = f"Your placeholder (Pag {self.pagina + 1})"
        self.view = DynamicSelectMenu(options[self.pagina], self.placeholder)
        self.add_item(self.view)

    async def update_buttons(self, interaction: discord.Interaction):
        if self.pagina == 0:
            self.prev_button.disabled = True
        else:
            self.prev_button.disabled = False

        if self.pagina == self.max_pag:
            self.pass_button.disabled = True
        else:
            self.pass_button.disabled = False

        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='⬅', style=discord.ButtonStyle.blurple, custom_id='prev_button_spell', disabled=True)
    async def prev_button(self, interaction: discord.Interaction, button: discord.Button):
        self.pagina -= 1
        self.placeholder = f"Your placeholder (Pag {self.pagina + 1})"
        self.view.update_placeholder(self.placeholder)
        self.view.update_options(self.options[self.pagina])
        await self.update_buttons(interaction)

    @discord.ui.button(label='➡', style=discord.ButtonStyle.blurple, custom_id='pass_button_spell')
    async def pass_button(self, interaction: discord.Interaction, button: discord.Button):
        self.pagina += 1
        self.placeholder = f"Your placeholder (Pag {self.pagina + 1})"
        self.view.update_placeholder(self.placeholder)
        self.view.update_options(self.options[self.pagina])
        await self.update_buttons(interaction)


class TestDynamicMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='Test', description='Test dynamic selectMenu with mysql')
    async def test(self, interaction: discord.Interaction):
        infos = queires.select_name()['data']
        options = []
        for info in infos:
            pag_options = [discord.SelectOption(label=name) for name in info]
            options.append(pag_options)

        await interaction.response.send_message(
            f"Your dynamic selectmenu",
            view=DynamicMenuConfig(options),
            ephemeral=True,
            delete_after=3
        )

async def setup(client: commands.Bot):
    await client.add_cog(TestDynamicMenu(client))