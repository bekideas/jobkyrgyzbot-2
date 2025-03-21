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
import aiosqlite

DB_NAME = "jobkyrgyz.db"

# Проверка: есть ли анкета
async def user_has_anketa(user_id: int) -> bool:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT 1 FROM ankets WHERE user_id=? AND role='seeker'", (user_id,)) as cursor:
            return await cursor.fetchone() is not None

# Сохранение анкеты
async def save_seeker_anketa(user_id, name, city, position, skills, experience, contact):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            INSERT OR REPLACE INTO ankets 
            (user_id, role, name, city, position, skills, experience, contact, status)
            VALUES (?, 'seeker', ?, ?, ?, ?, ?, ?, 'active')
        ''', (user_id, name, city, position, skills, experience, contact))
        await db.commit()
