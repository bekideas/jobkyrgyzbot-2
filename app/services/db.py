import aiosqlite

DB_NAME = "jobkyrgyz.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS ankets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            role TEXT,
            name TEXT,
            city TEXT,
            position TEXT,
            skills TEXT,
            experience TEXT,
            contact TEXT,
            company TEXT,
            requirements TEXT,
            salary TEXT,
            status TEXT,
            created_at TEXT,
            updated_at TEXT
        )
        ''')
        await db.commit()
