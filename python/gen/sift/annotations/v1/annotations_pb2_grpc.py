# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sift.annotations.v1 import annotations_pb2 as sift_dot_annotations_dot_v1_dot_annotations__pb2


class AnnotationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAnnotation = channel.unary_unary(
                '/sift.annotations.v1.AnnotationService/CreateAnnotation',
                request_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.CreateAnnotationRequest.SerializeToString,
                response_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.CreateAnnotationResponse.FromString,
                )
        self.DeleteAnnotation = channel.unary_unary(
                '/sift.annotations.v1.AnnotationService/DeleteAnnotation',
                request_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.DeleteAnnotationRequest.SerializeToString,
                response_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.DeleteAnnotationResponse.FromString,
                )
        self.BatchDeleteAnnotations = channel.unary_unary(
                '/sift.annotations.v1.AnnotationService/BatchDeleteAnnotations',
                request_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.BatchDeleteAnnotationsRequest.SerializeToString,
                response_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.BatchDeleteAnnotationsResponse.FromString,
                )
        self.ListAnnotations = channel.unary_unary(
                '/sift.annotations.v1.AnnotationService/ListAnnotations',
                request_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.ListAnnotationsRequest.SerializeToString,
                response_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.ListAnnotationsResponse.FromString,
                )
        self.GetAnnotation = channel.unary_unary(
                '/sift.annotations.v1.AnnotationService/GetAnnotation',
                request_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.GetAnnotationRequest.SerializeToString,
                response_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.GetAnnotationResponse.FromString,
                )
        self.UpdateAnnotation = channel.unary_unary(
                '/sift.annotations.v1.AnnotationService/UpdateAnnotation',
                request_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.UpdateAnnotationRequest.SerializeToString,
                response_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.UpdateAnnotationResponse.FromString,
                )


class AnnotationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateAnnotation(self, request, context):
        """Creates an annotation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAnnotation(self, request, context):
        """Deletes an annotation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchDeleteAnnotations(self, request, context):
        """Batch deletes annotations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAnnotations(self, request, context):
        """Retrieves annotations using an optional filter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnnotation(self, request, context):
        """Retrieves an annotation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAnnotation(self, request, context):
        """Updates an existing annotation using using the list of fields specified in `update_mask`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnnotationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAnnotation': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAnnotation,
                    request_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.CreateAnnotationRequest.FromString,
                    response_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.CreateAnnotationResponse.SerializeToString,
            ),
            'DeleteAnnotation': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAnnotation,
                    request_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.DeleteAnnotationRequest.FromString,
                    response_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.DeleteAnnotationResponse.SerializeToString,
            ),
            'BatchDeleteAnnotations': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchDeleteAnnotations,
                    request_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.BatchDeleteAnnotationsRequest.FromString,
                    response_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.BatchDeleteAnnotationsResponse.SerializeToString,
            ),
            'ListAnnotations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAnnotations,
                    request_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.ListAnnotationsRequest.FromString,
                    response_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.ListAnnotationsResponse.SerializeToString,
            ),
            'GetAnnotation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnnotation,
                    request_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.GetAnnotationRequest.FromString,
                    response_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.GetAnnotationResponse.SerializeToString,
            ),
            'UpdateAnnotation': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAnnotation,
                    request_deserializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.UpdateAnnotationRequest.FromString,
                    response_serializer=sift_dot_annotations_dot_v1_dot_annotations__pb2.UpdateAnnotationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sift.annotations.v1.AnnotationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AnnotationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateAnnotation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.annotations.v1.AnnotationService/CreateAnnotation',
            sift_dot_annotations_dot_v1_dot_annotations__pb2.CreateAnnotationRequest.SerializeToString,
            sift_dot_annotations_dot_v1_dot_annotations__pb2.CreateAnnotationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAnnotation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.annotations.v1.AnnotationService/DeleteAnnotation',
            sift_dot_annotations_dot_v1_dot_annotations__pb2.DeleteAnnotationRequest.SerializeToString,
            sift_dot_annotations_dot_v1_dot_annotations__pb2.DeleteAnnotationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchDeleteAnnotations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.annotations.v1.AnnotationService/BatchDeleteAnnotations',
            sift_dot_annotations_dot_v1_dot_annotations__pb2.BatchDeleteAnnotationsRequest.SerializeToString,
            sift_dot_annotations_dot_v1_dot_annotations__pb2.BatchDeleteAnnotationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAnnotations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.annotations.v1.AnnotationService/ListAnnotations',
            sift_dot_annotations_dot_v1_dot_annotations__pb2.ListAnnotationsRequest.SerializeToString,
            sift_dot_annotations_dot_v1_dot_annotations__pb2.ListAnnotationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnnotation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.annotations.v1.AnnotationService/GetAnnotation',
            sift_dot_annotations_dot_v1_dot_annotations__pb2.GetAnnotationRequest.SerializeToString,
            sift_dot_annotations_dot_v1_dot_annotations__pb2.GetAnnotationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAnnotation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.annotations.v1.AnnotationService/UpdateAnnotation',
            sift_dot_annotations_dot_v1_dot_annotations__pb2.UpdateAnnotationRequest.SerializeToString,
            sift_dot_annotations_dot_v1_dot_annotations__pb2.UpdateAnnotationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
