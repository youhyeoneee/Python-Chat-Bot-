from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from COMMON import *

#user별로 하기 ~~!~!!~!
#==================================
# 첫번째 뭘 골랐는지
# 1 : 버스
depth1 = 0
depth2 = 0


app = Flask(__name__)
@app.route("/keyboard", methods=["GET"])
def keyboard():
    return jsonify(type="text")

@app.route("/message", methods=["POST"])
def message():
    global depth1,depth2
    data = json.loads(request.data)
    print(data)
    content = data["content"]
    #===
    if depth1 == INIT_STATUS:# 버스기능을 쓴다했고, depth1 상태가 아무것도 없을때
        result ="""
현재 제공가능한 메뉴는
'번역'
'버스'
'네이버실검'
입니다.
*기능을 종료하시려면 'x'를 입력하세요!
        """
        depth1 = SELECETED_STATUS #선택상태로 변경
    elif content =='버스' and depth1 == SELECETED_STATUS and depth2 == INIT_STATUS:#depth1은 선택을 했고, 키워드를 줬는데, 키워드 메뉴를 안뿌림
        result = bus_menu() # 키워드보고 판단
        depth2 = SELECT_BUS
    elif content == '네이버실검' and depth1 == SELECETED_STATUS and depth2 == INIT_STATUS:  # depth1은 선택을 했고, 키워드를 줬는데, 키워드 메뉴를 안뿌림
        result = naver_menu()  # 키워드보고 판단
        depth2 = SELECT_NAVER
    elif content == '번역' and depth1 == SELECETED_STATUS and depth2 == INIT_STATUS:  # depth1은 선택을 했고, 키워드를 줬는데, 키워드 메뉴를 안뿌림
        result = trans_menu()
        depth2 = SELECT_TRANS

    #======================================================================================================================================
    elif depth1 == SELECETED_STATUS and depth2 == SELECT_BUS: # 메뉴줘서 키워드 입력후 -> 버스를 선택한 상태
        if content != 'x':
            result = bus_info_by_station_name(content)
        else:
            result = "버스 기능이 종료되었습니다."
            depth1 = INIT_STATUS
            depth2 = INIT_STATUS
    elif depth1 == SELECETED_STATUS and depth2 == SELECT_NAVER: #depth1 은 종류고, depth2는 입력받았는지여부야
        if content != 'x':
            min, max = content.split(',')
            result = naver_keyword_rank(int(min), int(max))
        else:
            result = "네이버실검 기능이 종료되었습니다."
            depth1 = INIT_STATUS
            depth2 = INIT_STATUS
    elif depth1 == SELECETED_STATUS and depth2 == SELECT_TRANS:
        if content != 'x':
            result = transtlate(content)
        else:
            result = "번역이 종료되었습니다."
            depth1 = INIT_STATUS
            depth2 = INIT_STATUS
    else:
        result='고르라는것만 골라라 ㅡㅡ'
        depth1 = INIT_STATUS
        depth2 = INIT_STATUS
    #===
    text = result
    response = {
        "message": {
            "text": text
        }
    }
    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888)
    #ngrok http 8888 --region ap