from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

usrou = Router()


class reg(StatesGroup):
    start = State()
    vacancy = State()
    user_data = State()


@usrou.message(reg.start)
async def select_workshop(message: Message, state: FSMContext) -> None:
    print(message.text)
    await state.update_data(start=message.text)
    await state.set_state(reg.vacancy)
    await message.answer(f"<i>Выберите тип вакансии... 👀</i>")


@usrou.message(reg.vacancy)
async def nachalo(message: Message, state: FSMContext) -> None:
    print(message.text)
    await state.update_data(vacancy=message.text)
    await state.set_state(reg.user_data)
    await message.answer("<i>Введите ваше ФИО</i>")


@usrou.message(reg.user_data)
async def fioshka(message: Message, state: FSMContext) -> None:
    print(message.text)
    await state.update_data(user_data=message.text)
    data = await state.get_data()
    await message.answer(f"{data['start']}, {data['vacancy']}, {data['user_data']}")
    await state.clear()
