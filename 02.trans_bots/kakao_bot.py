from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from googletrans import Translator
app = Flask(__name__)

@app.route("/keyboard")
def keyboard():
    return jsonify(type="text")

@app.route("/message", methods=["POST"])
def message():
    data = json.loads(request.data)
    print(data)
    content = data["content"]
    translator = Translator() #Create object of Translator.
    translated = translator.translate(content, dest="en", src="ko")
    response = {
        "message": {
            "text": translated.text
        }
    }
    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    #ngrok http 8888 --region ap