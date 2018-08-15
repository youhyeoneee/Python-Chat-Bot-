#연습용
import requests
from bs4 import BeautifulSoup
import time
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'exoLanguage=ko; ASP.NET_SessionId=0ifbs1wkqjbe4rveg1qjgivk; __RequestVerificationToken=OVeDWINnDlFyJ_X_5_Pgj5C43zCJ6H1zwOzaoLdsb9DrOhvunqJ_Xfn_2p890gkeTMoOeCL5zG30ZnUCox2ughY_5RU1; _ga=GA1.2.898370047.1534243951; _gid=GA1.2.612276175.1534243951; EXOInfo=zhnmAGrgFSQvTHiu9mragQ==||sY4kdYa7gqULZQQWwkQPOoD2SJrgYZWhu/3A2YtR0cPcT3e9Tbjz3YX8110nNU3c||ka1CRKB1xkzRIceDFSWgtQ==||Wt3pICPyPcvg8O6m6Eq16A==||4Re2iisS6a4JJh0gXueorv21Usrp6fZFROc2omopB0A=||emgxU+abdR85gw299Ii01Q==||3FdKMeySNGaazzl6onRI9Q==||3FdKMeySNGaazzl6onRI9Q==||',
'Host': 'exo-l.smtown.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

is_First = True
what_time = 3
#for i in all_title:
 #   print(i.get_text())

while(True):
    html = requests.get('https://exo-l.smtown.com/Board/List/10300', headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    all_title = soup.find_all("a", {"class": "boardDetails"})
    if what_time == 5:
        newFirstTitle = "프엑 새글"

    if is_First:
        nowFirstTitle = all_title[0].get_text()
        newFirstTitle = nowFirstTitle
        print(newFirstTitle)
        print(nowFirstTitle)
        is_First = False
    else:
        if nowFirstTitle != newFirstTitle:
            requests.get('https://api.telegram.org/bot602009043:AAHbtbRjehdhptkyxyxoyYbZdhd_RwYwyNw/sendMessage?chat_id=-1001270337756&text=새글떴다요!!제목은"{}"다요'.format(newFirstTitle))
            nowFirstTitle = newFirstTitle
            print(newFirstTitle)
            print(nowFirstTitle)
    time.sleep(3)
    what_time += 1


