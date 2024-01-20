from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    documentation_info = """<h1>Def API</h1>\n\n<p>Url format : http://127.0.0.1:5000/api/v1/word<br>Url Exemple : http://127.0.0.1:5000/api/v1/Hello"""
    return documentation_info

@app.route('/api/v1/<word>')
def api_v1(word):

    #Get the word data
    r = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')

    #Format data to json
    row_data = r.json()

    #Get the word definition
    definition = row_data[0].get('meanings')[0].get('definitions')[0].get('definition')

    #Setting up our API
    data = {
        'Word': word,
        'Definition': definition
    }

    return data



app.run(debug=True)