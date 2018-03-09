import connector
import concurrent.futures as futures
import grpc
import connector_pb2_grpc
import time

_LISTENING_PORT = 9001
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

print('Starting...')

svc = connector.Service()
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
connector_pb2_grpc.add_ConnectorServicer_to_server(svc, server)
server.add_insecure_port('[::]:{}'.format(_LISTENING_PORT))

server.start()

print('Listening on [::]:{}'.format(_LISTENING_PORT))

try:
  while True:
    time.sleep(_ONE_DAY_IN_SECONDS)
except KeyboardInterrupt:
  server.stop(0)
