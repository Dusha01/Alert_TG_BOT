from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config.setting import Setting

router = Router()



@router.message(Command(commands=['grafana']))
async def send_url_grafana(msg: Message):
    user_id = msg.from_user.id
    if user_id == int(Setting.USER_ID_1) or user_id == int(Setting.USER_ID_2):
        await msg.answer(f"{Setting.GRAFANA_URL}")
    else:
        await msg.answer("Послан")



@router.message(Command(commands=['Prometheus']))
async def send_url_prometheus(msg: Message):
    user_id = msg.from_user.id
    if user_id == int(Setting.USER_ID_1) or user_id == int(Setting.USER_ID_2):
        await msg.answer(f"{Setting.PROMETHEUS_URL}")
    else:
        await msg.answer("Послан")