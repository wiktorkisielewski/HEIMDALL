from flask import Flask, render_template
from data_harvester import pools

app = Flask(__name__)
time_intervals = ['5min', 'hour', 'day', 'week', 'month', 'year']

@app.route('/', methods=['GET'])
def main():
    pool_list = pools.get_pools()
    return render_template('index.html', pools=pool_list, intervals=time_intervals)

if __name__ == '__main__':
   app.run(debug=True)