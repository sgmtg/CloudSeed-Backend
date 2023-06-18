import create_wordcloud
import kintone.keyword as kk
import kintone.figdata as kf
import kintone.comment as cm
from flask import Flask, jsonify, request, send_file
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
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
    kw_list = request.data.decode()
    kw_list = kw_list[12:-2]
    kw_list = [item.strip('"') for item in kw_list.split(',')]
    # kw_list = ["プログラミング", "IT業界"]

    # ワードクラウドの生成
    create_wordcloud.create_wordcloud(kw_list=kw_list)
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
