from bs4 import BeautifulSoup
from selenium import webdriver
import CONFIG
import time
import requests
import telegram

#변수
ID = CONFIG.ID
PW = CONFIG.PW
TARGET_KEYWORD_LIST = CONFIG.TARGET_KEYWORD_LIST
TARGET_KEYWORD = CONFIG.TARGET_KEYWORD
oldList = []
linkList = []
#봇 구현
TOKEN = CONFIG.BOT_TOKEN
CHAT_ID = CONFIG.CHAT_ID
BOT_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}".format(TOKEN, CHAT_ID)
BOT = telegram.Bot(token = TOKEN) # bot 선언

#찾고자 하는 키워드 추가 함수
#def Add_keyword():
#    keyword = input(">>알림받을 키워드를 입력해주세요 ::")
#    TARGET_KEYWORD_LIST.append(keyword)

if __name__ == '__main__':
    #브라우저 제어
    browser = webdriver.Chrome('./chromedriver')
    #browser.maximize_window()

    browser.get('https://khu.everytime.kr')
    browser.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/form/a[1]').click()
    #아이디, 비밀번호 입력
    browser.find_element_by_name('userid').send_keys(ID)
    browser.find_element_by_name('password').send_keys(PW)

    #로그인 버튼 누르기
    browser.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

    # 검색하기
    browser.find_element_by_xpath('//*[@id="container"]/div[3]/form/input').send_keys(TARGET_KEYWORD + '\n')
    time.sleep(5)  # 페이지 글 로딩되는거 기다려주기

    while True:
        bs4 = BeautifulSoup(browser.page_source, 'lxml')
        #print(TARGET_KEYWORD_LIST)
        # 알림 부분 구현
        articles = bs4.find_all('article')
        for article in articles:
            link = article.find('a',{'class':'article'})['href']
            print(link)
            if link not in linkList:
                linkList.append(link)
                for target_keyword in TARGET_KEYWORD_LIST:
                    if target_keyword in article.get_text().strip() and article.get_text().strip() not in oldList:
                        if article.find('h2') != None: #제목 있을 때
                            if len(article.p.get_text().strip()) >= 50: #글자수 제한
                                #print("[제목] ::{}".format(article.h2.get_text().strip()))
                                #print("[내용] ::{}".format(article.p.get_text().strip()))
                                requests.get(BOT_URL + '&text=[새 글 알림]\n제목 ::{}\n내용 ::{}\nURL ::{}'.format(article.h2.get_text().strip(),article.p.get_text().strip()[:50]+'[더보기]','https://khu.everytime.kr'+link))
                            else:
                                requests.get(BOT_URL + '&text=[새 글 알림]\n제목 ::{}\n내용 ::{}\nURL ::{}'.format(article.h2.get_text().strip(),article.p.get_text().strip()[:50],'https://khu.everytime.kr'+link))


                        else: #제목 없을 때
                            if len(article.p.get_text().strip()) >= 50: #글자수 제한
                                requests.get(BOT_URL + '&text=[새 글 알림]\n제목 ::없음\n내용 ::{}\nURL ::{}'.format(article.p.get_text().strip()[:50]+'[더보기]','https://khu.everytime.kr'+link))
                            else:
                                requests.get(BOT_URL + ' [새 글 알림]\n제목 ::없음\n내용 ::{}\nURL ::{}'.format(article.p.get_text().strip(),'https://khu.everytime.kr'+link))

                            #print("[제목없음]") #제목 없을 때
                            #print("[내용] ::{}".format(article.p.get_text().strip()))
                oldList.append(article.get_text().strip())
        print(linkList)
        #새로고침후 원하는 딜레이시간까지 기다리기
        browser.get('https://khu.everytime.kr/search/all/{}'.format(target_keyword))
        time.sleep(CONFIG.DELAY)

#test 결과 전체검색창에 글 뜨는데 3분정도 걸림

    browser.quit()