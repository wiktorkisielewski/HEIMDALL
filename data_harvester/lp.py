import api_requests

class PoolInfo():
	def __init__(self, ticker, interval, count):
		self.ticker = ticker
		self.count = count
		self.interval = interval
		self.depth, self.price, self.price_usd, self.liquidity_units, self.rune_depth = api_requests.pool_history(ticker, interval, count)

#bnb_lp = PoolInfo("BNB.BNB", "hour", "200")
#print(bnb_lp.__dict__)