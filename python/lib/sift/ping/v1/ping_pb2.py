# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sift/ping/v1/ping.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17sift/ping/v1/ping.proto\x12\x0csift.ping.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\r\n\x0bPingRequest\"/\n\x0cPingResponse\x12\x1f\n\x08response\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x08response2b\n\x0bPingService\x12S\n\x04Ping\x12\x19.sift.ping.v1.PingRequest\x1a\x1a.sift.ping.v1.PingResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/v1/pingB\x82\x01\n\x10\x63om.sift.ping.v1B\tPingProtoP\x01\xa2\x02\x03SPX\xaa\x02\x0cSift.Ping.V1\xca\x02\x0cSift\\Ping\\V1\xe2\x02\x18Sift\\Ping\\V1\\GPBMetadata\xea\x02\x0eSift::Ping::V1\x92\x41\x10\x12\x0e\n\x0cPing Serviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sift.ping.v1.ping_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.sift.ping.v1B\tPingProtoP\001\242\002\003SPX\252\002\014Sift.Ping.V1\312\002\014Sift\\Ping\\V1\342\002\030Sift\\Ping\\V1\\GPBMetadata\352\002\016Sift::Ping::V1\222A\020\022\016\n\014Ping Service'
  _globals['_PINGRESPONSE'].fields_by_name['response']._loaded_options = None
  _globals['_PINGRESPONSE'].fields_by_name['response']._serialized_options = b'\340A\003'
  _globals['_PINGSERVICE'].methods_by_name['Ping']._loaded_options = None
  _globals['_PINGSERVICE'].methods_by_name['Ping']._serialized_options = b'\202\323\344\223\002\016\022\014/api/v1/ping'
  _globals['_PINGREQUEST']._serialized_start=152
  _globals['_PINGREQUEST']._serialized_end=165
  _globals['_PINGRESPONSE']._serialized_start=167
  _globals['_PINGRESPONSE']._serialized_end=214
  _globals['_PINGSERVICE']._serialized_start=216
  _globals['_PINGSERVICE']._serialized_end=314
# @@protoc_insertion_point(module_scope)