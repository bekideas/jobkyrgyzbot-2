from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from services.db import save_seeker_anketa

router = Router()

# Шаги анкеты
class SeekerForm(StatesGroup):
    name = State()
    city = State()
    position = State()
    skills = State()
    experience = State()
    contact = State()


# Запуск FSM
async def start_seeker_fsm(message: Message, state: FSMContext = None):
    await message.answer("Введите ваше имя:")
    await state.set_state(SeekerForm.name)


@router.message(SeekerForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Город?")
    await state.set_state(SeekerForm.city)

@router.message(SeekerForm.city)
async def get_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer("На какую должность претендуете?")
    await state.set_state(SeekerForm.position)

@router.message(SeekerForm.position)
async def get_position(message: Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer("Ваши ключевые навыки?")
    await state.set_state(SeekerForm.skills)

@router.message(SeekerForm.skills)
async def get_skills(message: Message, state: FSMContext):
    await state.update_data(skills=message.text)
    await message.answer("Опыт работы?")
    await state.set_state(SeekerForm.experience)

@router.message(SeekerForm.experience)
async def get_experience(message: Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await message.answer("Контакт (телефон, Telegram)?")
    await state.set_state(SeekerForm.contact)

@router.message(SeekerForm.contact)
async def get_contact(message: Message, state: FSMContext):
    await state.update_data(contact=message.text)

    data = await state.get_data()
    await save_seeker_anketa(user_id=message.from_user.id, **data)

    await message.answer("✅ Анкета сохранена и будет опубликована после проверки.")
    await state.clear()
