import os
from dotenv import load_dotenv

# načteme .env jen jednou při importu
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FMP_API_KEY = os.getenv("FMP_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if OPENAI_API_KEY is None:
    raise RuntimeError("Missing OPENAI_API_KEY in .env")