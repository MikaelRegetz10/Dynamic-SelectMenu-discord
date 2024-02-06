import discord
from discord.ext import commands
import settings

my_guild = discord.Object(id=settings.ID_SERVER)


class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())

        self.coglist = ["cogs.dynamicmenu"]

    async def setup_hook(self):
        for ext in self.coglist:
            await self.load_extension(ext)

        self.tree.copy_global_to(guild=my_guild)
        await self.tree.sync(guild=my_guild)


client = MyClient()


@client.event
async def on_ready():
    print(f'Ready, started with {client.user}.')

client.run(settings.TOKEN_DISCORD)