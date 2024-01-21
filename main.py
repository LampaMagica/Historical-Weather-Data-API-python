from flask import Flask,render_template,url_for
import get_data
from datetime import datetime

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
    station = get_data.get_station_main_file()
    html_rendered = render_template('home.html', station=station.to_html())
    return html_rendered

@app.route('/api/v1/<station>/<date>')
def api_v1(date,station):
    get_data_by_date_var = get_data.get_row_by_date(date,station)
    return get_data_by_date_var

    
@app.route('/api/v1/<station>')
def data_station(station):
    data_raw = get_data.get_file_set_index(station,None)
    data = []
    for i, row in data_raw.iterrows():
        data_structred_time = datetime.strptime(str(row['    DATE']),"%Y-%m-%d %H:%M:%S")
        date_without_hours = data_structred_time.strftime('%Y-%m-%d')
        row_data = {
            'Station_ID' : float(row['STAID']),
            'Date' : date_without_hours,
            'Temp' : float(row['   TG'] / 10)
        }
        data.append(row_data)
    return data

    

if __name__ == '__main__':
    app.run(debug=True)