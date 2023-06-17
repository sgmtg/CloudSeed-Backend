import requests
import json

import requests
import json

def get_kintone_records(DOMAIN, KEYWORD_APP_ID, KEYWORD_API_TOKEN):
    # kintoneのエンドポイントURLを作成
    id = 1
    url = f"https://{DOMAIN}.cybozu.com/k/v1/records.json?app={KEYWORD_APP_ID}&id={id}"

    # APIトークンをヘッダーに設定
    headers = {
        "X-Cybozu-API-Token": KEYWORD_API_TOKEN
    }


    # GETリクエストを送信
    response = requests.get(url, headers=headers)


    # レスポンスをJSONとして解析し、レコード部分を返す
    response = json.loads(response.text)["records"]
    return response

def post_kintone_record(DOMAIN, KEYWORD_APP_ID, KEYWORD_API_TOKEN):
    url = f"https://{DOMAIN}.cybozu.com/k/v1/records.json"

    # APIトークンをヘッダーに設定
    headers = {
        "X-Cybozu-API-Token": KEYWORD_API_TOKEN,
        "Content-Type": "application/json"
    }

    body = {
        "app": KEYWORD_APP_ID,
        "records":[
            {
                "evaluation":{
                    "value":"星２"
                },
                "keyword":{
                    "value":"テニス"
                },
                "figdata_id":{
                    "value":"2"
                }
            }
        ]
    }
    body_json = json.dumps(body)
    response = requests.post(url, headers=headers, data=body_json)
    return response

if __name__ == "__main__":
    # テスト用のkintoneのドメイン、アプリID、APIトークン
    DOMAIN = "bv9iwgn82tj7"
    KEYWORD_API_TOKEN = "sZZ3h8ZzIEiKYwT6wAaO59ZyLdSF9nq4COLI2Rfm"
    KEYWORD_APP_ID = 4

    # kintoneからデータを取得
    res = get_kintone_records(DOMAIN, KEYWORD_APP_ID, KEYWORD_API_TOKEN)
    # res = post_kintone_record(DOMAIN, KEYWORD_APP_ID, KEYWORD_API_TOKEN)

    print(res)
    # # 取得したデータを表示
    # for record in records:
    #     print(record)
