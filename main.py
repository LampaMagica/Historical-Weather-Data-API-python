from flask import Flask,render_template,url_for

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

@app.route('/api/v1/<date>/<station>')
def api_v1(date,station):
    temperature = 24
    data = {
        "date":date,
        "station":station,
        "temperature":temperature
    }
    return data

app.run(debug=True)