from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from emoji import emojize as em

def set_time_inline_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Утро", callback_data='morning')],
        [InlineKeyboardButton(text="Вечер", callback_data='evening')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def get_serum_inline_kb(user_id):
    inline_kb_list = [
        [InlineKeyboardButton(text=em(":check_mark_button: Принял средство"), callback_data=f'used_{str(user_id)}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)