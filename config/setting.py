from dotenv import load_dotenv
import os

load_dotenv()

class Setting:
    BOT_TOKEN=os.getenv("BOT_TOKEN_")
    PROMETHEUS_URL=os.getenv("PROMETHEUS_URL_")