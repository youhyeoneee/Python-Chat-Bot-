import telegram


my_token ='602009043:AAHbtbRjehdhptkyxyxoyYbZdhd_RwYwyNw'
bot = telegram.Bot(token = my_token)
bot.sendMessage(chat_id = '@dasom1', text="저는 봇입니다.")