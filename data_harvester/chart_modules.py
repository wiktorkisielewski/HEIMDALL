from data_harvester import api_requests

def block_spawn(data):
  block = {
    'label': "Pool Depth",
    'backgroundColor': "#54FFD820",
    'borderColor': "#54FFD820",
    'borderWidth': 2,
    'hoverBackgroundColor': "#54FFD820",
    'hoverBorderColor': "#54FFD820",
    'data': data,
  }
  return block

def pool_history_data(ticker, interval, count):
  api_req = api_requests.pool_history(ticker, interval, count)
  blocks = []
  for i in api_req:
    blocks.append(block_spawn(api_req[i]))
  dataset = {
    'labels': list(range(1,int(count))),
    'datasets': blocks
  }
  return dataset
