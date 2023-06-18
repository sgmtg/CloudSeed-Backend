from flask import Flask, jsonify, request, make_response, send_file
import create_wordcloud
from flask_cors import CORS, cross_origin
from io import BytesIO
import os

app = Flask(__name__)
CORS(app)

# ルートパスへのリクエストを処理する関数
@app.route("/", methods=["GET", "POST", "OPTIONS"])
def lambda_handler(event=None, context=None):
    return "hello!"


# /word-cloud パスへのリクエストを処理する関数
# @cross_origin(origins=["http://localhost:5173"], methods=["POST", "OPTIONS"])
@app.route("/word-cloud", methods=["GET", "POST", "OPTIONS"])
def get_words():
    # POSTリクエストからデータを取得
    # data = request.get_json()
    # kw_list = data.get("kw_list")
    kw_list = ["key", "key2"]

    # ワードクラウドの生成
    # image = create_wordcloud.create_wordcloud(kw_list=kw_list)
    create_wordcloud.create_wordcloud(kw_list=kw_list)
    # 画像をバイナリデータに変換してレスポンスとして返す
    # img_io = BytesIO()
    # image.save(img_io, "JPEG", quality=95)
    # img_io.seek(0)
    return send_file("/tmp/wordcloud.png", mimetype="image/png")


if __name__ == "__main__":
    # アプリケーションを実行する
    app.run(debug=True)
