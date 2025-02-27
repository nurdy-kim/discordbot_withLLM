import discord
from discord.ext import commands
import asyncio
import os
from google import genai
from google.genai import types
from utils.logger import logger

TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
      ]
    )

if not GEMINI_API_KEY:
    logger.error("GOOGLE_API_KEY 값을 가져 올 수 없습니다.")
    raise ValueError("GOOGLE_API_KEY 값을 가져 올 수 없습니다.")

class ChatThreadCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.llm_client = genai.Client(api_key=GEMINI_API_KEY)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if message.channel.id == TARGET_CHANNEL_ID:
            logger.info(f"[LLM] Received message: {message.content} - by {message.author}.")
            try:
                response = await asyncio.to_thread(
                    self.llm_client.models.generate_content,
                    model="models/gemini-1.5-flash-latest",
                    contents=message.content,
                    config=config
                )
                if response and hasattr(response, "text"):
                    answer = response.text
                else:
                    answer = "[ERROR] 응답을 받지 못했습니다."
                    logger.error(f"[LLM] 요청 중 오류 발생")
            except Exception as e:
                answer = f"요청 중 오류가 발생했습니다: {e}"
                logger.error("[LLM] 요청중 오류 발생")
            await message.channel.send(answer)

async def setup(bot: commands.Bot):
    await bot.add_cog(ChatThreadCog(bot))
    logger.info("[DEBUG] ChatThreadCog 추가 완료.")
