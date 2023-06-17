from collections import Counter
from wordcloud import WordCloud
from pytrends.request import TrendReq
from PIL import Image

def create_wordcloud(kw_list):
    WORDCLOUD_FONT_PATH ='/Library/Fonts/Arial Unicode.ttf'
    # wordcloud用の幅
    WORDCLOUD_WIDTH = 600
    # wordcloud用の高さ
    WORDCLOUD_HEIGHT = 600
    # wordcloud用の背景色
    WORDCLOUD_BG_COLOR = 'white'
    # wordcloud出力先
    WORDCLOUD_OUTPUT_FILE = './images/wordcloud.png'

    # ---------- 処理開始 ----------

    # GoogleTrandsのdict
    google_trend_dict = {}

    """
    期間の指定例：
    timeframe='now 1-d' -> 過去1日間（あるいは7-dで指定）
    timeframe='today 1-m' -> 過去1ヶ月間（あるいは3-mで指定）
    timeframe='today 5-y' -> 過去5年間（5-yしか指定できない）
    """
    pytrends = TrendReq(hl='ja-JP', tz=360)
    for keyword in kw_list:
        pytrends.build_payload([keyword], cat=0, timeframe='today 5-y', geo='JP', gprop='')
        trends = pytrends.related_queries()
        trends_values = trends[keyword]['top'].values.tolist()

        keyword_trends = []
        for value in trends_values:
            item = str(value[0]).replace(keyword, '') # 関連キーワードのみを出力するので、検索キーワードは消している
            item = item.replace('　', '')
            item = item.replace(' ', '')
            keyword_trends.append(item)

        google_trend_dict[keyword] = set(keyword_trends)

    # 和を取る
    all_trends = set.union(*google_trend_dict.values())
    all_trends_list = list(all_trends)

    # 
    word_counter = Counter(all_trends_list)
    wordcloud = WordCloud(
        font_path= WORDCLOUD_FONT_PATH,
        width = WORDCLOUD_WIDTH,
        height = WORDCLOUD_HEIGHT).generate_from_frequencies(word_counter)
    wordcloud.to_file(WORDCLOUD_OUTPUT_FILE)
    return Image.open(WORDCLOUD_OUTPUT_FILE)

# test用
if __name__ == '__main__':
    kw_list = ["SIer", "web系", "IT業界"]
    create_wordcloud(kw_list)
