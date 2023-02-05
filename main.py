import asyncio
from utils import y_color
import requests as requests
from pyrogram import Client
from config.config import APP_ID, APP_HASH, BOLTALKA_CHAT_ID, BOT_TOKEN, CHANNEL_FOR_REPORT
from utils.db_api_sqlite import BotDB
from datetime import datetime
from utils import clear

now = datetime.now()
time_now = now.strftime("%m:%d:%Y, %H:%M:%S")

BotDB = BotDB('boltalka_db')

api_id = APP_ID
api_hash = APP_HASH

slovar = ['куплю', 'ищу', 'хакер', 'анкета', 'продает', 'занимается', 'заплачу',
          'реклама', 'оплачу', 'рекламщик', 'взлом', 'покупал']


async def send_msg_tg(text):
    token = BOT_TOKEN
    chat_id = CHANNEL_FOR_REPORT
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


async def main():
    while True:
        async with Client("my_account", api_id, api_hash) as app:
            count = 0
            async for message in app.search_messages(BOLTALKA_CHAT_ID, limit=50):
                sms = message.text
                mess = f"{y_color(f'{message.from_user.first_name}')}: {sms} [{count + 1}]"
                count += 1
                print(mess)
                if not BotDB.message_exists(message.id):
                    BotDB.add_message(message.id)
                    for keyword in slovar:
                        if keyword in str(sms):
                            try:
                                await send_msg_tg(
                                    f'👩‍✈ [{time_now}] Бос я работаю\nНайдено уникальное сообщение:\n'
                                    f'')
                                await message.forward('sceoor30')
                            except:
                                continue
            print('*' * 130)
            await asyncio.sleep(180)

if __name__ == "__main__":
    try:
        asyncio.run(main())
        clear()
    except Exception as err:
        try:
            print(err)
        except:
            print(err)
