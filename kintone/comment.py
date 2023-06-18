import os
import requests
from dotenv import load_dotenv
import json


def get_comment():
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    domain = os.getenv("DOMAIN")
    comment_app_id = os.getenv("COMMENT_APP_ID")
    comment_api_token = os.getenv("COMMENT_API_TOKEN")
    url = f"{domain}/k/v1/records.json?app={comment_app_id}"

    # APIトークンをヘッダーに設定
    headers = {
        "X-Cybozu-API-Token": comment_api_token
    }

    # GETリクエストを送信
    response = requests.get(url, headers=headers)

    # レスポンスをJSONとして解析し、レコード部分を返す
    records = json.loads(response.text)["records"]
    return records


def post_comment(records):
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    domain = os.getenv("DOMAIN")
    comment_app_id = os.getenv("COMMENT_APP_ID")
    comment_api_token = os.getenv("COMMENT_API_TOKEN")
    url = f"{domain}/k/v1/records.json"

    # APIトークンをヘッダーに設定
    headers = {
        "X-Cybozu-API-Token": comment_api_token,
        "Content-Type": "application/json"
    }

    body = {
        "app": comment_app_id,
        "record": records
        
    }
    body_json = json.dumps(body)
    response = requests.post(url, headers=headers, data=body_json)
    return response


