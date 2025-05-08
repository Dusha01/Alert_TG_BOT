import asyncio
from aiogram.types import Message, InlineKeyboardMarkup
import asyncio
from typing import Optional


async def send_temp_message(msg: Message, text: str, delete_after: int = 5, parse_mode: Optional[str] = None, reply_markup: Optional[InlineKeyboardMarkup] = None) -> None:
    bot_msg = await msg.answer(text, parse_mode=parse_mode, reply_markup=reply_markup)
    await asyncio.sleep(delete_after)
    try: await msg.delete()
    except Exception as e: print(f"Не удалось удалить сообщение пользователя: {e}")    

    try: await bot_msg.delete()
    except Exception as e: print(f"Не удалось удалить ответ бота: {e}")