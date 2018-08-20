import requests
import json

datas = {
'cmd': 'searchBusStationJson',
'stationId': ''
}
# 228000710외대
# 228001174 자대
# 228000703 체대
stationList = [228000710,228001174,228000703]
print("1.외대")
print("2.자대")
print("3.체대")
inputNum=int( input("알고싶은거입력:"))-1
datas['stationId'] = stationList[inputNum]

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
    print("버스정보없음 ㅂㅂ")
else:
    print(resultStr.format(jsonStr['result']['stationNm'],busNo,remainTime))