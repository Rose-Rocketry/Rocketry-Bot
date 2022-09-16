"""Main file for runing discord client bot"""
import asyncio
import logging
import logging.handlers
import os

from rosie_bot import DEFAULT_ROSIE

async def main():
    """Bot initialization and startup."""
    # Setup Logging
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32*1024*1024,
        backupCount=5,
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(
        '[{asctime}] [{levelname:<8}] {name}: {message}',
        dt_fmt,
        style="{"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Run the bot
    bot_key = os.environ["BOTKEY"]
    await DEFAULT_ROSIE.start(bot_key)

asyncio.run(main())
