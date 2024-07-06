from aiogram.types import ReplyKeyboardMarkup,KeyboardButton , InlineKeyboardMarkup , InlineKeyboardButton

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Добавить админа", callback_data="add_admin"),
            InlineKeyboardButton(text="Удалить админа", callback_data="delete_admin")
        ],
        [
            InlineKeyboardButton(text="Добавить цех", callback_data="add_cheh"),
            InlineKeyboardButton(text="Удалить цех", callback_data="delete_cheh")

        ]
    ]
)
