# Create-Lambdaの使い方
まず初めに！このプロジェクトはプロジェクト主が頑張ってGitのインストールからプロジェクトの立ち上げまで全部一人でやってくれた最高のレポジトリになります。★を付けてあげてください。上のstarってやつ★

本プロジェクトはローカルでの実行を想定しております。Zappaやawsがどーのこーの描いてありますが、デプロイは成功していないのでご注意ください。

下に実行手順を示します。あ、様々な.envファイルが必要です。今回必要になったのは下のようになりました。プロジェクト直下に作ってください。

```shell
DOMAIN = ""
KEYWORD_API_TOKEN = ""
KEYWORD_APP_ID = ""
FIGDATA_APP_TOKEN = ""
FIGDATA_APP_ID = ""
USERDATA_APP_TOKEN = ""
USERDATA_APP_ID = ""
COMMENT_API_TOKEN = ""
COMMENT_APP_ID = ""
```

## 環境構築
新しい環境の作成
```shell
python -m venv development
```

Activate
```shell
.\development\Scripts\activate
```

パッケージのインストール
```shell
pip install -r requirements.txt
```

## AWS configureの確認
```shell
aws configure
```

## flaskのテスト
```shell
flask --debug run
```

もしくは、

```shell
python /flasktest.py
```

で動かしてください。

この後、フロントエンドでのサーバー立ち上げが必要です。以下はNodeがインストールされている状況を想定しています。

# Frontendの立ち上げ

[CloudSeed-Frontend](https://github.com/Melonps/CloudSeed-Frontend)にアクセスし、本プロジェクトは別のプロジェクトディレクトリで、

```shell
git clone https://github.com/Melonps/CloudSeed-Frontend.git
```

で、レポジトリをダウンロードしてもらって、フロントエンドのAPI_KEYを入力してください。詳細は向こうのレポジトリで。

```shell
cd CloudSeed-Frontend
```

で、ディレクトリ移動

```shell
npm install
```

で、モジュールをインストールしてください。

```shell
npm start
```

というコマンドをうち、http://localhost:5173 にアクセスすると、プロジェクトが立ち上がります。
