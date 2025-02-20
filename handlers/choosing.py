from aiogram import Bot, Router
from aiogram.types import CallbackQuery

from db_handlers.for_filters import get_first_time_save
from db_handlers.main_functions import del_time, save_reminder, save_timezone
from handlers.reminders import send_reminder
from keyboards.inline import get_time_of_day_kb_H, get_time_of_day_kb, menu_kb, set_time_inline_kb, timezones_kb
from services.functions import convert_time_to_utc, generate_caption_choosing, generate_menu_caption, get_selected_timezone, start_user
from services.sheduler import add_reminder, remove_reminder
from services.variables import timezones

choose_time_router = Router()

@choose_time_router.callback_query(lambda c: c.data == "set_timezone")
async def set_timezone(call: CallbackQuery):
    await call.message.edit_caption(
        caption='Выбери свой часовой пояс:',
        reply_markup=timezones_kb(get_selected_timezone(call.from_user.id))
    )

    await call.answer()

@choose_time_router.callback_query(lambda c: c.data == "set_time")
async def set_time(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=set_time_inline_kb())

    await call.answer()

@choose_time_router.callback_query(lambda c: c.data == "del")
async def choose_time_of_ddelay_H(call: CallbackQuery):
    user_id = call.from_user.id

    await remove_reminder(user_id)    
    del_time(user_id)
    await call.message.edit_caption(
        caption=generate_menu_caption(user_id),
        reply_markup=menu_kb(user_id)
        )

    await call.answer('Уведомления были очищены')

@choose_time_router.callback_query(lambda c: c.data.startswith('timezone_'))
async def timezone_call(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    c_data = call.data.split('_')
    timezone_id = int(c_data[1])

    save_timezone(call.from_user.id, timezone_id)

    if get_first_time_save(call.from_user.id)[0] =='not yet':
        text=generate_caption_choosing('morning', 'часы')
        rm=get_time_of_day_kb_H('morning')
    else:
        await start_user(user_id, bot)
        text=generate_menu_caption(user_id)
        rm=menu_kb(user_id)

    await call.message.edit_caption(
        caption=text, 
        reply_markup=rm
    )

    await call.answer(f'Установлен часовой пояс {timezones[timezone_id-2][1]} ({timezones[timezone_id-2][2]})')

@choose_time_router.callback_query(lambda c: c.data in ['morning', 'evening'])
async def choose_time_of_day_H(call: CallbackQuery):
    await call.message.edit_caption(
        caption=generate_caption_choosing(call.data, 'часы'),
        reply_markup=get_time_of_day_kb_H(call.data)
    )

    await call.answer()

@choose_time_router.callback_query(lambda c: c.data.startswith('time_H'))
async def choose_time_of_day(call: CallbackQuery):
    c_data = call.data.split('_')
    time_period = c_data[2]
    time_H = c_data[3]

    await call.message.edit_caption(
        caption=generate_caption_choosing(call.data, 'минуты'),
        reply_markup=get_time_of_day_kb(time_period, time_H)
    )

    await call.answer()

@choose_time_router.callback_query(lambda c: c.data.startswith('fulltime_'))
async def fulltime(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id

    c_data = call.data.split('_')
    time_period = c_data[1]
    time_H = c_data[2]
    time_M = c_data[3]

    time_To = time_H+':'+time_M

    mesag = ''
    if get_first_time_save(user_id)[0] == 'not yet':
        mesag = 'choosing'
        have_first_time_save='not yet'
    elif get_first_time_save(user_id)[0] in ['morning', 'evening']:
        have_first_time_save='morning/evening'
    else:
        have_first_time_save='get all'
    
    job_id=str(user_id)+'_'+time_period
    utc_time = convert_time_to_utc(time_To, user_id)
    save_reminder(user_id, time_period, time_To, have_first_time_save) 
    await add_reminder(send_reminder, user_id, job_id, utc_time, bot)

    if mesag == 'choosing':
        sending_time_period_to_kb = 'morning' if time_period == 'evening' else 'evening'
        text = generate_caption_choosing(sending_time_period_to_kb, 'часы')
        rm=get_time_of_day_kb_H(sending_time_period_to_kb)
    else:
        text = generate_menu_caption(user_id)
        rm=menu_kb(user_id)
    await call.message.edit_caption(
        caption=text,
        reply_markup=rm
    )

    await call.answer(f'Напоминание установлено на {time_To}')