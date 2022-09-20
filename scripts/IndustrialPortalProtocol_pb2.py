# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IndustrialPortalProtocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CarStateProtocol_pb2 as CarStateProtocol__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='IndustrialPortalProtocol.proto',
  package='IndustrialPortal',
  syntax='proto3',
  serialized_options=_b('Z!../internal/pkg/ba_proto;ba_proto\252\002\030Google.Protobuf.ba_proto'),
  serialized_pb=_b('\n\x1eIndustrialPortalProtocol.proto\x12\x10IndustrialPortal\x1a\x16\x43\x61rStateProtocol.proto\"\xc8\x01\n\x17MessageIndustrialPortal\x12;\n\x0e\x63onnectReponse\x18\x01 \x01(\x0b\x32!.IndustrialPortal.ConnectResponseH\x00\x12:\n\x0estatusResponse\x18\x02 \x01(\x0b\x32 .IndustrialPortal.StatusResponseH\x00\x12,\n\x07\x63ommand\x18\x03 \x01(\x0b\x32\x19.IndustrialPortal.CommandH\x00\x42\x06\n\x04Type\"\xaf\x01\n\rMessageDaemon\x12,\n\x07\x63onnect\x18\x01 \x01(\x0b\x32\x19.IndustrialPortal.ConnectH\x00\x12*\n\x06status\x18\x02 \x01(\x0b\x32\x18.IndustrialPortal.StatusH\x00\x12<\n\x0f\x63ommandResponse\x18\x03 \x01(\x0b\x32!.IndustrialPortal.CommandResponseH\x00\x42\x06\n\x04Type\";\n\x07\x43onnect\x12\x0f\n\x07\x63ompany\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tsessionId\x18\x03 \x01(\t\"~\n\x0f\x43onnectResponse\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.IndustrialPortal.ConnectResponse.Type\x12\x11\n\tsessionId\x18\x02 \x01(\t\"\"\n\x04Type\x12\x06\n\x02OK\x10\x00\x12\x12\n\x0e\x41LREADY_LOGGED\x10\x01\"\x93\x02\n\x06Status\x12.\n\tcarStatus\x18\x01 \x01(\x0b\x32\x1b.CarStateProtocol.CarStatus\x12\x34\n\x06server\x18\x02 \x01(\x0b\x32$.IndustrialPortal.Status.ServerError\x12\x11\n\tsessionId\x18\x03 \x01(\t\x1a\x8f\x01\n\x0bServerError\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).IndustrialPortal.Status.ServerError.Type\x12%\n\x05stops\x18\x02 \x03(\x0b\x32\x16.CarStateProtocol.Stop\" \n\x04Type\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0cSERVER_ERROR\x10\x01\"h\n\x0eStatusResponse\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.IndustrialPortal.StatusResponse.Type\x12\x11\n\tsessionId\x18\x02 \x01(\t\"\x0e\n\x04Type\x12\x06\n\x02OK\x10\x00\"N\n\x07\x43ommand\x12\x30\n\ncarCommand\x18\x01 \x01(\x0b\x32\x1c.CarStateProtocol.CarCommand\x12\x11\n\tsessionId\x18\x02 \x01(\t\"j\n\x0f\x43ommandResponse\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.IndustrialPortal.CommandResponse.Type\x12\x11\n\tsessionId\x18\x02 \x01(\t\"\x0e\n\x04Type\x12\x06\n\x02OK\x10\x00\x42>Z!../internal/pkg/ba_proto;ba_proto\xaa\x02\x18Google.Protobuf.ba_protob\x06proto3')
  ,
  dependencies=[CarStateProtocol__pb2.DESCRIPTOR,])



_CONNECTRESPONSE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='IndustrialPortal.ConnectResponse.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_LOGGED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=610,
  serialized_end=644,
)
_sym_db.RegisterEnumDescriptor(_CONNECTRESPONSE_TYPE)

_STATUS_SERVERERROR_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='IndustrialPortal.Status.ServerError.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=890,
  serialized_end=922,
)
_sym_db.RegisterEnumDescriptor(_STATUS_SERVERERROR_TYPE)

_STATUSRESPONSE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='IndustrialPortal.StatusResponse.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=610,
  serialized_end=624,
)
_sym_db.RegisterEnumDescriptor(_STATUSRESPONSE_TYPE)

_COMMANDRESPONSE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='IndustrialPortal.CommandResponse.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=610,
  serialized_end=624,
)
_sym_db.RegisterEnumDescriptor(_COMMANDRESPONSE_TYPE)


_MESSAGEINDUSTRIALPORTAL = _descriptor.Descriptor(
  name='MessageIndustrialPortal',
  full_name='IndustrialPortal.MessageIndustrialPortal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connectReponse', full_name='IndustrialPortal.MessageIndustrialPortal.connectReponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statusResponse', full_name='IndustrialPortal.MessageIndustrialPortal.statusResponse', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='IndustrialPortal.MessageIndustrialPortal.command', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='IndustrialPortal.MessageIndustrialPortal.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=77,
  serialized_end=277,
)


