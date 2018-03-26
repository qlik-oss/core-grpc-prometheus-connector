# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connector.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='connector.proto',
  package='qlik.connect',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x63onnector.proto\x12\x0cqlik.connect\"J\n\x0e\x43onnectionInfo\x12\x18\n\x10\x63onnectionString\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"=\n\x0bSessionInfo\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\r\n\x05\x64ocId\x18\x03 \x01(\t\"(\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"J\n\x08\x44\x61taInfo\x12\x11\n\tstatement\x18\x01 \x01(\t\x12+\n\nparameters\x18\x02 \x03(\x0b\x32\x17.qlik.connect.Parameter\"\x9b\x01\n\x0b\x44\x61taRequest\x12\x30\n\nconnection\x18\x01 \x01(\x0b\x32\x1c.qlik.connect.ConnectionInfo\x12.\n\x0bsessionInfo\x18\x02 \x01(\x0b\x32\x19.qlik.connect.SessionInfo\x12*\n\nparameters\x18\x03 \x01(\x0b\x32\x16.qlik.connect.DataInfo\"a\n\tDataChunk\x12\x14\n\x0cstringBucket\x18\x01 \x03(\t\x12\x14\n\x0c\x64oubleBucket\x18\x02 \x03(\x01\x12\x13\n\x0bstringCodes\x18\x03 \x03(\x11\x12\x13\n\x0bnumberCodes\x18\x04 \x03(\x12\"<\n\x0f\x46ieldAttributes\x12)\n\x04Type\x18\x01 \x01(\x0e\x32\x1b.qlik.connect.FieldAttrType\"\x91\x01\n\tFieldInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x0csemanticType\x18\x02 \x01(\x0e\x32\x1a.qlik.connect.SemanticType\x12\x36\n\x0f\x66ieldAttributes\x18\x03 \x01(\x0b\x32\x1d.qlik.connect.FieldAttributes\x12\x0c\n\x04tags\x18\x04 \x03(\t\"P\n\x0fGetDataResponse\x12*\n\tfieldInfo\x18\x01 \x03(\x0b\x32\x17.qlik.connect.FieldInfo\x12\x11\n\ttableName\x18\x02 \x01(\t\"<\n\x08MetaInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x11\n\tdeveloper\x18\x03 \x01(\t\"\x11\n\x0fMetaInfoRequest*J\n\x0cSemanticType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x1f\n\x1bUNIX_SECONDS_SINCE_1970_UTC\x10\x01\x12\x0c\n\x08ISO_8601\x10\x02*\x82\x01\n\rFieldAttrType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\x08\n\x04REAL\x10\x02\x12\x08\n\x04\x44\x41TE\x10\x03\x12\x08\n\x04TIME\x10\x04\x12\r\n\tTIMESTAMP\x10\x05\x12\x0c\n\x08INTERVAL\x10\x06\x12\x0b\n\x07INTEGER\x10\n\x12\x07\n\x03\x46IX\x10\x0b\x12\t\n\x05MONEY\x10\x0c\x32\x96\x01\n\tConnector\x12\x41\n\x07GetData\x12\x19.qlik.connect.DataRequest\x1a\x17.qlik.connect.DataChunk\"\x00\x30\x01\x12\x46\n\x0bGetMetaInfo\x12\x1d.qlik.connect.MetaInfoRequest\x1a\x16.qlik.connect.MetaInfo\"\x00\x62\x06proto3')
)

_SEMANTICTYPE = _descriptor.EnumDescriptor(
  name='SemanticType',
  full_name='qlik.connect.SemanticType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNIX_SECONDS_SINCE_1970_UTC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISO_8601', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=920,
  serialized_end=994,
)
_sym_db.RegisterEnumDescriptor(_SEMANTICTYPE)

SemanticType = enum_type_wrapper.EnumTypeWrapper(_SEMANTICTYPE)
_FIELDATTRTYPE = _descriptor.EnumDescriptor(
  name='FieldAttrType',
  full_name='qlik.connect.FieldAttrType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERVAL', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTEGER', index=7, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIX', index=8, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONEY', index=9, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=997,
  serialized_end=1127,
)
_sym_db.RegisterEnumDescriptor(_FIELDATTRTYPE)

FieldAttrType = enum_type_wrapper.EnumTypeWrapper(_FIELDATTRTYPE)
DEFAULT = 0
UNIX_SECONDS_SINCE_1970_UTC = 1
ISO_8601 = 2
UNKNOWN = 0
TEXT = 1
REAL = 2
DATE = 3
TIME = 4
TIMESTAMP = 5
INTERVAL = 6
INTEGER = 10
FIX = 11
MONEY = 12



_CONNECTIONINFO = _descriptor.Descriptor(
  name='ConnectionInfo',
  full_name='qlik.connect.ConnectionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connectionString', full_name='qlik.connect.ConnectionInfo.connectionString', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='qlik.connect.ConnectionInfo.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='qlik.connect.ConnectionInfo.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=107,
)


_SESSIONINFO = _descriptor.Descriptor(
  name='SessionInfo',
  full_name='qlik.connect.SessionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='qlik.connect.SessionInfo.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='qlik.connect.SessionInfo.sessionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docId', full_name='qlik.connect.SessionInfo.docId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=170,
)


_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='qlik.connect.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='qlik.connect.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='qlik.connect.Parameter.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=212,
)


_DATAINFO = _descriptor.Descriptor(
  name='DataInfo',
  full_name='qlik.connect.DataInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statement', full_name='qlik.connect.DataInfo.statement', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='qlik.connect.DataInfo.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=288,
)


_DATAREQUEST = _descriptor.Descriptor(
  name='DataRequest',
  full_name='qlik.connect.DataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='qlik.connect.DataRequest.connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionInfo', full_name='qlik.connect.DataRequest.sessionInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='qlik.connect.DataRequest.parameters', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=446,
)


_DATACHUNK = _descriptor.Descriptor(
  name='DataChunk',
  full_name='qlik.connect.DataChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringBucket', full_name='qlik.connect.DataChunk.stringBucket', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doubleBucket', full_name='qlik.connect.DataChunk.doubleBucket', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringCodes', full_name='qlik.connect.DataChunk.stringCodes', index=2,
      number=3, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numberCodes', full_name='qlik.connect.DataChunk.numberCodes', index=3,
      number=4, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=545,
)


_FIELDATTRIBUTES = _descriptor.Descriptor(
  name='FieldAttributes',
  full_name='qlik.connect.FieldAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='qlik.connect.FieldAttributes.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=607,
)


_FIELDINFO = _descriptor.Descriptor(
  name='FieldInfo',
  full_name='qlik.connect.FieldInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='qlik.connect.FieldInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='semanticType', full_name='qlik.connect.FieldInfo.semanticType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fieldAttributes', full_name='qlik.connect.FieldInfo.fieldAttributes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='qlik.connect.FieldInfo.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=755,
)


_GETDATARESPONSE = _descriptor.Descriptor(
  name='GetDataResponse',
  full_name='qlik.connect.GetDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fieldInfo', full_name='qlik.connect.GetDataResponse.fieldInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableName', full_name='qlik.connect.GetDataResponse.tableName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=837,
)


_METAINFO = _descriptor.Descriptor(
  name='MetaInfo',
  full_name='qlik.connect.MetaInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='qlik.connect.MetaInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='qlik.connect.MetaInfo.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='developer', full_name='qlik.connect.MetaInfo.developer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=839,
  serialized_end=899,
)


_METAINFOREQUEST = _descriptor.Descriptor(
  name='MetaInfoRequest',
  full_name='qlik.connect.MetaInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=901,
  serialized_end=918,
)

_DATAINFO.fields_by_name['parameters'].message_type = _PARAMETER
_DATAREQUEST.fields_by_name['connection'].message_type = _CONNECTIONINFO
_DATAREQUEST.fields_by_name['sessionInfo'].message_type = _SESSIONINFO
_DATAREQUEST.fields_by_name['parameters'].message_type = _DATAINFO
_FIELDATTRIBUTES.fields_by_name['Type'].enum_type = _FIELDATTRTYPE
_FIELDINFO.fields_by_name['semanticType'].enum_type = _SEMANTICTYPE
_FIELDINFO.fields_by_name['fieldAttributes'].message_type = _FIELDATTRIBUTES
_GETDATARESPONSE.fields_by_name['fieldInfo'].message_type = _FIELDINFO
DESCRIPTOR.message_types_by_name['ConnectionInfo'] = _CONNECTIONINFO
DESCRIPTOR.message_types_by_name['SessionInfo'] = _SESSIONINFO
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['DataInfo'] = _DATAINFO
DESCRIPTOR.message_types_by_name['DataRequest'] = _DATAREQUEST
DESCRIPTOR.message_types_by_name['DataChunk'] = _DATACHUNK
DESCRIPTOR.message_types_by_name['FieldAttributes'] = _FIELDATTRIBUTES
DESCRIPTOR.message_types_by_name['FieldInfo'] = _FIELDINFO
DESCRIPTOR.message_types_by_name['GetDataResponse'] = _GETDATARESPONSE
DESCRIPTOR.message_types_by_name['MetaInfo'] = _METAINFO
DESCRIPTOR.message_types_by_name['MetaInfoRequest'] = _METAINFOREQUEST
DESCRIPTOR.enum_types_by_name['SemanticType'] = _SEMANTICTYPE
DESCRIPTOR.enum_types_by_name['FieldAttrType'] = _FIELDATTRTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectionInfo = _reflection.GeneratedProtocolMessageType('ConnectionInfo', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTIONINFO,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.ConnectionInfo)
  ))
