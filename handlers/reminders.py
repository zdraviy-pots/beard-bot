from aiogram import Router
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ContentType
from aiogram.filters import StateFilter

from db_handlers.main_functions import get_all_user_chat_ids, get_total_users, get_users_with_get_all_status
from filters.is_admin import IsAdmin
from config import admins
from keyboards.inline import get_serum_inline_kb, menu_kb, to_menu_kb
from services.states import NotifyState

reminders_router = Router()

async def send_reminder(user_id, bot: Bot):
    await bot.send_message(user_id, text="Пора принять наш коктейль для роста волос!", reply_markup=get_serum_inline_kb(user_id))

@reminders_router.callback_query(lambda c: c.data.startswith('used_'))
async def serum_used(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

@reminders_router.callback_query(lambda c: c.data == "send_notify", IsAdmin(admins))
async def send_notify(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Напишите сообщение для рассылки всем пользователям.\nДопустимые форматы:\n- сообщение\n- фото\n- голосовое\n- кружок\n- видео\n- документ\n- аудио", reply_markup=to_menu_kb())
    await state.set_state(NotifyState.waiting_for_message)
    await call.answer()

@reminders_router.callback_query(lambda c: c.data == "show_stat", IsAdmin(admins))
async def send_notify(call: CallbackQuery):
    user_id = call.from_user.id
    total_users = get_total_users()
    get_all_users = get_users_with_get_all_status()

    text = (
        f"📊 <b>Статистика</b>\n\n"
        f"👥 Общее количество пользователей: <b>{total_users}</b>\n"
        f"📨 Активные пользователи: <b>{get_all_users}</b>"
    )

    await call.message.edit_caption(
        caption=text,
        reply_markup=to_menu_kb(),
        parse_mode='HTML'
        )

    await call.answer()

@reminders_router.message(IsAdmin(admins), StateFilter(NotifyState.waiting_for_message))
async def forward_message_to_all(message: Message, state: FSMContext, bot: Bot):
    all_chat_ids = get_all_user_chat_ids()

    if message.content_type == ContentType.TEXT:
        text = message.text
        for chat_id in all_chat_ids:
            try:
                await bot.send_message(chat_id, text, reply_markup=to_menu_kb())
            except Exception as e:
                print(f"Не удалось отправить текст в чат {chat_id}: {e}")
    elif message.content_type == ContentType.PHOTO:
        photo = message.photo[-1]
        caption = message.caption
        for chat_id in all_chat_ids:
            try:
                await bot.send_photo(chat_id, photo.file_id, caption=caption, reply_markup=to_menu_kb())
            except Exception as e:
                print(f"Не удалось отправить фото в чат {chat_id}: {e}")
    elif message.content_type == ContentType.VOICE:
        voice = message.voice
        caption = message.caption
        for chat_id in all_chat_ids:
            try:
                await bot.send_voice(chat_id, voice.file_id, caption=caption, reply_markup=to_menu_kb())
            except Exception as e:
                print(f"Не удалось отправить голосовое сообщение в чат {chat_id}: {e}")
    elif message.content_type == ContentType.VIDEO_NOTE:
        video = message.video_note
        for chat_id in all_chat_ids:
            try:
                await bot.send_video_note(chat_id, video.file_id, reply_markup=to_menu_kb())
            except Exception as e:
                print(f"Не удалось отправить кружок в чат {chat_id}: {e}")
    elif message.content_type == ContentType.VIDEO:
        video = message.video
        caption = message.caption
        for chat_id in all_chat_ids:
            try:
                await bot.send_video(chat_id, video.file_id, caption=caption, reply_markup=to_menu_kb())
            except Exception as e:
                print(f"Не удалось отправить видео в чат {chat_id}: {e}")
    elif message.content_type == ContentType.DOCUMENT:
        document = message.document
        caption = message.caption
        for chat_id in all_chat_ids:
            try:
                await bot.send_document(chat_id, document.file_id, caption=caption, reply_markup=to_menu_kb())
            except Exception as e:
                print(f"Не удалось отправить документ в чат {chat_id}: {e}")
    elif message.content_type == ContentType.AUDIO:
        audio = message.audio
        caption = message.caption
        for chat_id in all_chat_ids:
            try:
                await bot.send_audio(chat_id, audio.file_id, caption=caption, reply_markup=to_menu_kb())
            except Exception as e:
                print(f"Не удалось отправить аудио в чат {chat_id}: {e}")

    await message.answer("Сообщение было отправлено всем пользователям!", reply_markup=to_menu_kb())
    await state.clear()