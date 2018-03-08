from grpc_tools import protoc

protoc.main((
  '',
  '--python_out=.',
  '--grpc_python_out=.',
  './connector.proto',
))
