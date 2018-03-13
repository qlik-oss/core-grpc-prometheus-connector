import requests
import connector_pb2
from datetime import timezone, datetime

scrape_timestamp = None

def build_metadata(results):
  """
  Builds up the MetaData object needed by engine to figure out which fields
  the data contain, and what type they are (we default to strings here).
  """

  print('Building metadata...')

  fields = set(['name', 'timestamp', 'value', 'scrape_timestamp'])
  metadata = connector_pb2.GetDataResponse()

  for result in results:
    for metric in result['metric'].keys():
      if metric != '__name__':
        fields.add(metric)

  for field in fields:
    metadata.fieldInfo.extend([connector_pb2.FieldInfo(name = field)])

  #print('Metadata built {}'.format(metadata.fieldInfo))

  return metadata

def set_value(result, fieldName, chunk):
  is_string = True
  value = None
  if fieldName == 'name':
    value = result['metric'].get('__name__', '')
    #print(value)
  elif fieldName == 'timestamp':
    is_string = False
    value = result['value'][0]
  elif fieldName == 'value':
    value = result['value'][1]
    try:
      value = float(value)
      is_string = False
    except ValueError:
      pass
  elif fieldName == 'scrape_timestamp':
    value = scrape_timestamp
    is_string = False
  else:
    value = result['metric'].get(fieldName, '')
    if type(value) is float:
      is_string = False

  if is_string:
    if len(value) == 0:
      chunk.stringCodes.append(-1)
      chunk.stringBucket.append('')
      chunk.numberCodes.append(-1)      
    else:
      chunk.stringCodes.append(len(chunk.stringBucket))
      chunk.stringBucket.append(str(value))
      chunk.numberCodes.append(-1)
  else:
    chunk.numberCodes.append(len(chunk.doubleBucket))
    chunk.doubleBucket.append(float(value))
    chunk.stringCodes.append(-1)

def build_chunks(results, metadata):
  """
  Builds up the DataChunk object, in this case we only build up one
  but we could also build up several if the data is too large for
  the streaming gRPC protocol.
  """

  print('Building data chunks...')
  print(metadata.fieldInfo)
  for result in results:
    chunk = connector_pb2.DataChunk()
    for field in metadata.fieldInfo:
      set_value(result, field.name, chunk)
    yield chunk

  print('Data chunks built')

def fetch(prom_url, query_expr):
  """
  Fetch data from Prometheus, transform it, and return gRPC-compatible
  data structures.
  """

  print('Querying Prometheus...')
  global scrape_timestamp
  scrape_timestamp = int(datetime.now(tz=timezone.utc).timestamp() * 1000)

  response = requests.get('{0}/api/v1/query'.format(prom_url), params={ 'query': query_expr })
  results = response.json()['data']['result']

  print('Query complete')

  return results
