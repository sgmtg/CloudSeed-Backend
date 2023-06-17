from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    
    return 'hello!'

@app.route('/<words>', methods=['GET', 'POST'])
def get_words(words):
    #postされたワードで検索して、結果を返す
    # search_words(words)




    #結果からワードクラウドを作成
    # create_wordcloud(words)

    
    return jsonify({'image': 'gazou', 'text': words}), 200

if __name__ == '__main__':
    app.run()