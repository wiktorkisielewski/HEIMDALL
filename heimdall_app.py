from flask import Flask, render_template, request
from data_harvester import pools
import requests

app = Flask(__name__)
time_intervals = ['5min', 'hour', 'day', 'week', 'month', 'year']

@app.route('/', methods=['GET'])
def main():
    data ={'pools': pools.get_pools(), 'intervals': time_intervals}
    return render_template('index.html', data=data)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['data.pool']
    return render_template('index.html', pools=pool_list, intervals=time_intervals)

if __name__ == '__main__':
   app.run(debug=False)

