from dotenv import load_dotenv
import os # 운영체제 다루는 라이브러리

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

URL = 'https://api.telegram.org/bot'

print(f'{URL}{TOKEN}/getME')