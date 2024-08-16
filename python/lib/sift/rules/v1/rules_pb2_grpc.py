# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sift.rules.v1 import rules_pb2 as sift_dot_rules_dot_v1_dot_rules__pb2


class RuleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchRules = channel.unary_unary(
                '/sift.rules.v1.RuleService/SearchRules',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.SearchRulesRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.SearchRulesResponse.FromString,
                )
        self.GetRule = channel.unary_unary(
                '/sift.rules.v1.RuleService/GetRule',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleResponse.FromString,
                )
        self.BatchGetRules = channel.unary_unary(
                '/sift.rules.v1.RuleService/BatchGetRules',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRulesRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRulesResponse.FromString,
                )
        self.CreateRule = channel.unary_unary(
                '/sift.rules.v1.RuleService/CreateRule',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.CreateRuleRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.CreateRuleResponse.FromString,
                )
        self.UpdateRule = channel.unary_unary(
                '/sift.rules.v1.RuleService/UpdateRule',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateRuleRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateRuleResponse.FromString,
                )
        self.DeleteRule = channel.unary_unary(
                '/sift.rules.v1.RuleService/DeleteRule',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.DeleteRuleRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.DeleteRuleResponse.FromString,
                )
        self.EvaluateRules = channel.unary_unary(
                '/sift.rules.v1.RuleService/EvaluateRules',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.EvaluateRulesRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.EvaluateRulesResponse.FromString,
                )
        self.ViewHumanFriendlyRules = channel.unary_unary(
                '/sift.rules.v1.RuleService/ViewHumanFriendlyRules',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.ViewHumanFriendlyRulesRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.ViewHumanFriendlyRulesResponse.FromString,
                )
        self.ViewJsonRules = channel.unary_unary(
                '/sift.rules.v1.RuleService/ViewJsonRules',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.ViewJsonRulesRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.ViewJsonRulesResponse.FromString,
                )
        self.UpdateHumanFriendlyRules = channel.unary_unary(
                '/sift.rules.v1.RuleService/UpdateHumanFriendlyRules',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateHumanFriendlyRulesRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateHumanFriendlyRulesResponse.FromString,
                )
        self.ValidateJsonRules = channel.unary_unary(
                '/sift.rules.v1.RuleService/ValidateJsonRules',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.ValidateJsonRulesRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.ValidateJsonRulesResponse.FromString,
                )
        self.UpdateJsonRules = channel.unary_unary(
                '/sift.rules.v1.RuleService/UpdateJsonRules',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateJsonRulesRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateJsonRulesResponse.FromString,
                )
        self.ListRuleVersions = channel.unary_unary(
                '/sift.rules.v1.RuleService/ListRuleVersions',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.ListRuleVersionsRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.ListRuleVersionsResponse.FromString,
                )
        self.GetRuleVersion = channel.unary_unary(
                '/sift.rules.v1.RuleService/GetRuleVersion',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleVersionRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleVersionResponse.FromString,
                )
        self.BatchGetRuleVersions = channel.unary_unary(
                '/sift.rules.v1.RuleService/BatchGetRuleVersions',
                request_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRuleVersionsRequest.SerializeToString,
                response_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRuleVersionsResponse.FromString,
                )


class RuleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SearchRules(self, request, context):
        """Queries rules based on provided search parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRule(self, request, context):
        """Retrieves the latest version of a rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetRules(self, request, context):
        """Retrieve multiple rules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRule(self, request, context):
        """Creates a rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRule(self, request, context):
        """Updates an existing rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRule(self, request, context):
        """Deletes a rule
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EvaluateRules(self, request, context):
        """Evaluates the provided rules and generate annotations based on the result.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViewHumanFriendlyRules(self, request, context):
        """Deprecated - use ViewJsonRules instead. Retrieve a JSON object containing all of the rules for a given asset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViewJsonRules(self, request, context):
        """Retrieve a JSON object containing all of the rules for a given asset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateHumanFriendlyRules(self, request, context):
        """Deprecated - use UpdateJsonRules instead. Batch update rules given the `rules_json` which is a JSON list of rules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateJsonRules(self, request, context):
        """Validate a batch update for rules given the `rules_json` which is a JSON list of rules. This is a dry-run operation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateJsonRules(self, request, context):
        """Batch update rules given the `rules_json` which is a JSON list of rules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRuleVersions(self, request, context):
        """Retrieves a list of rule versions for the given rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRuleVersion(self, request, context):
        """Retrieves a specific version of a rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetRuleVersions(self, request, context):
        """Retrieves multiple rules by rule versions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RuleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchRules': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchRules,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.SearchRulesRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.SearchRulesResponse.SerializeToString,
            ),
            'GetRule': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRule,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleResponse.SerializeToString,
            ),
            'BatchGetRules': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetRules,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRulesRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRulesResponse.SerializeToString,
            ),
            'CreateRule': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRule,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.CreateRuleRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.CreateRuleResponse.SerializeToString,
            ),
            'UpdateRule': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRule,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateRuleRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateRuleResponse.SerializeToString,
            ),
            'DeleteRule': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRule,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.DeleteRuleRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.DeleteRuleResponse.SerializeToString,
            ),
            'EvaluateRules': grpc.unary_unary_rpc_method_handler(
                    servicer.EvaluateRules,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.EvaluateRulesRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.EvaluateRulesResponse.SerializeToString,
            ),
            'ViewHumanFriendlyRules': grpc.unary_unary_rpc_method_handler(
                    servicer.ViewHumanFriendlyRules,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.ViewHumanFriendlyRulesRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.ViewHumanFriendlyRulesResponse.SerializeToString,
            ),
            'ViewJsonRules': grpc.unary_unary_rpc_method_handler(
                    servicer.ViewJsonRules,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.ViewJsonRulesRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.ViewJsonRulesResponse.SerializeToString,
            ),
            'UpdateHumanFriendlyRules': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateHumanFriendlyRules,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateHumanFriendlyRulesRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateHumanFriendlyRulesResponse.SerializeToString,
            ),
            'ValidateJsonRules': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateJsonRules,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.ValidateJsonRulesRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.ValidateJsonRulesResponse.SerializeToString,
            ),
            'UpdateJsonRules': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateJsonRules,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateJsonRulesRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.UpdateJsonRulesResponse.SerializeToString,
            ),
            'ListRuleVersions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRuleVersions,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.ListRuleVersionsRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.ListRuleVersionsResponse.SerializeToString,
            ),
            'GetRuleVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRuleVersion,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleVersionRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleVersionResponse.SerializeToString,
            ),
            'BatchGetRuleVersions': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetRuleVersions,
                    request_deserializer=sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRuleVersionsRequest.FromString,
                    response_serializer=sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRuleVersionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sift.rules.v1.RuleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RuleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/SearchRules',
            sift_dot_rules_dot_v1_dot_rules__pb2.SearchRulesRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.SearchRulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/GetRule',
            sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchGetRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/BatchGetRules',
            sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRulesRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/CreateRule',
            sift_dot_rules_dot_v1_dot_rules__pb2.CreateRuleRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.CreateRuleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/UpdateRule',
            sift_dot_rules_dot_v1_dot_rules__pb2.UpdateRuleRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.UpdateRuleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/DeleteRule',
            sift_dot_rules_dot_v1_dot_rules__pb2.DeleteRuleRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.DeleteRuleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EvaluateRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/EvaluateRules',
            sift_dot_rules_dot_v1_dot_rules__pb2.EvaluateRulesRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.EvaluateRulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ViewHumanFriendlyRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/ViewHumanFriendlyRules',
            sift_dot_rules_dot_v1_dot_rules__pb2.ViewHumanFriendlyRulesRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.ViewHumanFriendlyRulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ViewJsonRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/ViewJsonRules',
            sift_dot_rules_dot_v1_dot_rules__pb2.ViewJsonRulesRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.ViewJsonRulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateHumanFriendlyRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/UpdateHumanFriendlyRules',
            sift_dot_rules_dot_v1_dot_rules__pb2.UpdateHumanFriendlyRulesRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.UpdateHumanFriendlyRulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateJsonRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/ValidateJsonRules',
            sift_dot_rules_dot_v1_dot_rules__pb2.ValidateJsonRulesRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.ValidateJsonRulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateJsonRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/UpdateJsonRules',
            sift_dot_rules_dot_v1_dot_rules__pb2.UpdateJsonRulesRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.UpdateJsonRulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRuleVersions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/ListRuleVersions',
            sift_dot_rules_dot_v1_dot_rules__pb2.ListRuleVersionsRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.ListRuleVersionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRuleVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/GetRuleVersion',
            sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleVersionRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.GetRuleVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchGetRuleVersions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sift.rules.v1.RuleService/BatchGetRuleVersions',
            sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRuleVersionsRequest.SerializeToString,
            sift_dot_rules_dot_v1_dot_rules__pb2.BatchGetRuleVersionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
