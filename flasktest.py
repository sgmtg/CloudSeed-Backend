from flask import Flask, jsonify, request, make_response, send_file
import create_wordcloud
from flask_cors import CORS
import os
import kintone.keyword as kk
import kintone.figdata as kf
import kintone.comment as cm
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
CORS(app)

DOMAIN = os.getenv("DOMAIN")
KEYWORD_API_TOKEN = os.getenv("KEYWORD_API_TOKEN")
KEYWORD_APP_ID = os.getenv("KEYWORD_APP_ID")
FIGDATA_APP_TOKEN = os.getenv("FIGDATA_APP_TOKEN")
FIGDATA_APP_ID = os.getenv("FIGDATA_APP_ID")
USERDATA_APP_TOKEN = os.getenv("USERDATA_APP_TOKEN")
USERDATA_APP_ID = os.getenv("USERDATA_APP_ID")


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

@app.route("/kintone/comment", methods=["GET"])
def get_comment():
    response = cm.get_comment()
    return jsonify({"message": "Created", "response": response}), 201


@app.route("/kintone/comment", methods=["POST"])
def post_comment():
    data = request.get_json()
    records = data.get("records")

    response = cm.post_comment(records)
    return jsonify({"message": "Created", "response": response.text}), 201




if __name__ == "__main__":
    # アプリケーションを実行する
    app.run(debug=True)
