# Фоновый скрипт для удаления старых анкет (планируется запуск по cron)
import aiosqlite
import asyncio
from datetime import datetime, timedelta

async def delete_old_records():
    async with aiosqlite.connect("jobkyrgyz.db") as db:
        threshold_date = (datetime.utcnow() - timedelta(days=7)).isoformat()
        await db.execute("DELETE FROM ankets WHERE created_at < ?", (threshold_date,))
        await db.commit()

if __name__ == "__main__":
    asyncio.run(delete_old_records())
