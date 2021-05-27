from data_harvester import api_requests

def block_spawn(data):
  block = {
    'label': "Pool Depth",
    'backgroundColor': "rgba(0, 0, 0, 0.0)",
    'borderColor': "rgba(255, 255, 255, 0.8)",
    'borderWidth': 2,
    'hoverBackgroundColor': "rgba(0, 0, 0, 0.0)",
    'hoverBorderColor': "rgba(255, 255, 255, 1.0)",
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



