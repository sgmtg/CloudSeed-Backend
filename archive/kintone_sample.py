from flask import Flask, request
import requests
from pyntone import ApiTokenAuth, KintoneRestAPIClient

app = Flask(__name__)
# Kintoneの設定
DOMAIN = ""
KEYWORD_API_TOKEN = ""
KEYWORD_APP_ID = 4
@app.route('/add_keyword', methods=['GET'])
def add_keyword():
    keyword = request.form.get('keyword')
    
    # Kintoneに接続するクライアントを作成
    auth = ApiTokenAuth(api_token=KEYWORD_API_TOKEN)
    client = KintoneRestAPIClient(DOMAIN, auth=auth)

    res = client.record.get_record(KEYWORD_APP_ID, 1)
    print(res)
    return res
    
if __name__ == '__main__':
    app.run()