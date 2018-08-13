import telegram #텔레그램 모듈 임포트


TOKEN = '602009043:AAHbtbRjehdhptkyxyxoyYbZdhd_RwYwyNw' #토큰을 변수에 저장

BOT = telegram.Bot(token= TOKEN) # bot 선언

updates = BOT.getUpdates() #업데이트 내역 받아옴

for u in updates:
    print(u.message) #업데이트 내역 중 메시지 출력
    print(u.message.text)
    print(u)

chat_id = BOT.getUpdates()[-1].message.chat.id #봇이 메세지 보내기
BOT.sendMessage(chat_id = chat_id, text="저는 봇입니다.")