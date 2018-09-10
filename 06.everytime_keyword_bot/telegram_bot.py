from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import datetime
#====================
import keyword_add_delete
import CONFIG
#키워드 여러개 어케 동시에 검색할수 있을까
#############################################

#변수
ID = CONFIG.ID
PW = CONFIG.PW
TARGET_KEYWORD_LIST = CONFIG.TARGET_KEYWORD_LIST
oldList = []
linkList = []

#봇 구현
TOKEN = CONFIG.BOT_TOKEN
CHAT_ID = CONFIG.CHAT_ID
BOT_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}".format(TOKEN, CHAT_ID)


###################################################

if __name__ == '__main__':
    now = datetime.datetime.now()
    # 브라우저 제어
    browser = webdriver.Chrome('./chromedriver')
    # browser.maximize_window()

    browser.get('https://khu.everytime.kr')
    browser.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/form/a[1]').click()
    # 아이디, 비밀번호 입력
    browser.find_element_by_name('userid').send_keys(ID)
    browser.find_element_by_name('password').send_keys(PW)

    # 로그인 버튼 누르기
    browser.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

    while True:
        print(now)
        #키워드 관리
        keyword_add_delete.keyword()
        for target_keyword in TARGET_KEYWORD_LIST:

            # 검색하기
            browser.find_element_by_xpath('//*[@id="container"]/div[3]/form/input').send_keys(target_keyword + '\n')
            time.sleep(5)  # 페이지 글 로딩되는거 기다려주기

            bs4 = BeautifulSoup(browser.page_source, 'lxml') #페이지 소스 파싱

            # 알림 부분 구현
            articles = bs4.find_all('article')
            for article in articles:
                #시간 비교
                article_time = article.find('time')['title']
                convert_time = datetime.datetime.strptime(article_time, "%Y-%m-%d %H:%M:%S") #type : str -> <class 'datetime.datetime'>
                if convert_time>now: #글 올린 시간이 지금보다 더 최근일때
                    print("@@@최근글::"+article.get_text().strip())
                    link = article.find('a',{'class':'article'})['href']
                    if link not in linkList:
                        linkList.append(link)
                        if target_keyword in article.get_text().strip() and article.get_text().strip() not in oldList:
                            if article.find('h2') != None: #제목 있을 때
                                if len(article.p.get_text().strip()) >= 50: #글자수 제한
                                    requests.get(BOT_URL + '&text=[새 글 알림]\n제목 ::{}\n내용 ::{}\nURL ::{}'.format(article.h2.get_text().strip(),article.p.get_text().strip()[:50]+'[더보기]','https://khu.everytime.kr'+link))
                                else:
                                    requests.get(BOT_URL + '&text=[새 글 알림]\n제목 ::{}\n내용 ::{}\nURL ::{}'.format(article.h2.get_text().strip(),article.p.get_text().strip()[:50],'https://khu.everytime.kr'+link))

                            else: #제목 없을 때
                                if len(article.p.get_text().strip()) >= 50: #글자수 제한
                                    requests.get(BOT_URL + '&text=[새 글 알림]\n제목 ::없음\n내용 ::{}\nURL ::{}'.format(article.p.get_text().strip()[:50]+'[더보기]','https://khu.everytime.kr'+link))
                                else:
                                    requests.get(BOT_URL + '&text=[새 글 알림]\n제목 ::없음\n내용 ::{}\nURL ::{}'.format(article.p.get_text().strip(),'https://khu.everytime.kr'+link))

                    oldList.append(article.get_text().strip())
                else:
                    print("예전글 ::"+article.get_text().strip())
            # 새로고침후 원하는 딜레이시간까지 기다리기
            print(linkList)
            print(oldList)
            browser.get('https://khu.everytime.kr/search/all/{}'.format(target_keyword))
        time.sleep(20)
    browser.quit()
#test 결과 전체검색창에 글 뜨는데 3분정도 걸림

