# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CarStateProtocol.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x43\x61rStateProtocol.proto\x12\x10\x43\x61rStateProtocol\"\x86\x03\n\tCarStatus\x12\x38\n\ttelemetry\x18\x01 \x01(\x0b\x32%.CarStateProtocol.CarStatus.Telemetry\x12\x30\n\x05state\x18\x02 \x01(\x0e\x32!.CarStateProtocol.CarStatus.State\x12$\n\x04stop\x18\x03 \x01(\x0b\x32\x16.CarStateProtocol.Stop\x1a`\n\tTelemetry\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x0c\n\x04\x66uel\x18\x02 \x01(\x01\x12\x36\n\x08position\x18\x03 \x01(\x0b\x32$.CarStateProtocol.CarStatus.Position\x1a\x41\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\"B\n\x05State\x12\x08\n\x04IDLE\x10\x00\x12\t\n\x05\x44RIVE\x10\x01\x12\x0b\n\x07IN_STOP\x10\x02\x12\x0c\n\x08OBSTACLE\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"\x96\x01\n\nCarCommand\x12%\n\x05stops\x18\x01 \x03(\x0b\x32\x16.CarStateProtocol.Stop\x12\x33\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32#.CarStateProtocol.CarCommand.Action\",\n\x06\x41\x63tion\x12\r\n\tNO_ACTION\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\t\n\x05START\x10\x02\"\x12\n\x04Stop\x12\n\n\x02to\x18\x01 \x01(\tB>Z!../internal/pkg/ba_proto;ba_proto\xaa\x02\x18Google.Protobuf.ba_protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CarStateProtocol_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z!../internal/pkg/ba_proto;ba_proto\252\002\030Google.Protobuf.ba_proto'
  _CARSTATUS._serialized_start=45
  _CARSTATUS._serialized_end=435
  _CARSTATUS_TELEMETRY._serialized_start=204
  _CARSTATUS_TELEMETRY._serialized_end=300
  _CARSTATUS_POSITION._serialized_start=302
  _CARSTATUS_POSITION._serialized_end=367
  _CARSTATUS_STATE._serialized_start=369
  _CARSTATUS_STATE._serialized_end=435
  _CARCOMMAND._serialized_start=438
  _CARCOMMAND._serialized_end=588
  _CARCOMMAND_ACTION._serialized_start=544
  _CARCOMMAND_ACTION._serialized_end=588
  _STOP._serialized_start=590
  _STOP._serialized_end=608
# @@protoc_insertion_point(module_scope)
