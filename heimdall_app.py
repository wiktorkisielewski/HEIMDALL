from flask import Flask, render_template, request
from data_harvester import pools
import requests

app = Flask(__name__)
time_intervals = ['5min', 'hour', 'day', 'week', 'month', 'year']

@app.route('/', methods=['GET'])
def main():
    data ={'pools': pools.get_pools(), 'intervals': time_intervals}
    return render_template('index.html', data=data)

@app.route('/py_test', methods=['GET', 'POST'])
def py_test():
	return "420x69"
	


if __name__ == '__main__':
   app.run(debug=True)

