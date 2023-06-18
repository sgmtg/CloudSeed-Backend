import os
import requests
from dotenv import load_dotenv
import json


def get_keyword(id):
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    domain = os.getenv("DOMAIN")
    keyword_app_id = os.getenv("KEYWORD_APP_ID")
    keyword_api_token = os.getenv("KEYWORD_API_TOKEN")
    url = f"{domain}/k/v1/record.json?app={keyword_app_id}&id={id}"

    # APIトークンをヘッダーに設定
    headers = {
        "X-Cybozu-API-Token": keyword_api_token
    }

    # GETリクエストを送信
    response = requests.get(url, headers=headers)

    # レスポンスをJSONとして解析し、レコード部分を返す
    records = json.loads(response.text)["record"]
    return records


def post_keyword(records):
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    domain = os.getenv("DOMAIN")
    keyword_app_id = os.getenv("KEYWORD_APP_ID")
    keyword_api_token = os.getenv("KEYWORD_API_TOKEN")
    url = f"{domain}/k/v1/records.json"

    # APIトークンをヘッダーに設定
    headers = {
        "X-Cybozu-API-Token": keyword_api_token,
        "Content-Type": "application/json"
    }

    body = {
        "app": keyword_app_id,
        "records": records
    }
    body_json = json.dumps(body)
    response = requests.post(url, headers=headers, data=body_json)
    return response


