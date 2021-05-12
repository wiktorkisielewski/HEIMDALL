import requests as req

def pool_info(asset, stats):
	if stats is False:
		return req.get("https://midgard.thorchain.info/v2/pool/{}".format(asset)).json()
	else:
		return req.get("https://midgard.thorchain.info/v2/pool/{}/stats?period={}".format(asset, stats)).json()

def pool_history(asset, interval, count):
	if (interval and count) is False:
		return req.get("https://midgard.thorchain.info/v2/history/depths/{}".format(asset)).json()
	else:
		return req.get("https://midgard.thorchain.info/v2/history/depths/{}?interval={}&count={}".format(asset, interval, count)).json()


def get_pools():
	return req.get("https://midgard.thorchain.info/v2/pools").json()

print(pool_history("BNB.BNB", "day", "10"))