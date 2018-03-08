import connector
import concurrent.futures as futures
import grpc
import connector_pb2_grpc
import time

listening_port = 9001

print('Starting...')

svc = connector.Service()
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
connector_pb2_grpc.add_ConnectorServicer_to_server(svc, server)
server.add_insecure_port('[::]:{}'.format(listening_port))

server.start()

print('Listening on [::]:{}'.format(listening_port))

try:
  while True:
    time.sleep(1000)
except KeyboardInterrupt:
  server.stop(0)