_sym_db.RegisterMessage(ConnectionInfo)

SessionInfo = _reflection.GeneratedProtocolMessageType('SessionInfo', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONINFO,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.SessionInfo)
  ))
_sym_db.RegisterMessage(SessionInfo)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETER,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.Parameter)
  ))
_sym_db.RegisterMessage(Parameter)

DataInfo = _reflection.GeneratedProtocolMessageType('DataInfo', (_message.Message,), dict(
  DESCRIPTOR = _DATAINFO,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.DataInfo)
  ))
_sym_db.RegisterMessage(DataInfo)

DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), dict(
  DESCRIPTOR = _DATAREQUEST,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.DataRequest)
  ))
_sym_db.RegisterMessage(DataRequest)

DataChunk = _reflection.GeneratedProtocolMessageType('DataChunk', (_message.Message,), dict(
  DESCRIPTOR = _DATACHUNK,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.DataChunk)
  ))
_sym_db.RegisterMessage(DataChunk)

FieldAttributes = _reflection.GeneratedProtocolMessageType('FieldAttributes', (_message.Message,), dict(
  DESCRIPTOR = _FIELDATTRIBUTES,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.FieldAttributes)
  ))
_sym_db.RegisterMessage(FieldAttributes)

FieldInfo = _reflection.GeneratedProtocolMessageType('FieldInfo', (_message.Message,), dict(
  DESCRIPTOR = _FIELDINFO,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.FieldInfo)
  ))
