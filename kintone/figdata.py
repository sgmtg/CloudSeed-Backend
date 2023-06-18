import os
import requests
from dotenv import load_dotenv
import json


def get_figdata(id):
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    domain = os.getenv("DOMAIN")
    
    figdata_app_id = os.getenv("FIGDATA_APP_ID")
    
    figdata_api_token = os.getenv("FIGDATA_API_TOKEN")
    url = f"{domain}/k/v1/records.json?app={figdata_app_id}&id={id}"

    # APIトークンをヘッダーに設定
    headers = {
        "X-Cybozu-API-Token": figdata_api_token
    }

    # GETリクエストを送信
    response = requests.get(url, headers=headers)
    
    print(response.text)
    # レスポンスをJSONとして解析し、レコード部分を返す
    records = json.loads(response.text)["records"]
    return records


def post_figdata(records):
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    domain = os.getenv("DOMAIN")
    figdata_app_id = os.getenv("FIGDATA_APP_ID")
    figdata_api_token = os.getenv("FIGDATA_API_TOKEN")
    url = f"{domain}/k/v1/records.json"

    # APIトークンをヘッダーに設定
    headers = {
        "X-Cybozu-API-Token": figdata_api_token,
        "Content-Type": "application/json"
    }

    body = {
        "app": figdata_app_id,
        "records": records
    }
    body_json = json.dumps(body)
    response = requests.post(url, headers=headers, data=body_json)
    return response