_MESSAGEDAEMON = _descriptor.Descriptor(
  name='MessageDaemon',
  full_name='IndustrialPortal.MessageDaemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connect', full_name='IndustrialPortal.MessageDaemon.connect', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='IndustrialPortal.MessageDaemon.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commandResponse', full_name='IndustrialPortal.MessageDaemon.commandResponse', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='IndustrialPortal.MessageDaemon.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=280,
  serialized_end=455,
)


_CONNECT = _descriptor.Descriptor(
  name='Connect',
  full_name='IndustrialPortal.Connect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='company', full_name='IndustrialPortal.Connect.company', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='IndustrialPortal.Connect.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='IndustrialPortal.Connect.sessionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=516,
)


_CONNECTRESPONSE = _descriptor.Descriptor(
  name='ConnectResponse',
  full_name='IndustrialPortal.ConnectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='IndustrialPortal.ConnectResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='IndustrialPortal.ConnectResponse.sessionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONNECTRESPONSE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=644,
)


_STATUS_SERVERERROR = _descriptor.Descriptor(
  name='ServerError',
  full_name='IndustrialPortal.Status.ServerError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='IndustrialPortal.Status.ServerError.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stops', full_name='IndustrialPortal.Status.ServerError.stops', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUS_SERVERERROR_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=779,
  serialized_end=922,
)

_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='IndustrialPortal.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='carStatus', full_name='IndustrialPortal.Status.carStatus', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server', full_name='IndustrialPortal.Status.server', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='IndustrialPortal.Status.sessionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATUS_SERVERERROR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=647,
  serialized_end=922,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='IndustrialPortal.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='IndustrialPortal.StatusResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='IndustrialPortal.StatusResponse.sessionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUSRESPONSE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=924,
  serialized_end=1028,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='IndustrialPortal.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='carCommand', full_name='IndustrialPortal.Command.carCommand', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='IndustrialPortal.Command.sessionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1030,
  serialized_end=1108,
)


_COMMANDRESPONSE = _descriptor.Descriptor(
  name='CommandResponse',
  full_name='IndustrialPortal.CommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='IndustrialPortal.CommandResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='IndustrialPortal.CommandResponse.sessionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMANDRESPONSE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1110,
  serialized_end=1216,
)

_MESSAGEINDUSTRIALPORTAL.fields_by_name['connectReponse'].message_type = _CONNECTRESPONSE
_MESSAGEINDUSTRIALPORTAL.fields_by_name['statusResponse'].message_type = _STATUSRESPONSE
_MESSAGEINDUSTRIALPORTAL.fields_by_name['command'].message_type = _COMMAND
_MESSAGEINDUSTRIALPORTAL.oneofs_by_name['Type'].fields.append(
  _MESSAGEINDUSTRIALPORTAL.fields_by_name['connectReponse'])
_MESSAGEINDUSTRIALPORTAL.fields_by_name['connectReponse'].containing_oneof = _MESSAGEINDUSTRIALPORTAL.oneofs_by_name['Type']
_MESSAGEINDUSTRIALPORTAL.oneofs_by_name['Type'].fields.append(
  _MESSAGEINDUSTRIALPORTAL.fields_by_name['statusResponse'])
_MESSAGEINDUSTRIALPORTAL.fields_by_name['statusResponse'].containing_oneof = _MESSAGEINDUSTRIALPORTAL.oneofs_by_name['Type']
_MESSAGEINDUSTRIALPORTAL.oneofs_by_name['Type'].fields.append(
  _MESSAGEINDUSTRIALPORTAL.fields_by_name['command'])
_MESSAGEINDUSTRIALPORTAL.fields_by_name['command'].containing_oneof = _MESSAGEINDUSTRIALPORTAL.oneofs_by_name['Type']
_MESSAGEDAEMON.fields_by_name['connect'].message_type = _CONNECT
_MESSAGEDAEMON.fields_by_name['status'].message_type = _STATUS
_MESSAGEDAEMON.fields_by_name['commandResponse'].message_type = _COMMANDRESPONSE
_MESSAGEDAEMON.oneofs_by_name['Type'].fields.append(
  _MESSAGEDAEMON.fields_by_name['connect'])
_MESSAGEDAEMON.fields_by_name['connect'].containing_oneof = _MESSAGEDAEMON.oneofs_by_name['Type']
_MESSAGEDAEMON.oneofs_by_name['Type'].fields.append(
  _MESSAGEDAEMON.fields_by_name['status'])
