from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from database import database as db
from aiogram.fsm.context import FSMContext
from handlers.user.message import usrou, reg
from handlers.admin.keyboard import admin_keyboard
from handlers.admin.callback import acrou
from handlers.config import token

dp = Dispatcher()
bot = Bot(token=token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def hello(message: Message, state: FSMContext):
    if message.from_user.id == 6292728634:
        await message.answer(f"<b>{message.from_user.first_name} , вы успешно вошли в админку</b>",
                             reply_markup=admin_keyboard)
    else:
        await state.set_state(reg.start)
        await message.answer("<b>Привет, выбери цех</b>")


async def start():
    db.create_table()
    dp.include_router(acrou)
    dp.include_router(usrou)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start())
