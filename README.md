# Create-Lambdaの使い方

基本的に個人用に作成しました。AWSのアカウントを作成していて、AWS CLIがインストール済み、ローカルで```aws configure```が叩ければ使用できると思います。

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

## Zappaのインストールとデプロイ
初期化
```shell
zappa init
```
```zappa_settings.json```を編集する


以下のように
```
{
    "dev": {
        "app_function": "flasktest.app",
        "aws_region": "ap-northeast-3",
        "profile_name": "default",
        "project_name": "create-lambda",
        "runtime": "python3.10",
        "s3_bucket": "zappa-08ktiswxo"
    }
}
```

dev環境構築をlambdaにデプロイ
```shell
zappa deploy dev
```

ローカルのflasktest.pyをいじってupdate
```shell
zappa update
```
