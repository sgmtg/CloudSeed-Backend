from flask import Flask, jsonify, request
import create_wordcloud
from dotenv import load_dotenv
import os
from pyntone import ApiTokenAuth, KintoneRestAPIClient
import json
import requests

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
@app.route("/word-cloud", methods=["GET", "POST"])
def get_words():
    # POSTリクエストからデータを取得
    data = request.get_json()
    kw_list = data.get("kw_list")
    # ワードクラウドの生成
    image = create_wordcloud.create_wordcloud(kw_list=kw_list)
    print(type(image))
    # レスポンスをJSON形式で返す
    return jsonify({"message": "Word cloud created!"}), 200


if __name__ == "__main__":
    # アプリケーションを実行する
    app.run()
