import subprocess
import telegram
import CONFIG
import time

TOKEN = CONFIG.BOT_TOKEN
CHAT_ID = CONFIG.CHAT_ID
BOT = telegram.Bot(token = TOKEN) # bot 선언
update_id_LIST = []


def keyword():
    updates = BOT.getUpdates(chat_id=CHAT_ID)
    print("실행중..")
    for u in updates:
        UPDATE_ID = u.update_id
        if UPDATE_ID not in update_id_LIST:#새로운 메세지 인식
            message = u.channel_post.text
            print(u)
            print(message)
            if '/exo' in message:
                subprocess.call("telegram_bot.py 1", shell=True)

            elif 'exit' in message:
                pass
                #exit(-1)
            else:
                print("pass")
    time.sleep(10)