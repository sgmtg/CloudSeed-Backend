import requests

base_url = "https://cymntn2bea.execute-api.ap-northeast-3.amazonaws.com/dev"

# ルートパスへのGETリクエスト
response = requests.get(base_url)
print(response.text)

# /word-cloud パスへのPOSTリクエスト
word_cloud_url = base_url + "/word-cloud"
data = {"kw_list": ["SIer", "web系", "IT業界"]}
response = requests.post(word_cloud_url, json=data)
print(response.text)
