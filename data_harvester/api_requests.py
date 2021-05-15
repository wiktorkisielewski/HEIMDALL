import requests as req

midgard_link = "https://midgard.thorchain.info/v2"

def pool_info(asset, stats):
	if stats is False:
		data = req.get("{}/pool/{}".format(midgard_link, asset)).json()
	else:
		data = req.get("{}/pool/{}/stats?period={}".format(midgard_link, asset, stats)).json()

def pool_history(asset, interval, count):
	if (interval and count) is None:
		data = req.get("{}/history/depths/{}".format(midgard_link, asset)).json()
	else:
		data = req.get("{}/history/depths/{}?interval={}&count={}".format(midgard_link, asset, interval, count)).json()

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
	return req.get("{}/pools".format(midgard_link)).json()


#print(pool_history("BNB.BNB", "day", "5"))
