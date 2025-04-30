from dotenv import load_dotenv
import os

load_dotenv()

class Setting:
    BOT_TOKEN=os.getenv("BOT_TOKEN_")
    PROMETHEUS_URL=os.getenv("PROMETHEUS_URL_")
    USER_ID_1=os.getenv("USER_ID_1_")
    USER_ID_2=os.getenv("USER_ID_2_")