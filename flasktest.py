from flask import Flask, jsonify, request
import create_wordcloud
import kintone.keyword as kk
import kintone.figdata as kf
from dotenv import load_dotenv
import os
from dotenv import load_dotenv



load_dotenv()
app = Flask(__name__)

DOMAIN = os.getenv("DOMAIN")
KEYWORD_API_TOKEN = os.getenv("KEYWORD_API_TOKEN")
KEYWORD_APP_ID = os.getenv("KEYWORD_APP_ID")
FIGDATA_APP_TOKEN = os.getenv("FIGDATA_APP_TOKEN")
FIGDATA_APP_ID = os.getenv("FIGDATA_APP_ID")
USERDATA_APP_TOKEN = os.getenv("USERDATA_APP_TOKEN")
USERDATA_APP_ID = os.getenv("USERDATA_APP_ID")


# ルートパスへのリクエストを処理する関数
@app.route("/", methods=["GET", "POST"])
def lambda_handler(event=None, context=None):
    return "hello!"


# /word-cloud パスへのリクエストを処理する関数
@app.route("/word-cloud", methods=["POST"])
def post_wordcloud():
    # POSTリクエストからデータを取得
    data = request.get_json()
    kw_list = data.get("kw_list")
    # ワードクラウドの生成
    image = create_wordcloud.create_wordcloud(kw_list=kw_list)
    # レスポンスをJSON形式で返す
    return jsonify({"message": "Word cloud created!"}), 200


@app.route("/kintone/keyword/<id>", methods=["GET"])
def get_keyword(id):
    records = kk.get_keyword(id)
    return jsonify({"record": records}), 200

@app.route("/kintone/keyword", methods=["POST"])
def post_keyword():
    data = request.get_json()
    records = data.get("records")

    response = kk.post_keyword(records)
    return jsonify({"message": "Created", "response": response.text}), 201


@app.route("/kintone/figdata/<id>", methods=["GET"])
def get_figdata(id):
    records = kf.get_figdata(id)
    return jsonify({"record": records}), 200

@app.route("/kintone/figdata", methods=["POST"])
def post_figdata():
    data = request.get_json()
    records = data.get("records")

    response = kf.post_figdata(records)
    return jsonify({"message": "Created", "response": response.text}), 201

if __name__ == "__main__":
    # アプリケーションを実行する
    app.run()
