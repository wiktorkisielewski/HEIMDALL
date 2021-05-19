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
		depth.append(float(i['assetDepth']))
		price.append(float(i['assetPrice']))
		price_usd.append(float(i['assetPriceUSD']))
		liquidity_units.append(float(i['liquidityUnits']))
		rune_depth.append(float(i['runeDepth']))
		data_output = {'depth': depth, 'price': price, 'price_usd': price_usd, 'liquidity_units': liquidity_units, 'rune_depth': rune_depth}
	return data_output


def swaps_history(asset, interval, count):
	if (asset and interval and count) is None:
		data = req.get("{}/history/swaps".format(midgard_link)).json()
	elif asset is None and (interval and count) is not None:
		data = req.get("{}/history/swaps?interval={}&count={}".format(midgard_link, interval, count)).json()
	elif count is None and (asset and interval) is not None:
		data = req.get("{}/history/swaps?pool={}&interval={}".format(midgard_link, asset, interval)).json()
	elif asset is not None and (interval and count) is None:
		data = req.get("{}/history/swaps?pool={}".format(midgard_link, asset)).json()


	average_slip = []
	rune_price_usd = []
	to_asset_average_slip = [] 
	to_asset_count = []
	to_asset_fees = []
	to_asset_volume = []
	to_rune_average_slip = []
	to_rune_count = []
	to_rune_fees = []
	to_rune_volume = []
	total_count = []
	total_fees = []
	total_volume = []
	for i in data['meta']:
		average_slip.append(i['averageSlip'])
		rune_price_usd.append(i['runePriceUSD'])
		to_asset_average_slip.append(i['toAssetAverageSlip'])
		to_asset_count.append(i['toAssetCount'])
		to_asset_fees.append(i['toAssetFees'])
		to_asset_volume.append(i['toAssetVolume'])
		to_rune_average_slip.append(i['toRuneAverageSlip'])
		to_rune_count.append(i['toRuneCount'])
		to_rune_fees.append(i['toRuneFees'])
		to_rune_volume.append(i['toRuneVolume'])
		total_count.append(i['totalCount'])
		total_fees.append(i['totalFees'])
		total_volume.append(i['totalVolume'])

	return average_slip, rune_price_usd, to_asset_average_slip, to_asset_count, to_asset_fees, to_asset_volume, to_rune_average_slip, to_rune_count, to_rune_fees, to_rune_volume, total_count, total_fees, total_volume




def get_pools():
	return req.get("{}/pools".format(midgard_link)).json()


#print(pool_history("BNB.BNB", "day", "5"))
