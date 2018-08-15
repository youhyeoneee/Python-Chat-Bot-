import requests
from bs4 import BeautifulSoup
#requests를 통해서 웹에 있는 소스 가져오기
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

html = requests.get('https://exo-l.smtown.com/Board/List/10300',headers =headers)
soup = BeautifulSoup(html.text, 'html.parser')
print(soup.prettify())

