# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CarStateProtocol.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CarStateProtocol.proto',
  package='CarStateProtocol',
  syntax='proto3',
  serialized_options=b'Z!../internal/pkg/ba_proto;ba_proto\252\002\030Google.Protobuf.ba_proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x43\x61rStateProtocol.proto\x12\x10\x43\x61rStateProtocol\"\x86\x03\n\tCarStatus\x12\x38\n\ttelemetry\x18\x01 \x01(\x0b\x32%.CarStateProtocol.CarStatus.Telemetry\x12\x30\n\x05state\x18\x02 \x01(\x0e\x32!.CarStateProtocol.CarStatus.State\x12$\n\x04stop\x18\x03 \x01(\x0b\x32\x16.CarStateProtocol.Stop\x1a`\n\tTelemetry\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x0c\n\x04\x66uel\x18\x02 \x01(\x01\x12\x36\n\x08position\x18\x03 \x01(\x0b\x32$.CarStateProtocol.CarStatus.Position\x1a\x41\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\"B\n\x05State\x12\x08\n\x04IDLE\x10\x00\x12\t\n\x05\x44RIVE\x10\x01\x12\x0b\n\x07IN_STOP\x10\x02\x12\x0c\n\x08OBSTACLE\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"\x96\x01\n\nCarCommand\x12%\n\x05stops\x18\x01 \x03(\x0b\x32\x16.CarStateProtocol.Stop\x12\x33\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32#.CarStateProtocol.CarCommand.Action\",\n\x06\x41\x63tion\x12\r\n\tNO_ACTION\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\t\n\x05START\x10\x02\"\x12\n\x04Stop\x12\n\n\x02to\x18\x01 \x01(\tB>Z!../internal/pkg/ba_proto;ba_proto\xaa\x02\x18Google.Protobuf.ba_protob\x06proto3'
)



_CARSTATUS_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='CarStateProtocol.CarStatus.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DRIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_STOP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OBSTACLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=369,
  serialized_end=435,
)
_sym_db.RegisterEnumDescriptor(_CARSTATUS_STATE)

_CARCOMMAND_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='CarStateProtocol.CarCommand.Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ACTION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='START', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=544,
  serialized_end=588,
)
_sym_db.RegisterEnumDescriptor(_CARCOMMAND_ACTION)


_CARSTATUS_TELEMETRY = _descriptor.Descriptor(
  name='Telemetry',
  full_name='CarStateProtocol.CarStatus.Telemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='CarStateProtocol.CarStatus.Telemetry.speed', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fuel', full_name='CarStateProtocol.CarStatus.Telemetry.fuel', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='CarStateProtocol.CarStatus.Telemetry.position', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=204,
  serialized_end=300,
)

_CARSTATUS_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='CarStateProtocol.CarStatus.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='CarStateProtocol.CarStatus.Position.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='CarStateProtocol.CarStatus.Position.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='CarStateProtocol.CarStatus.Position.altitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=302,
  serialized_end=367,
)

_CARSTATUS = _descriptor.Descriptor(
  name='CarStatus',
  full_name='CarStateProtocol.CarStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='telemetry', full_name='CarStateProtocol.CarStatus.telemetry', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='CarStateProtocol.CarStatus.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop', full_name='CarStateProtocol.CarStatus.stop', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CARSTATUS_TELEMETRY, _CARSTATUS_POSITION, ],
  enum_types=[
    _CARSTATUS_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=435,
)


_CARCOMMAND = _descriptor.Descriptor(
  name='CarCommand',
  full_name='CarStateProtocol.CarCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stops', full_name='CarStateProtocol.CarCommand.stops', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='CarStateProtocol.CarCommand.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CARCOMMAND_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=588,
)


_STOP = _descriptor.Descriptor(
  name='Stop',
  full_name='CarStateProtocol.Stop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='CarStateProtocol.Stop.to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=590,
  serialized_end=608,
)

_CARSTATUS_TELEMETRY.fields_by_name['position'].message_type = _CARSTATUS_POSITION
_CARSTATUS_TELEMETRY.containing_type = _CARSTATUS
_CARSTATUS_POSITION.containing_type = _CARSTATUS
_CARSTATUS.fields_by_name['telemetry'].message_type = _CARSTATUS_TELEMETRY
_CARSTATUS.fields_by_name['state'].enum_type = _CARSTATUS_STATE
_CARSTATUS.fields_by_name['stop'].message_type = _STOP
_CARSTATUS_STATE.containing_type = _CARSTATUS
_CARCOMMAND.fields_by_name['stops'].message_type = _STOP
_CARCOMMAND.fields_by_name['action'].enum_type = _CARCOMMAND_ACTION
_CARCOMMAND_ACTION.containing_type = _CARCOMMAND
DESCRIPTOR.message_types_by_name['CarStatus'] = _CARSTATUS
DESCRIPTOR.message_types_by_name['CarCommand'] = _CARCOMMAND
DESCRIPTOR.message_types_by_name['Stop'] = _STOP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CarStatus = _reflection.GeneratedProtocolMessageType('CarStatus', (_message.Message,), {

  'Telemetry' : _reflection.GeneratedProtocolMessageType('Telemetry', (_message.Message,), {
    'DESCRIPTOR' : _CARSTATUS_TELEMETRY,
    '__module__' : 'CarStateProtocol_pb2'
    # @@protoc_insertion_point(class_scope:CarStateProtocol.CarStatus.Telemetry)
    })
  ,

  'Position' : _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
    'DESCRIPTOR' : _CARSTATUS_POSITION,
    '__module__' : 'CarStateProtocol_pb2'
    # @@protoc_insertion_point(class_scope:CarStateProtocol.CarStatus.Position)
    })
  ,
  'DESCRIPTOR' : _CARSTATUS,
  '__module__' : 'CarStateProtocol_pb2'
  # @@protoc_insertion_point(class_scope:CarStateProtocol.CarStatus)
  })
_sym_db.RegisterMessage(CarStatus)
_sym_db.RegisterMessage(CarStatus.Telemetry)
_sym_db.RegisterMessage(CarStatus.Position)

CarCommand = _reflection.GeneratedProtocolMessageType('CarCommand', (_message.Message,), {
  'DESCRIPTOR' : _CARCOMMAND,
  '__module__' : 'CarStateProtocol_pb2'
  # @@protoc_insertion_point(class_scope:CarStateProtocol.CarCommand)
  })
_sym_db.RegisterMessage(CarCommand)

Stop = _reflection.GeneratedProtocolMessageType('Stop', (_message.Message,), {
  'DESCRIPTOR' : _STOP,
  '__module__' : 'CarStateProtocol_pb2'
  # @@protoc_insertion_point(class_scope:CarStateProtocol.Stop)
  })
_sym_db.RegisterMessage(Stop)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
