import telegram

#채널에 메세지 보내기
my_token ='602009043:AAHbtbRjehdhptkyxyxoyYbZdhd_RwYwyNw'
bot = telegram.Bot(token = my_token)
bot.sendMessage(chat_id = '@dasom1', text="저는 봇입니다.")