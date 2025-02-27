import logging
import logging.handlers
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE = os.getenv("LOG_FILE", "bot.log")

logger = logging.getLogger("discord_bot")
logger.setLevel(LOG_LEVEL)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler=logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=10*1024*1024, backupCount=5, encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

if __name__ == "__main__":
    logger.info("Logger가 성공적으로 설정되었습니다.")