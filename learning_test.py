from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    documentation_info = """<h1>Def API</h1>\n\n<p>Url format : http://127.0.0.1:5000/api/v1/word<br>Url Exemple : http://127.0.0.1:5000/api/v1/Hello"""
    return documentation_info

@app.route('/api/v1/<word>')
def api_v1(word):
    data = {
        'word': word,
        'definition': word.upper()
    }
    return data

if __name__ == "__name__":
    app.run(debug=True)