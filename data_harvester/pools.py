import api_requests

def get_pools():
	pools = []
	for i in api_requests.get_pools():
		pools.append(i['asset'].split('-')[0])
	return pools

#def get_pools_depth():
