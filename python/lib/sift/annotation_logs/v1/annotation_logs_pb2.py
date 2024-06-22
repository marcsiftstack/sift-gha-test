# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sift/annotation_logs/v1/annotation_logs.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-sift/annotation_logs/v1/annotation_logs.proto\x12\x17sift.annotation_logs.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xa8\x03\n\x1a\x43reateAnnotationLogRequest\x12(\n\rannotation_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0c\x61nnotationId\x12\x43\n\x04kind\x18\x02 \x01(\x0e\x32*.sift.annotation_logs.v1.AnnotationLogKindB\x03\xe0\x41\x02R\x04kind\x12V\n\x08\x61ssigned\x18\x03 \x01(\x0b\x32\x38.sift.annotation_logs.v1.AnnotationLogAssignedPropertiesH\x00R\x08\x61ssigned\x12`\n\x0cstate_update\x18\x04 \x01(\x0b\x32;.sift.annotation_logs.v1.AnnotationLogStateUpdatePropertiesH\x00R\x0bstateUpdate\x12S\n\x07\x63omment\x18\x05 \x01(\x0b\x32\x37.sift.annotation_logs.v1.AnnotationLogCommentPropertiesH\x00R\x07\x63ommentB\x0c\n\nproperties\"x\n\x1b\x43reateAnnotationLogResponse\x12Y\n\x0e\x61nnotation_log\x18\x01 \x01(\x0b\x32\x32.sift.annotation_logs.v1.AnnotationLogSearchResultR\rannotationLog\"\xa8\x01\n\x19ListAnnotationLogsRequest\x12(\n\rannotation_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0c\x61nnotationId\x12 \n\tpage_size\x18\x02 \x01(\rB\x03\xe0\x41\x01R\x08pageSize\x12\"\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01R\tpageToken\x12\x1b\n\x06\x66ilter\x18\x04 \x01(\tB\x03\xe0\x41\x01R\x06\x66ilter\"\xa1\x01\n\x1aListAnnotationLogsResponse\x12[\n\x0f\x61nnotation_logs\x18\x01 \x03(\x0b\x32\x32.sift.annotation_logs.v1.AnnotationLogSearchResultR\x0e\x61nnotationLogs\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"w\n\x1a\x44\x65leteAnnotationLogRequest\x12(\n\rannotation_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0c\x61nnotationId\x12/\n\x11\x61nnotation_log_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x0f\x61nnotationLogId\"\x1d\n\x1b\x44\x65leteAnnotationLogResponse\"\xca\x05\n\x19\x41nnotationLogSearchResult\x12/\n\x11\x61nnotation_log_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0f\x61nnotationLogId\x12\x42\n\x0c\x63reated_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x02R\x0b\x63reatedDate\x12\x44\n\rmodified_date\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x02R\x0cmodifiedDate\x12(\n\rannotation_id\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x0c\x61nnotationId\x12\x43\n\x04kind\x18\x05 \x01(\x0e\x32*.sift.annotation_logs.v1.AnnotationLogKindB\x03\xe0\x41\x02R\x04kind\x12\x30\n\x12\x63reated_by_user_id\x18\x06 \x01(\tB\x03\xe0\x41\x02R\x0f\x63reatedByUserId\x12\x34\n\x14\x63reated_by_user_name\x18\x07 \x01(\tB\x03\xe0\x41\x02R\x11\x63reatedByUserName\x12V\n\x08\x61ssigned\x18\x08 \x01(\x0b\x32\x38.sift.annotation_logs.v1.AnnotationLogAssignedPropertiesH\x00R\x08\x61ssigned\x12`\n\x0cstate_update\x18\t \x01(\x0b\x32;.sift.annotation_logs.v1.AnnotationLogStateUpdatePropertiesH\x00R\x0bstateUpdate\x12S\n\x07\x63omment\x18\n \x01(\x0b\x32\x37.sift.annotation_logs.v1.AnnotationLogCommentPropertiesH\x00R\x07\x63ommentB\x0c\n\nproperties\"\x8f\x01\n\x1f\x41nnotationLogAssignedProperties\x12\x32\n\x13\x61ssigned_to_user_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x10\x61ssignedToUserId\x12\x38\n\x16\x61ssigned_to_user_email\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x13\x61ssignedToUserEmail\"l\n\"AnnotationLogStateUpdateProperties\x12\x46\n\x05state\x18\x01 \x01(\x0e\x32+.sift.annotation_logs.v1.AnnotationLogStateB\x03\xe0\x41\x02R\x05state\"k\n\x1e\x41nnotationLogCommentProperties\x12I\n\x04\x62ody\x18\x01 \x03(\x0b\x32\x35.sift.annotation_logs.v1.AnnotationCommentBodyElementR\x04\x62ody\"\xea\x01\n\x1c\x41nnotationCommentBodyElement\x12R\n\x04type\x18\x01 \x01(\x0e\x32\x39.sift.annotation_logs.v1.AnnotationCommentBodyElementTypeB\x03\xe0\x41\x02R\x04type\x12\x17\n\x04text\x18\x02 \x01(\tB\x03\xe0\x41\x01R\x04text\x12]\n\x0cuser_mention\x18\x03 \x01(\x0b\x32\x35.sift.annotation_logs.v1.AnnotationCommentUserMentionB\x03\xe0\x41\x01R\x0buserMention\"`\n\x1c\x41nnotationCommentUserMention\x12\x1c\n\x07user_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x06userId\x12\"\n\nuser_email\x18\x02 \x01(\tB\x03\xe0\x41\x02R\tuserEmail*\xa1\x01\n\x11\x41nnotationLogKind\x12#\n\x1f\x41NNOTATION_LOG_KIND_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x41NNOTATION_LOG_KIND_COMMENT\x10\x01\x12$\n ANNOTATION_LOG_KIND_STATE_UPDATE\x10\x02\x12 \n\x1c\x41NNOTATION_LOG_KIND_ASSIGNED\x10\x03*\xc0\x01\n\x12\x41nnotationLogState\x12$\n ANNOTATION_LOG_STATE_UNSPECIFIED\x10\x00\x12 \n\x1c\x41NNOTATION_LOG_STATE_CREATED\x10\x01\x12\x1d\n\x19\x41NNOTATION_LOG_STATE_OPEN\x10\x02\x12 \n\x1c\x41NNOTATION_LOG_STATE_FLAGGED\x10\x03\x12!\n\x1d\x41NNOTATION_LOG_STATE_RESOLVED\x10\x04*\xbe\x01\n AnnotationCommentBodyElementType\x12\x34\n0ANNOTATION_COMMENT_BODY_ELEMENT_TYPE_UNSPECIFIED\x10\x00\x12-\n)ANNOTATION_COMMENT_BODY_ELEMENT_TYPE_TEXT\x10\x01\x12\x35\n1ANNOTATION_COMMENT_BODY_ELEMENT_TYPE_USER_MENTION\x10\x02\x32\xe1\x07\n\x14\x41nnotationLogService\x12\xfa\x01\n\x13\x43reateAnnotationLog\x12\x33.sift.annotation_logs.v1.CreateAnnotationLogRequest\x1a\x34.sift.annotation_logs.v1.CreateAnnotationLogResponse\"x\x92\x41\x42\x12\x13\x43reateAnnotationLog\x1a+Creates an annotation log on an annotation.\x82\xd3\xe4\x93\x02-\"(/api/v1/annotations/{annotation_id}/logs:\x01*\x12\xfb\x01\n\x12ListAnnotationLogs\x12\x32.sift.annotation_logs.v1.ListAnnotationLogsRequest\x1a\x33.sift.annotation_logs.v1.ListAnnotationLogsResponse\"|\x92\x41I\x12\x12ListAnnotationLogs\x1a\x33Retrieves annotation logs using an optional filter.\x82\xd3\xe4\x93\x02*\x12(/api/v1/annotations/{annotation_id}/logs\x12\xfa\x01\n\x13\x44\x65leteAnnotationLog\x12\x33.sift.annotation_logs.v1.DeleteAnnotationLogRequest\x1a\x34.sift.annotation_logs.v1.DeleteAnnotationLogResponse\"x\x92\x41\x31\x12\x13\x44\x65leteAnnotationLog\x1a\x1a\x44\x65letes an annotation log.\x82\xd3\xe4\x93\x02>*</api/v1/annotations/{annotation_id}/logs/{annotation_log_id}\x1a\xd0\x01\x92\x41\xcc\x01\x12RService to programmatically interact with [annotation logs](/glossary#annotation).\x1av\n\x1cRead more about annotations.\x12Vhttps://customer.support.siftstack.com/servicedesk/customer/portal/2/article/265486685B\xef\x01\n\x1b\x63om.sift.annotation_logs.v1B\x13\x41nnotationLogsProtoP\x01ZAazimuth/gen/protos/go/sift/annotation_logs/v1;annotation_logsv1pb\xa2\x02\x03SAX\xaa\x02\x16Sift.AnnotationLogs.V1\xca\x02\x16Sift\\AnnotationLogs\\V1\xe2\x02\"Sift\\AnnotationLogs\\V1\\GPBMetadata\xea\x02\x18Sift::AnnotationLogs::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sift.annotation_logs.v1.annotation_logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.sift.annotation_logs.v1B\023AnnotationLogsProtoP\001ZAazimuth/gen/protos/go/sift/annotation_logs/v1;annotation_logsv1pb\242\002\003SAX\252\002\026Sift.AnnotationLogs.V1\312\002\026Sift\\AnnotationLogs\\V1\342\002\"Sift\\AnnotationLogs\\V1\\GPBMetadata\352\002\030Sift::AnnotationLogs::V1'
  _globals['_CREATEANNOTATIONLOGREQUEST'].fields_by_name['annotation_id']._loaded_options = None
  _globals['_CREATEANNOTATIONLOGREQUEST'].fields_by_name['annotation_id']._serialized_options = b'\340A\002'
  _globals['_CREATEANNOTATIONLOGREQUEST'].fields_by_name['kind']._loaded_options = None
  _globals['_CREATEANNOTATIONLOGREQUEST'].fields_by_name['kind']._serialized_options = b'\340A\002'
  _globals['_LISTANNOTATIONLOGSREQUEST'].fields_by_name['annotation_id']._loaded_options = None
  _globals['_LISTANNOTATIONLOGSREQUEST'].fields_by_name['annotation_id']._serialized_options = b'\340A\002'
  _globals['_LISTANNOTATIONLOGSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTANNOTATIONLOGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\340A\001'
  _globals['_LISTANNOTATIONLOGSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTANNOTATIONLOGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\340A\001'
  _globals['_LISTANNOTATIONLOGSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTANNOTATIONLOGSREQUEST'].fields_by_name['filter']._serialized_options = b'\340A\001'
  _globals['_DELETEANNOTATIONLOGREQUEST'].fields_by_name['annotation_id']._loaded_options = None
  _globals['_DELETEANNOTATIONLOGREQUEST'].fields_by_name['annotation_id']._serialized_options = b'\340A\002'
  _globals['_DELETEANNOTATIONLOGREQUEST'].fields_by_name['annotation_log_id']._loaded_options = None
  _globals['_DELETEANNOTATIONLOGREQUEST'].fields_by_name['annotation_log_id']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['annotation_log_id']._loaded_options = None
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['annotation_log_id']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['created_date']._loaded_options = None
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['created_date']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['modified_date']._loaded_options = None
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['modified_date']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['annotation_id']._loaded_options = None
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['annotation_id']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['kind']._loaded_options = None
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['kind']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['created_by_user_id']._loaded_options = None
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['created_by_user_id']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['created_by_user_name']._loaded_options = None
  _globals['_ANNOTATIONLOGSEARCHRESULT'].fields_by_name['created_by_user_name']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGASSIGNEDPROPERTIES'].fields_by_name['assigned_to_user_id']._loaded_options = None
  _globals['_ANNOTATIONLOGASSIGNEDPROPERTIES'].fields_by_name['assigned_to_user_id']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGASSIGNEDPROPERTIES'].fields_by_name['assigned_to_user_email']._loaded_options = None
  _globals['_ANNOTATIONLOGASSIGNEDPROPERTIES'].fields_by_name['assigned_to_user_email']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSTATEUPDATEPROPERTIES'].fields_by_name['state']._loaded_options = None
  _globals['_ANNOTATIONLOGSTATEUPDATEPROPERTIES'].fields_by_name['state']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONCOMMENTBODYELEMENT'].fields_by_name['type']._loaded_options = None
  _globals['_ANNOTATIONCOMMENTBODYELEMENT'].fields_by_name['type']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONCOMMENTBODYELEMENT'].fields_by_name['text']._loaded_options = None
  _globals['_ANNOTATIONCOMMENTBODYELEMENT'].fields_by_name['text']._serialized_options = b'\340A\001'
  _globals['_ANNOTATIONCOMMENTBODYELEMENT'].fields_by_name['user_mention']._loaded_options = None
  _globals['_ANNOTATIONCOMMENTBODYELEMENT'].fields_by_name['user_mention']._serialized_options = b'\340A\001'
  _globals['_ANNOTATIONCOMMENTUSERMENTION'].fields_by_name['user_id']._loaded_options = None
  _globals['_ANNOTATIONCOMMENTUSERMENTION'].fields_by_name['user_id']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONCOMMENTUSERMENTION'].fields_by_name['user_email']._loaded_options = None
  _globals['_ANNOTATIONCOMMENTUSERMENTION'].fields_by_name['user_email']._serialized_options = b'\340A\002'
  _globals['_ANNOTATIONLOGSERVICE']._loaded_options = None
  _globals['_ANNOTATIONLOGSERVICE']._serialized_options = b'\222A\314\001\022RService to programmatically interact with [annotation logs](/glossary#annotation).\032v\n\034Read more about annotations.\022Vhttps://customer.support.siftstack.com/servicedesk/customer/portal/2/article/265486685'
  _globals['_ANNOTATIONLOGSERVICE'].methods_by_name['CreateAnnotationLog']._loaded_options = None
  _globals['_ANNOTATIONLOGSERVICE'].methods_by_name['CreateAnnotationLog']._serialized_options = b'\222AB\022\023CreateAnnotationLog\032+Creates an annotation log on an annotation.\202\323\344\223\002-\"(/api/v1/annotations/{annotation_id}/logs:\001*'
  _globals['_ANNOTATIONLOGSERVICE'].methods_by_name['ListAnnotationLogs']._loaded_options = None
  _globals['_ANNOTATIONLOGSERVICE'].methods_by_name['ListAnnotationLogs']._serialized_options = b'\222AI\022\022ListAnnotationLogs\0323Retrieves annotation logs using an optional filter.\202\323\344\223\002*\022(/api/v1/annotations/{annotation_id}/logs'
  _globals['_ANNOTATIONLOGSERVICE'].methods_by_name['DeleteAnnotationLog']._loaded_options = None
  _globals['_ANNOTATIONLOGSERVICE'].methods_by_name['DeleteAnnotationLog']._serialized_options = b'\222A1\022\023DeleteAnnotationLog\032\032Deletes an annotation log.\202\323\344\223\002>*</api/v1/annotations/{annotation_id}/logs/{annotation_log_id}'
  _globals['_ANNOTATIONLOGKIND']._serialized_start=2672
  _globals['_ANNOTATIONLOGKIND']._serialized_end=2833
  _globals['_ANNOTATIONLOGSTATE']._serialized_start=2836
  _globals['_ANNOTATIONLOGSTATE']._serialized_end=3028
  _globals['_ANNOTATIONCOMMENTBODYELEMENTTYPE']._serialized_start=3031
  _globals['_ANNOTATIONCOMMENTBODYELEMENTTYPE']._serialized_end=3221
  _globals['_CREATEANNOTATIONLOGREQUEST']._serialized_start=219
  _globals['_CREATEANNOTATIONLOGREQUEST']._serialized_end=643
  _globals['_CREATEANNOTATIONLOGRESPONSE']._serialized_start=645
  _globals['_CREATEANNOTATIONLOGRESPONSE']._serialized_end=765
  _globals['_LISTANNOTATIONLOGSREQUEST']._serialized_start=768
  _globals['_LISTANNOTATIONLOGSREQUEST']._serialized_end=936
  _globals['_LISTANNOTATIONLOGSRESPONSE']._serialized_start=939
  _globals['_LISTANNOTATIONLOGSRESPONSE']._serialized_end=1100
  _globals['_DELETEANNOTATIONLOGREQUEST']._serialized_start=1102
  _globals['_DELETEANNOTATIONLOGREQUEST']._serialized_end=1221
  _globals['_DELETEANNOTATIONLOGRESPONSE']._serialized_start=1223
  _globals['_DELETEANNOTATIONLOGRESPONSE']._serialized_end=1252
  _globals['_ANNOTATIONLOGSEARCHRESULT']._serialized_start=1255
  _globals['_ANNOTATIONLOGSEARCHRESULT']._serialized_end=1969
  _globals['_ANNOTATIONLOGASSIGNEDPROPERTIES']._serialized_start=1972
  _globals['_ANNOTATIONLOGASSIGNEDPROPERTIES']._serialized_end=2115
  _globals['_ANNOTATIONLOGSTATEUPDATEPROPERTIES']._serialized_start=2117
  _globals['_ANNOTATIONLOGSTATEUPDATEPROPERTIES']._serialized_end=2225
  _globals['_ANNOTATIONLOGCOMMENTPROPERTIES']._serialized_start=2227
  _globals['_ANNOTATIONLOGCOMMENTPROPERTIES']._serialized_end=2334
  _globals['_ANNOTATIONCOMMENTBODYELEMENT']._serialized_start=2337
  _globals['_ANNOTATIONCOMMENTBODYELEMENT']._serialized_end=2571
  _globals['_ANNOTATIONCOMMENTUSERMENTION']._serialized_start=2573
  _globals['_ANNOTATIONCOMMENTUSERMENTION']._serialized_end=2669
  _globals['_ANNOTATIONLOGSERVICE']._serialized_start=3224
  _globals['_ANNOTATIONLOGSERVICE']._serialized_end=4217
# @@protoc_insertion_point(module_scope)