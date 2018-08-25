import telegram
import CONFIG
import requests
import time
TOKEN = CONFIG.BOT_TOKEN
CHAT_ID = CONFIG.CHAT_ID
TARGET_KEYWORD_LIST = CONFIG.TARGET_KEYWORD_LIST
update_id_LIST = []
BOT_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}".format(TOKEN, CHAT_ID)
BOT = telegram.Bot(token = TOKEN) # bot 선언


def Add_keyword():
    keyword = requests.get(BOT_URL +">>알림받을 키워드를 입력해주세요 ::")
    TARGET_KEYWORD_LIST.append(keyword)
while(True):
    updates = BOT.getUpdates(chat_id=CHAT_ID)
    for u in updates:
        UPDATE_ID = u.update_id
        if UPDATE_ID not in update_id_LIST:
            message = u.channel_post.text
            print(u)
            print(message)
            if 'A:' in message :
                keyword = message.split(':')[1]
                if keyword not in TARGET_KEYWORD_LIST:
                    TARGET_KEYWORD_LIST.append(keyword)
                    requests.get(BOT_URL + "&text=새로운 키워드가 추가되었습니다.\n현재 키워드는 {} 입니다.".format(TARGET_KEYWORD_LIST))
                else:
                    requests.get(BOT_URL + "&text=이미 존재하는 키워드입니다.")

            elif 'D:' in message:
                keyword = message.split(':')[1]
                if keyword in TARGET_KEYWORD_LIST:
                    TARGET_KEYWORD_LIST.remove(keyword)
                    requests.get(BOT_URL + "&text=키워드가 삭제되었습니다.\n현재 키워드는 {} 입니다.".format(TARGET_KEYWORD_LIST))
                else:
                    requests.get(BOT_URL + "&text=키워드가 존재하지 않습니다.")
            elif message == 'X':
                exit(-1)
            else:
                requests.get(BOT_URL + "&text=알 수 없는 명령어입니다.")
            update_id_LIST.append(UPDATE_ID)
        else:
            pass
    print(update_id_LIST)
    time.sleep(10)


