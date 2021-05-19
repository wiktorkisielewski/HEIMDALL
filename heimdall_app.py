from flask import Flask, render_template, request
from data_harvester import pools, api_requests
import requests
import json

app = Flask(__name__) 

time_intervals = ['5min', 'hour', 'day', 'week', 'month', 'year']

ticker = 'ETH.SUSHI-0X6B3595068778DD592E39A122F4F5A5CF09C90FE2'
interval = 'hour'
count = '400'

def block_spawn(data):
  block = {
    'label': "Pool Depth",
    'backgroundColor': "#54FFD820",
    'borderColor': "#54FFD820",
    'borderWidth': 2,
    'hoverBackgroundColor': "#54FFD820",
    'hoverBorderColor': "#54FFD820",
    'data': data,
  }
  return block

def pool_history_data(ticker, interval, count):
  api_req = api_requests.pool_history(ticker, interval, count)
  blocks = []
  for i in api_req:
    blocks.append(block_spawn(api_req[i]))
  dataset = {
    'labels': list(range(1,int(count))),
    'datasets': blocks
  }
  return dataset


@app.route('/', methods=['GET'])
def main():
    data ={'pools': pools.get_pools(), 'intervals': time_intervals, 'dataset': pool_history_data(ticker, interval, count)}
    return render_template('index.html', data=data)

@app.route('/py_test', methods=['GET', 'POST'])
def py_test():
	data2 ={'pools': [1,2,3], 'intervals': [1,2,3], 'dataset': pool_history_data(ticker, interval, count)}
	return render_template('index.html', data=data2)
	


if __name__ == '__main__':
   app.run(debug=True)

