import csv
import requests
import sys

# Inspired by https://github.com/RobustPerception/python_examples/blob/master/csv/query_csv.py

def fetch(prom_url, query_expr):
  response = requests.get('{0}/api/v1/query'.format(prom_url), params={ 'query': query_expr })
  results = response.json()['data']['result']

  table_header = set()
  for result in results:
    table_header.update(result['metric'].keys())

  table_header.discard('__name__')
  table_header = sorted(table_header)

  table = list()
  table.append(['name', 'timestamp', 'value'] + table_header)

  for result in results:
    l = [result['metric'].get('__name__', '')] + result['value']
    for label in table_header:
      l.append(result['metric'].get(label, ''))
    table.append(l)

  return table
