import requests
import json
from bs4 import BeautifulSoup
#=== CONFIG VALUE
INIT_STATUS = 0 #맨처음 상태
SELECETED_STATUS = 1# 뭔가를 고른상태

SELECT_BUS = 1 #depth2에서 버스를 고름
SELECT_NAVER = 2
#===
def bus_menu():
    return "외대, 자대, 체대 중에 알고 싶은 정류장 이름을 쓰세요 ~ "
def naver_menu():
    return "몇위부터 몇위까지 궁금한지 숫자를 ,로 구분해 쓰세요"
def naver_keyword_rank(_min:int =1,_max:int=20):
    resultStr =''
    html = requests.get('https://www.naver.com/')
    bs4 = BeautifulSoup(html.text,'lxml')
    keys = bs4.find_all('span',class_='ah_k')
    idx = _min
    for key in keys[_min:_max+1]:
        resultStr += "{}위 : {}\n".format(idx,key.get_text().strip())
        idx+=1
    return resultStr

def bus_info_by_station_name(_name):
    datas = {
    'cmd': 'searchBusStationJson',
    'stationId': ''
    }
    # 228000710외대
    # 228001174 자대
    # 228000703 체대
    stationList = [228000710,228001174,228000703]
    if _name == '외대':
        datas['stationId'] = stationList[0]
    elif _name == '자대':
        datas['stationId'] = stationList[1]
    else:
        datas['stationId'] = stationList[2]


    html = requests.post('http://www.gbis.go.kr/gbis2014/schBusAPI.action',data=datas)
    jsonStr = json.loads(html.text)
    results = jsonStr['result']['busArrivalInfo']
    resultStr = "{}\n정거장 가장빨리 도착하는 버스는 {}번 버스고 {}분 뒤에 도착입니다 ~"
    remainTime = 999
    busNo = ''
    for bus in results:
        try:
            if remainTime > int(bus['predictTime1']):
                busNo = bus['routeName']
                remainTime = int(bus['predictTime1'])
        except:
            pass
    if remainTime == 999:
        return "버스정보없음 ㅂㅂ"
    else:
        return resultStr.format(jsonStr['result']['stationNm'],busNo,remainTime)