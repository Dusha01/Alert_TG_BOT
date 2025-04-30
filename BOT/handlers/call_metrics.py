from aiogram.types import CallbackQuery
from aiogram import Router
from aiogram.types import FSInputFile
import os

from BOT.core.prometheus import PrometheusClient
from BOT.core.graphing import create_metric_plot
from config.setting import Setting


router = Router()


async def handle_metric_callback(call: CallbackQuery, metric_name: str):
    user_id = call.from_user.id
    
    if user_id == int(Setting.USER_ID_1) or user_id == int(Setting.USER_ID_2):
        prom = PrometheusClient(Setting.PROMETHEUS_URL)
        metric_data = prom.get_metric(metric_name, "1h")
        plot_file = create_metric_plot(metric_data, metric_name)
        
        photo = FSInputFile(plot_file)
        await call.message.answer_photo(photo=photo, caption=f"Metric: {metric_name}")
        
        os.remove(plot_file)
        await call.answer()
    else:
        await call.answer("Послан", show_alert=True)


@router.callback_query(lambda c: c.data == 'CPU_metrics')
async def get_cpu(call: CallbackQuery):
    await handle_metric_callback(call, "node_cpu_seconds_total")


@router.callback_query(lambda c: c.data == 'RAM_metrics')
async def get_ram(call: CallbackQuery):
    await handle_metric_callback(call, "node_memory_MemFree_bytes")


@router.callback_query(lambda c: c.data == 'SWAP_metrics')
async def get_swap(call: CallbackQuery):
    await handle_metric_callback(call, "node_memory_SwapFree_bytes")


@router.callback_query(lambda c: c.data == 'DISK_metrics')
async def get_disk(call: CallbackQuery):
    await handle_metric_callback(call, "node_filesystem_avail_bytes")


@router.callback_query(lambda c: c.data == 'LOAD_metrics')
async def get_load(call: CallbackQuery):
    await handle_metric_callback(call, "node_load1")


@router.callback_query(lambda c: c.data == 'UPTIME_metrics')
async def get_uptime(call: CallbackQuery):
    await handle_metric_callback(call, "node_time_seconds")