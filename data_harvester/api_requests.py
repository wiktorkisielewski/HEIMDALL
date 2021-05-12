import requests as req

def pool_info(asset, stats):
	if stats is False:
		data = req.get("https://midgard.thorchain.info/v2/pool/{}".format(asset)).json()
	else:
		data = req.get("https://midgard.thorchain.info/v2/pool/{}/stats?period={}".format(asset, stats)).json()

def pool_history(asset, interval, count):
	if (interval and count) is None:
		data = req.get("https://midgard.thorchain.info/v2/history/depths/{}".format(asset)).json()
	else:
		data = req.get("https://midgard.thorchain.info/v2/history/depths/{}?interval={}&count={}".format(asset, interval, count)).json()

	depth = []
	price = []
	price_usd = [] 
	liquidity_units = []
	rune_depth = []
	for i in data['intervals']:
		depth.append(i['assetDepth'])
		price.append(i['assetPrice'])
		price_usd.append(i['assetPriceUSD'])
		liquidity_units.append(i['liquidityUnits'])
		rune_depth.append(i['runeDepth'])
	return depth, price, price_usd, liquidity_units, rune_depth




def get_pools():
	return req.get("https://midgard.thorchain.info/v2/pools").json()


print(pool_history("BNB.BNB", "day", "5"))
