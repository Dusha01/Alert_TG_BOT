from aiogram.types import InputFile, Message
from aiogram.types import Message
import os

from BOT.core.prometheus import PrometheusClient
from BOT.core.graphing import create_metric_plot
from config.setting import Setting

async def metrics_handler(message: Message):
    args = message.text.split()[1:]  # Получаем аргументы после команды
    
    metric_name = args[0] if args else "node_memory_MemFree_bytes"
    duration = args[1] if len(args) > 1 else "1h"
    
    prom = PrometheusClient(Setting.PROMETHEUS_URL)  # Или из настроек
    metric_data = prom.get_metric(metric_name, duration)
    plot_file = create_metric_plot(metric_data, metric_name)
    
    # Используем InputFile для отправки файла
    photo = InputFile(plot_file)
    await message.answer_photo(photo=photo, caption=f"Metric: {metric_name}")
    
    os.remove(plot_file)