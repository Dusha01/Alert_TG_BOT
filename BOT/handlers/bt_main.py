from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config.setting import Setting

router = Router()

@router.message(Command(commands=['start']))
async def go_main_bt(msg: Message):

    user_id=msg.from_user.id
    if user_id == int(Setting.USER_ID_1) or user_id == int(Setting.USER_ID_2):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="CPU", callback_data="CPU_metrics"),
                InlineKeyboardButton(text="RAM", callback_data="RAM_metrics"),
                InlineKeyboardButton(text="SWAP", callback_data="SWAP_metrics")
            ],
            [
                InlineKeyboardButton(text="DISK", callback_data="DISK_metrics"),
                InlineKeyboardButton(text="LOAD", callback_data="LOAD_metrics"),
                InlineKeyboardButton(text="UPTIME", callback_data="UPTIME_metrics")
            ],
        ])
        
        await msg.answer("Main menu:", reply_markup=keyboard)
    
    else:
        await msg.answer("Послан")