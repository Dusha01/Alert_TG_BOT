from aiogram.types import FSInputFile, Message
import os

from BOT.core.prometheus import PrometheusClient
from BOT.core.graphing import create_metric_plot
from config.setting import Setting

async def metrics_handler(message: Message):

    user_id = message.from_user.id

    if user_id == int(Setting.USER_ID_1) or user_id == int(Setting.USER_ID_2):
        args = message.text.split()[1:]
        
        metric_name = args[0] if args else "node_memory_MemFree_bytes"
        duration = args[1] if len(args) > 1 else "1h"
        
        prom = PrometheusClient(Setting.PROMETHEUS_URL)
        metric_data = prom.get_metric(metric_name, duration)
        plot_file = create_metric_plot(metric_data, metric_name)
        
        photo = FSInputFile(plot_file)
        await message.answer_photo(photo=photo, caption=f"Metric: {metric_name}")
        
        os.remove(plot_file)
    
    else:
        await message.answer("Слабость")