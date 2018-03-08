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
    data = prom.fetch('http://prometheus:9090', '{job=~".+"}')
    # data[0] is the field info
    # TODO: We need to send x-qlik-getdata-bin based on data[0]
    # We might have to fix prom.py to add types to the buckets
    # in the data list
    return data
