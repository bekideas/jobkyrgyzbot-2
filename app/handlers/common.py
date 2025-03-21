from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

router = Router()


# Команда /start — в личке
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Добро пожаловать в JobKyrgyz Bot!\n"
        "Выберите, кто вы:\n\n"
        "👤 Соискатель\n"
        "🏢 Работодатель"
    )


# Сообщения в группе — проверка регистрации и приглашение
@router.message(F.chat.type.in_({"group", "supergroup"}))
async def group_message_handler(message: Message):
    # 👉 Здесь должна быть проверка пользователя в БД (пока убираем)

    # Удаляем сообщение
    try:
        await message.delete()
    except Exception:
        pass  # не страшно, если не смог удалить

    # Пишем в личку
    try:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Пройти анкетирование", url=f"https://t.me/{(await message.bot.me()).username}")]
        ])
        await message.bot.send_message(
            chat_id=message.from_user.id,
            text="👋 Добро пожаловать! Чтобы писать в чат, пройдите анкетирование.",
            reply_markup=kb
        )
    except Exception:
        pass  # если пользователь не написал боту первым — не получится отправить
