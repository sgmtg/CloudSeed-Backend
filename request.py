import requests

base_url = "http://127.0.0.1:5000"

# ルートパスへのGETリクエスト
response = requests.get(base_url)
print(response.text)

# /word-cloud パスへのPOSTリクエスト
word_cloud_url = base_url + "/add_user"
response = requests.post(word_cloud_url)
print(response.text)
