from flask import Flask, render_template
from data_harvester import api_requests
app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

if __name__ == '__main__':
   app.run()