from flask import Flask, jsonify, request, make_response, send_file
import create_wordcloud
from io import BytesIO
import os

app = Flask(__name__)


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
    # image = create_wordcloud.create_wordcloud(kw_list=kw_list)
    create_wordcloud.create_wordcloud(kw_list=kw_list)
    # 画像をバイナリデータに変換してレスポンスとして返す
    # img_io = BytesIO()
    # image.save(img_io, "JPEG", quality=95)
    # img_io.seek(0)
    return send_file("/tmp/images/wordcloud.png", mimetype="image/jpeg")


if __name__ == "__main__":
    # アプリケーションを実行する
    app.run()
