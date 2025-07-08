from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from emoji import emojize as em
from config import admins

def set_time_inline_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Утро", callback_data='morning')],
        [InlineKeyboardButton(text="Вечер", callback_data='evening')],
        [InlineKeyboardButton(text=em(":muted_speaker: Отключить"), callback_data='del')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def get_serum_inline_kb(user_id):
    inline_kb_list = [
        [InlineKeyboardButton(text=em(":check_mark_button: Принял средство"), callback_data=f'used_{str(user_id)}_not')],
        [InlineKeyboardButton(text=em(":multiply: Пропуск"), callback_data=f'used_{str(user_id)}_yes')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def get_time_of_day_kb_H(time_period):
    if time_period == "morning":
        inline_kb_list = [
            [
            InlineKeyboardButton(text="06:", callback_data=f"time_H_{time_period}_06"),
            InlineKeyboardButton(text="10:", callback_data=f"time_H_{time_period}_10")
            ], [
            InlineKeyboardButton(text="07:", callback_data=f"time_H_{time_period}_07"),
            InlineKeyboardButton(text="11:", callback_data=f"time_H_{time_period}_11")
            ], [
            InlineKeyboardButton(text="08:", callback_data=f"time_H_{time_period}_08"),
            InlineKeyboardButton(text="12:", callback_data=f"time_H_{time_period}_12")
            ], [
            InlineKeyboardButton(text="09:", callback_data=f"time_H_{time_period}_09"),
            InlineKeyboardButton(text="13:", callback_data=f"time_H_{time_period}_13")
            ]
        ]
    elif time_period == "evening":
        inline_kb_list = [
            [
            InlineKeyboardButton(text="17:", callback_data=f"time_H_{time_period}_17"),
            InlineKeyboardButton(text="21:", callback_data=f"time_H_{time_period}_21")
            ], [
            InlineKeyboardButton(text="18:", callback_data=f"time_H_{time_period}_18"),
            InlineKeyboardButton(text="22:", callback_data=f"time_H_{time_period}_22")
            ], [
            InlineKeyboardButton(text="19:", callback_data=f"time_H_{time_period}_19"),
            InlineKeyboardButton(text="23:", callback_data=f"time_H_{time_period}_23")
            ], [
            InlineKeyboardButton(text="20:", callback_data=f"time_H_{time_period}_20"),
            InlineKeyboardButton(text="00:", callback_data=f"time_H_{time_period}_00")
            ]
        ]
    
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def get_time_of_day_kb(time_period, time_H):
    inline_kb_list = [
        [
            InlineKeyboardButton(text="00", callback_data=f"fulltime_{time_period}_{time_H}_00"),
            InlineKeyboardButton(text="15", callback_data=f"fulltime_{time_period}_{time_H}_15"),
            InlineKeyboardButton(text="30", callback_data=f"fulltime_{time_period}_{time_H}_30"),
            InlineKeyboardButton(text="45", callback_data=f"fulltime_{time_period}_{time_H}_45")
        ]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def timezones_kb(selected_time=None):
    inline_kb_list = [
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 2 else ''} (+2) Калининград"), callback_data="timezone_2")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 3 else ''} (+3) Москва"), callback_data="timezone_3")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 4 else ''} (+4) Самара"), callback_data="timezone_4")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 5 else ''} (+5) Екатеринбург"), callback_data="timezone_5")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 6 else ''} (+6) Омск"), callback_data=f"timezone_6")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 7 else ''} (+7) Красноярск"), callback_data=f"timezone_7")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 8 else ''} (+8) Иркутск"), callback_data=f"timezone_8")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 9 else ''} (+9) Якутск"), callback_data=f"timezone_9")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 10 else ''} (+10) Владивосток"), callback_data=f"timezone_10")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 11 else ''} (+11) Магадан"), callback_data=f"timezone_11")],
        [InlineKeyboardButton(text=em(f"{':check_mark:' if selected_time == 12 else ''} (+12) Камчатка"), callback_data=f"timezone_12")],
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def menu_kb(user_id):
    inline_kb_list = [
        [InlineKeyboardButton(text="Сменить время напоминаний", callback_data="set_time")],
        [InlineKeyboardButton(text="Выбрать другой часовой пояс", callback_data="set_timezone")]
    ]
    if str(user_id) in admins:
        inline_kb_list.append([InlineKeyboardButton(text=em(":loudspeaker: Отправить сообщение"), callback_data="send_notify")])
        inline_kb_list.append([InlineKeyboardButton(text=em(":bar_chart: Статистика"), callback_data="show_stat")])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def to_menu_kb():
    inline_kb_list = [[InlineKeyboardButton(text="В меню", callback_data="to_menu")],]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)