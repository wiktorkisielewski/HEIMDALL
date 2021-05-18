from flask import Flask, render_template, request
from data_harvester import pools, api_requests
import requests
import json

app = Flask(__name__) 

time_intervals = ['5min', 'hour', 'day', 'week', 'month', 'year']

dataset = {
  'labels': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  'datasets': [{
    'label': "Pool Depth",
    'backgroundColor': "#54FFD820",
    'borderColor': "#54FFD820",
    'borderWidth': 2,
    'hoverBackgroundColor': "#54FFD820",
    'hoverBorderColor': "#54FFD820",
    'data': [49, 47, 51, 48, 45, 44, 40, 42, 47, 45],
    #api_requests.pool_history('BNB.BNB', 'day', '10')[0]
  },
  {
    'label': "Price",
    'backgroundColor': "#54FFD840",
    'borderColor': "#54FFD840",
    'borderWidth': 2,
    'hoverBackgroundColor': "#54FFD840",
    'hoverBorderColor': "#54FFD840",
    'data': [11, 9, 7, 10, 9, 12, 16, 15, 18, 22],
  },
  {
    'label': "Rune Depth",
    'backgroundColor': "#54FFD860",
    'borderColor': "#54FFD860",
    'borderWidth': 2,
    'hoverBackgroundColor': "#54FFD860",
    'hoverBorderColor': "#54FFD860",
    'data': [32, 35, 33, 31, 29, 34, 35, 37, 36, 34],
  }
  ]
}


@app.route('/', methods=['GET'])
def main():
    data ={'pools': pools.get_pools(), 'intervals': time_intervals, 'dataset': dataset}
    return render_template('index.html', data=data)

@app.route('/py_test', methods=['GET', 'POST'])
def py_test():
	data2 ={'pools': [1,2,3], 'intervals': [1,2,3], 'dataset': dataset}
	return render_template('index.html', data=data2)
	


if __name__ == '__main__':
   app.run(debug=True)

