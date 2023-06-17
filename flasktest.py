from flask import Flask, jsonify, request
import create_wordcloud


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    
    return 'hello!'

@app.route('/word-cloud', methods=['GET', 'POST'])
def get_words():
    #postされたワードで検索して、結果を返す
    data = request.get_json()
    kw_list = data.get("kw_list")
    image = create_wordcloud.create_wordcloud(kw_list=kw_list)
    print(type(image))
    return jsonify({'message': 'Word cloud created!'}), 200



if __name__ == '__main__':
    app.run()