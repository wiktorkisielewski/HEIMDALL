import api_requests

class PoolInfo():
	def __init__(self, ticker, interval, count):
		self.ticker = ticker
		self.count = count
		self.interval = interval
		self.depth, self.price, self.price_usd, self.liquidity_units, self.rune_depth = api_requests.pool_history(ticker, interval, count)

#bnb_lp = PoolInfo("BNB.BNB", "hour", "200")
#print(bnb_lp.__dict__)

test = {
  "labels": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  "datasets": {
    "label": "Pool Depth",
    "backgroundColor": "#54FFD820",
    "borderColor": "#54FFD820",
    "borderWidth": 2,
    "hoverBackgroundColor": "#54FFD820",
    "hoverBorderColor": "#54FFD820",
    "data": [49, 47, 51, 48, 45, 44, 40, 42, 47, 45]
  }
}

def test_function():
	return test