_sym_db.RegisterMessage(FieldInfo)

GetDataResponse = _reflection.GeneratedProtocolMessageType('GetDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETDATARESPONSE,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.GetDataResponse)
  ))
_sym_db.RegisterMessage(GetDataResponse)

MetaInfo = _reflection.GeneratedProtocolMessageType('MetaInfo', (_message.Message,), dict(
  DESCRIPTOR = _METAINFO,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.MetaInfo)
  ))
_sym_db.RegisterMessage(MetaInfo)

MetaInfoRequest = _reflection.GeneratedProtocolMessageType('MetaInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _METAINFOREQUEST,
  __module__ = 'connector_pb2'
  # @@protoc_insertion_point(class_scope:qlik.connect.MetaInfoRequest)
  ))
_sym_db.RegisterMessage(MetaInfoRequest)



_CONNECTOR = _descriptor.ServiceDescriptor(
  name='Connector',
  full_name='qlik.connect.Connector',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1130,
  serialized_end=1280,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='qlik.connect.Connector.GetData',
    index=0,
    containing_service=None,
    input_type=_DATAREQUEST,
    output_type=_DATACHUNK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMetaInfo',
    full_name='qlik.connect.Connector.GetMetaInfo',
    index=1,
    containing_service=None,
    input_type=_METAINFOREQUEST,
    output_type=_METAINFO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECTOR)

DESCRIPTOR.services_by_name['Connector'] = _CONNECTOR

# @@protoc_insertion_point(module_scope)