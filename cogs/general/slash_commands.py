import discord
from discord.ext import commands

class GeneralSlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="hello", description="봇에게 인사를 보내보세요!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("안녕하세요! 좋은 하루입니다!")

async def setup(bot: commands.Bot):
    await bot.add_cog(GeneralSlashCommands(bot))