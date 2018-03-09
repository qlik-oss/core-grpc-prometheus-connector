import connector_pb2_grpc
import connector_pb2
import prom

class Service(connector_pb2_grpc.ConnectorServicer):
  def GetMetaInfo(self, request, context):
    return connector_pb2.MetaInfo(
      name = 'Prometheus Connector',
      version = '0.0.1',
      developer = 'Qlik'
    )
  def GetData(self, request, context):
    # TODO: Get these params from environment/call settings from script
    print('Fetching data from Prometheus...')
    results = prom.fetch('http://prometheus:9090', '{__name__=~".+"}')

    print('Data fetched, sending initial metadata...')
    metadata = prom.build_metadata(results)
    context.send_initial_metadata((('qlik-getdata-bin', metadata.SerializeToString()),))

    print('Initial metadata sent, sending chunks...')

    return prom.build_chunks(results, metadata)
