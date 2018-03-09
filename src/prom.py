import requests
import connector_pb2

# Inspired by https://github.com/RobustPerception/python_examples/blob/master/csv/query_csv.py

def build_metadata(results):
  """
  Builds up the MetaData object needed by engine to figure out which fields
  the data contain, and what type they are (we default to strings here).
  """

  print('Building metadata...')

  fields = set(['name', 'timestamp', 'value'])
  metadata = connector_pb2.GetDataResponse()

  for result in results:
    for metric in result['metric'].keys():
      if (metric == '__name__'):
        continue
      fields.add(metric)

  for field in fields:
    metadata.fieldInfo.extend([connector_pb2.FieldInfo(name = field)])

  #print('Metadata built {}'.format(metadata.fieldInfo))

  return metadata

def build_chunks(results, metadata):
  """
  Builds up the DataChunk object, in this case we only build up one
  but we could also build up several if the data is too large for
  the streaming gRPC protocol.
  """

  print('Building data chunks...')

  i = 0
  for result in results:
    print('Loop {} out of {}'.format(i, len(results)))
    chunk = connector_pb2.DataChunk()
    chunk.stringBucket.extend([result['metric'].get('__name__', '')])
    chunk.stringBucket.extend([str(i) for i in result['value']])
    for field in metadata.fieldInfo:
      chunk.stringBucket.extend([result['metric'].get(field.name, '')])
    chunk.stringCodes.extend([-1] * len(chunk.stringBucket))
    i = i + 1
    yield chunk

  print('Data chunks built')

def fetch(prom_url, query_expr):
  """
  Fetch data from Prometheus, transform it, and return gRPC-compatible
  data structures.
  """

  print('Querying Prometheus...')

  response = requests.get('{0}/api/v1/query'.format(prom_url), params={ 'query': query_expr })
  results = response.json()['data']['result']

  print('Query complete')

  return results
