from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from emoji import emojize as em

from db_handlers.for_filters import get_first_time_save
from db_handlers.main_functions import save_user
from keyboards.inline import menu_kb, timezones_kb
from services.functions import generate_menu_caption


start_router = Router()

@start_router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    save_user(user_id)

    BG_logo = FSInputFile("images/BG_logo.jpg")
    
    if get_first_time_save(message.from_user.id)[0] =='not yet':
        text=em("Привет!:waving_hand:\n\nЯ помогу тебе быстрее отрастить бороду и волосы. Буду напоминать тебе использовать средство и следить за результатами.\n\nДавай выберем удобное время для напоминаний. Но для начала укажи свой часовой пояс:") 
        rm=timezones_kb()
    else:
        text=generate_menu_caption(user_id)
        rm=menu_kb(user_id)
        
    await message.answer_photo(
        BG_logo,
        caption=text,
        reply_markup=rm
        )
    await state.clear()
    
@start_router.callback_query(lambda c: c.data == "to_menu")
async def cmd_start(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    save_user(user_id)

    BG_logo = FSInputFile("images/BG_logo.jpg")
    
    if get_first_time_save(call.from_user.id)[0] =='not yet':
        text=em("Привет!:waving_hand:\n\nЯ помогу тебе быстрее отрастить бороду и волосы. Буду напоминать тебе использовать средство и следить за результатами.\n\nДавай выберем удобное время для напоминаний. Но для начала укажи свой часовой пояс:") 
        rm=timezones_kb()
    else:
        text=generate_menu_caption(user_id)
        rm=menu_kb(user_id)
        
    await call.message.answer_photo(
        BG_logo,
        caption=text,
        reply_markup=rm
        )
    
    await call.answer()
    await state.clear()
