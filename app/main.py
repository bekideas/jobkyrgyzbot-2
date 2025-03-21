import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import common, seeker, employer, edit
from services.db import init_db
import logging

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    
    dp.include_routers(common.router, seeker.router, employer.router, edit.router)
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
