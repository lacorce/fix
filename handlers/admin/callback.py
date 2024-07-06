from aiogram.types import CallbackQuery , Message
from aiogram import Router , F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database import database as db
class Add(StatesGroup):
    cheh = State()
    vacancy = State()
    question = State()

acrou = Router()

@acrou.callback_query(F.data == "add_cheh")
async def add_cheh(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Add.cheh)
    await callback_query.message.edit_text("Введите название нового цеха")

@acrou.message(Add.cheh)
async def add_vacancy(message: Message, state: FSMContext):
    print(message.text)
    await state.update_data(cheh=message.text)
    await state.set_state(Add.vacancy)
    await message.answer("Введите название новой вакансии")

@acrou.message(Add.vacancy)
async def add_ques(message: Message, state: FSMContext):
    await state.update_data(vacancy=message.text)
    await state.set_state(Add.question)
    await message.answer("Введите вопрос")

@acrou.message(Add.question)
async def end(message: Message, state: FSMContext):
    await state.update_data(question=message.text)
    data = await state.get_data()
    a = data['cheh']
    b = data['vacancy']
    c = data['question']
    await db.add_tseh(a,b,c)
    print(a,b,c)
