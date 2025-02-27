import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.logger import logger

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

class DiscordBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix="!", intents=intents, **kwargs)

    async def on_ready(self):
        extensions = [
            "cogs.general.slash_commands",
            "cogs.llm",
        ]

        for ext in extensions:
            try:
                await self.load_extension(ext)
                logger.info(f"[SYSTEM] Loaded extension: {ext}")
            except Exception as e:
                logger.error(f"[SYSTEM] Failed to load extension: {ext}: {e}")

        await self.tree.sync()
        logger.info("[SYSTEM] Slash commands synchronized.")
        logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")

bot = DiscordBot()
bot.run(TOKEN)