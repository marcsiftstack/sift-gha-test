# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sift.channel_schemas.v1 import channel_schemas_pb2 as sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2


class ChannelSchemaServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateChannelSchema = channel.unary_unary(
                '/sift.channel_schemas.v1.ChannelSchemaService/CreateChannelSchema',
                request_serializer=sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.CreateChannelSchemaRequest.SerializeToString,
                response_deserializer=sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.CreateChannelSchemaResponse.FromString,
                )
        self.BatchCreateChannelSchemas = channel.unary_unary(
                '/sift.channel_schemas.v1.ChannelSchemaService/BatchCreateChannelSchemas',
                request_serializer=sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.BatchCreateChannelSchemasRequest.SerializeToString,
                response_deserializer=sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.BatchCreateChannelSchemasResponse.FromString,
                )


class ChannelSchemaServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateChannelSchema(self, request, context):
        """Create a channel schema
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateChannelSchemas(self, request, context):
        """Create a batch of channel schemas
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChannelSchemaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateChannelSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateChannelSchema,
                    request_deserializer=sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.CreateChannelSchemaRequest.FromString,
                    response_serializer=sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.CreateChannelSchemaResponse.SerializeToString,
            ),
            'BatchCreateChannelSchemas': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreateChannelSchemas,
                    request_deserializer=sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.BatchCreateChannelSchemasRequest.FromString,
                    response_serializer=sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.BatchCreateChannelSchemasResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sift.channel_schemas.v1.ChannelSchemaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChannelSchemaService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateChannelSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.channel_schemas.v1.ChannelSchemaService/CreateChannelSchema',
            sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.CreateChannelSchemaRequest.SerializeToString,
            sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.CreateChannelSchemaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchCreateChannelSchemas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.channel_schemas.v1.ChannelSchemaService/BatchCreateChannelSchemas',
            sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.BatchCreateChannelSchemasRequest.SerializeToString,
            sift_dot_channel__schemas_dot_v1_dot_channel__schemas__pb2.BatchCreateChannelSchemasResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
