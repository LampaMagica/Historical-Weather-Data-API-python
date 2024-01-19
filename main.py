from flask import Flask,render_template,url_for
import get_data

app = Flask(__name__)

# @app.route('/tutorial')
# def tutorial():
#     return render_template('tutorial.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<date>/<station>')
def api_v1(date,station):
    row_data = get_data.get_row_by_date(date,station)
    temperature = row_data.get('   TG') / 10
    data = {
        "date":row_data.get('    DATE'),
        "station":row_data.get('STAID'),
        "temperature":temperature
    }
    return data

app.run(debug=True)