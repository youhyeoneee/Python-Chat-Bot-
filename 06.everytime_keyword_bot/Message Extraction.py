import telegram
import CONFIG

TOKEN = CONFIG.BOT_TOKEN
CHAT_ID = CONFIG.CHAT_ID

BOT_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}".format(TOKEN, CHAT_ID)
BOT = telegram.Bot(token = TOKEN) # bot 선언

updates = BOT.getUpdates(chat_id= CHAT_ID)
for u in updates:
    print(u)
    print(u.channel_post.text)