from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import CommandStart
from services.db import user_has_anketa  # проверка анкеты
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    # Проверка: есть ли анкета?
    exists = await user_has_anketa(message.from_user.id)

    if exists:
        await message.answer("✅ У вас уже есть анкета.\n\nКоманда: /мояанкета для просмотра или изменения.")
        return

    # Если анкеты нет — предлагаем выбрать роль
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👤 Соискатель", callback_data="role_seeker")],
        [InlineKeyboardButton(text="🏢 Работодатель", callback_data="role_employer")]
    ])
    await message.answer("Добро пожаловать в JobKyrgyz Bot!\n\nВыберите, кто вы:", reply_markup=kb)


# Обработка нажатия на кнопку выбора роли
@router.callback_query(F.data.in_({"role_seeker", "role_employer"}))
async def role_selected(callback: CallbackQuery):
    role = "Соискатель" if callback.data == "role_seeker" else "Работодатель"
    await callback.message.answer(f"Отлично, вы выбрали роль: {role}\nДавайте начнем анкетирование!")

    # Импортируем нужную FSM и запускаем (позже)
    if callback.data == "role_seeker":
        from handlers.seeker import start_seeker_fsm
        await start_seeker_fsm(callback.message)
    else:
        from handlers.employer import start_employer_fsm
        await start_employer_fsm(callback.message)

    await callback.answer()