_MESSAGEDAEMON.fields_by_name['status'].containing_oneof = _MESSAGEDAEMON.oneofs_by_name['Type']
_MESSAGEDAEMON.oneofs_by_name['Type'].fields.append(
  _MESSAGEDAEMON.fields_by_name['commandResponse'])
_MESSAGEDAEMON.fields_by_name['commandResponse'].containing_oneof = _MESSAGEDAEMON.oneofs_by_name['Type']
_CONNECTRESPONSE.fields_by_name['type'].enum_type = _CONNECTRESPONSE_TYPE
_CONNECTRESPONSE_TYPE.containing_type = _CONNECTRESPONSE
_STATUS_SERVERERROR.fields_by_name['type'].enum_type = _STATUS_SERVERERROR_TYPE
_STATUS_SERVERERROR.fields_by_name['stops'].message_type = CarStateProtocol__pb2._STOP
_STATUS_SERVERERROR.containing_type = _STATUS
_STATUS_SERVERERROR_TYPE.containing_type = _STATUS_SERVERERROR
_STATUS.fields_by_name['carStatus'].message_type = CarStateProtocol__pb2._CARSTATUS
_STATUS.fields_by_name['server'].message_type = _STATUS_SERVERERROR
_STATUSRESPONSE.fields_by_name['type'].enum_type = _STATUSRESPONSE_TYPE
_STATUSRESPONSE_TYPE.containing_type = _STATUSRESPONSE
_COMMAND.fields_by_name['carCommand'].message_type = CarStateProtocol__pb2._CARCOMMAND
_COMMANDRESPONSE.fields_by_name['type'].enum_type = _COMMANDRESPONSE_TYPE
_COMMANDRESPONSE_TYPE.containing_type = _COMMANDRESPONSE
DESCRIPTOR.message_types_by_name['MessageIndustrialPortal'] = _MESSAGEINDUSTRIALPORTAL
DESCRIPTOR.message_types_by_name['MessageDaemon'] = _MESSAGEDAEMON
DESCRIPTOR.message_types_by_name['Connect'] = _CONNECT
DESCRIPTOR.message_types_by_name['ConnectResponse'] = _CONNECTRESPONSE
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['CommandResponse'] = _COMMANDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageIndustrialPortal = _reflection.GeneratedProtocolMessageType('MessageIndustrialPortal', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEINDUSTRIALPORTAL,
  __module__ = 'IndustrialPortalProtocol_pb2'
  # @@protoc_insertion_point(class_scope:IndustrialPortal.MessageIndustrialPortal)
  ))
_sym_db.RegisterMessage(MessageIndustrialPortal)

MessageDaemon = _reflection.GeneratedProtocolMessageType('MessageDaemon', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEDAEMON,
  __module__ = 'IndustrialPortalProtocol_pb2'
  # @@protoc_insertion_point(class_scope:IndustrialPortal.MessageDaemon)
  ))
_sym_db.RegisterMessage(MessageDaemon)

Connect = _reflection.GeneratedProtocolMessageType('Connect', (_message.Message,), dict(
  DESCRIPTOR = _CONNECT,
  __module__ = 'IndustrialPortalProtocol_pb2'
  # @@protoc_insertion_point(class_scope:IndustrialPortal.Connect)
  ))
_sym_db.RegisterMessage(Connect)

ConnectResponse = _reflection.GeneratedProtocolMessageType('ConnectResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTRESPONSE,
  __module__ = 'IndustrialPortalProtocol_pb2'
  # @@protoc_insertion_point(class_scope:IndustrialPortal.ConnectResponse)
  ))
_sym_db.RegisterMessage(ConnectResponse)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(

  ServerError = _reflection.GeneratedProtocolMessageType('ServerError', (_message.Message,), dict(
    DESCRIPTOR = _STATUS_SERVERERROR,
    __module__ = 'IndustrialPortalProtocol_pb2'
    # @@protoc_insertion_point(class_scope:IndustrialPortal.Status.ServerError)
    ))
  ,
  DESCRIPTOR = _STATUS,
  __module__ = 'IndustrialPortalProtocol_pb2'
  # @@protoc_insertion_point(class_scope:IndustrialPortal.Status)
  ))
_sym_db.RegisterMessage(Status)
_sym_db.RegisterMessage(Status.ServerError)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'IndustrialPortalProtocol_pb2'
  # @@protoc_insertion_point(class_scope:IndustrialPortal.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'IndustrialPortalProtocol_pb2'
  # @@protoc_insertion_point(class_scope:IndustrialPortal.Command)
  ))
_sym_db.RegisterMessage(Command)

CommandResponse = _reflection.GeneratedProtocolMessageType('CommandResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDRESPONSE,
  __module__ = 'IndustrialPortalProtocol_pb2'
  # @@protoc_insertion_point(class_scope:IndustrialPortal.CommandResponse)
  ))
_sym_db.RegisterMessage(CommandResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
