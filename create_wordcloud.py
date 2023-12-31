import os
import pprint
import time
import urllib.error
import urllib.request
import numpy as np
from collections import Counter
from wordcloud import WordCloud
from pytrends.request import TrendReq
from PIL import Image


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode="wb") as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def create_wordcloud(kw_list):
    WORDCLOUD_FONT_PATH = "./templates/SourceHanSansJP-Regular.otf"
    # wordcloud用の幅
    WORDCLOUD_WIDTH = 1200
    # wordcloud用の高さ
    WORDCLOUD_HEIGHT = 1200
    # wordcloud用の背景色
    WORDCLOUD_BG_COLOR = "white"
    # mask画像のパス
    WORDCLOUD_MASK = "./templates/mask.jpg"
    # フォントサイズの最小値
    WORDCLOUD_MIN_FONT_SIZE = 20
    # フォントサイズの最小値
    WORDCLOUD_MAX_FONT_SIZE = 50
    # カラーマップ
    WORDCLOUD_COLOR_MAP = "winter"
    # wordcloud出力先
    WORDCLOUD_OUTPUT_FILE = "./tmp/wordcloud.png"

    # ---------- 処理開始 ----------

    # Google Trendsのdict
    google_trend_dict = {}

    """
    期間の指定例：
    timeframe='now 1-d' -> 過去1日間（あるいは7-dで指定）
    timeframe='today 1-m' -> 過去1ヶ月間（あるいは3-mで指定）
    timeframe='today 5-y' -> 過去5年間（5-yしか指定できない）
    """
    pytrends = TrendReq(hl="ja-JP", tz=360)
    for keyword in kw_list:
        # Google Trendsのデータを取得する
        pytrends.build_payload(
            [keyword], cat=0, timeframe="today 5-y", geo="JP", gprop=""
        )
        trends = pytrends.related_queries()
        trends_values = trends[keyword]["top"].values.tolist()

        keyword_trends = []
        for value in trends_values:
            item = str(value[0]).replace(keyword, "")  # 関連キーワードのみを出力するので、検索キーワードは消している
            item = item.replace("　", "")
            item = item.replace(" ", "")
            keyword_trends.append(item)

        # 各キーワードごとの関連キーワードの集合を作成する
        google_trend_dict[keyword] = set(keyword_trends)

    # 全てのキーワードの関連キーワードの和集合を取る
    all_trends = set.union(*google_trend_dict.values())
    all_trends_list = list(all_trends)

    # 関連キーワードの出現回数をカウントする
    word_counter = Counter(all_trends_list)

    WORDCLOUD_MASK_SHAPE = np.array(Image.open(WORDCLOUD_MASK))

    # WordCloudを生成する
    wordcloud = WordCloud(
        background_color=WORDCLOUD_BG_COLOR,
        font_path=WORDCLOUD_FONT_PATH,
        width=WORDCLOUD_WIDTH,
        height=WORDCLOUD_HEIGHT,
        colormap=WORDCLOUD_COLOR_MAP,
    ).generate_from_frequencies(word_counter)

    # WordCloudを画像ファイルとして保存する
    wordcloud.to_file(WORDCLOUD_OUTPUT_FILE)

    # 生成したWordCloud画像を返す
    return Image.open(WORDCLOUD_OUTPUT_FILE)


# テスト用のコード
if __name__ == "__main__":
    kw_list = ["SIer", "web系", "IT業界"]
    create_wordcloud(kw_list)
