from data_harvester import api_requests

def block_spawn(data):
  block = {
    'label': "Pool Depth",
    'backgroundColor': "rgba(69, 176, 151, 0.78)",
    'borderColor': "rgba(69, 176, 151, 0.78)",
    'borderWidth': 2,
    'hoverBackgroundColor': "rgba(69, 176, 151, 0.78)",
    'hoverBorderColor': "rgba(69, 176, 151, 0.78)",
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



