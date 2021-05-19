from flask import Flask, render_template, request
from data_harvester import pools, api_requests, chart_modules
import requests
import json

app = Flask(__name__)

time_intervals = ['5min', 'hour', 'day', 'week', 'month', 'year']

ticker = 'ETH.SUSHI-0X6B3595068778DD592E39A122F4F5A5CF09C90FE2'
interval = 'hour'
count = '400'

def get_ticker():
  print('pool', request.form.get('pool_select'))
  return 'BNB.BNB'

@app.route('/', methods=['GET'])
def main():
  data ={'pools': pools.get_pools(), 'intervals': time_intervals, 'dataset': chart_modules.pool_history_data(get_ticker(), interval, count)}
  return render_template('index.html', data=data)

@app.route('/py_test', methods=['GET', 'POST'])
def py_test():
	data2 ={'pools': [1,2,3], 'intervals': [1,2,3], 'dataset': chart_modules.pool_history_data(get_ticker(), interval, count)}
	return render_template('index.html', data=data2)
	


if __name__ == '__main__':
   app.run(debug=True)

