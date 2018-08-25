from bs4 import BeautifulSoup
from selenium import webdriver
import CONFIG
import time

ID = CONFIG.ID
PW = CONFIG.PW
TARGET_KEYWORD_LIST = CONFIG.TARGET_KEYWORD_LIST
#찾고자 하는 키워드 추가
keyword = input(">>알림받을 키워드를 입력해주세요 ::")
TARGET_KEYWORD_LIST.append(keyword)

#브라우저 제어
browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

browser.get('https://khu.everytime.kr/370463')

#아이디, 비밀번호 입력
browser.find_element_by_name('userid').send_keys(ID)
browser.find_element_by_name('password').send_keys(PW)

#로그인 버튼 누르기
browser.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

#장터원룸 게시판 들어가기
browser.get('https://khu.everytime.kr/370463')
time.sleep(5)  # 페이지 글 로딩되는거 기다려주기

oldList = []
while True:
    #페이지 소스 얻어오기
    bs4 = BeautifulSoup(browser.page_source, 'lxml')
    print(TARGET_KEYWORD_LIST)
    # 알림 부분 구현
    articles = bs4.find_all('article')
    for article in articles:
        for target_keyword in TARGET_KEYWORD_LIST:
            if target_keyword in article.h2.get_text().strip() and article.h2.get_text().strip() not in oldList:
                print("[알림] :: ",article.h2.get_text().strip())
                oldList.append(article.h2.get_text().strip())


    #새로고침후 원하는 딜레이시간까지 기다리기
    browser.get('https://khu.everytime.kr/370463')
    time.sleep(CONFIG.DELAY)
browser.quit()