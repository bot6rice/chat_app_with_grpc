# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto import messenger_pb2 as proto_dot_messenger__pb2


class MessengerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FetchMessage = channel.unary_stream(
                '/messsenger.Messenger/FetchMessage',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_messenger__pb2.MessageResponse.FromString,
                )
        self.PostMessage = channel.unary_unary(
                '/messsenger.Messenger/PostMessage',
                request_serializer=proto_dot_messenger__pb2.MessageRequest.SerializeToString,
                response_deserializer=proto_dot_messenger__pb2.MessageResponse.FromString,
                )


class MessengerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FetchMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessengerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FetchMessage': grpc.unary_stream_rpc_method_handler(
                    servicer.FetchMessage,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=proto_dot_messenger__pb2.MessageResponse.SerializeToString,
            ),
            'PostMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.PostMessage,
                    request_deserializer=proto_dot_messenger__pb2.MessageRequest.FromString,
                    response_serializer=proto_dot_messenger__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'messsenger.Messenger', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Messenger(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FetchMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/messsenger.Messenger/FetchMessage',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            proto_dot_messenger__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messsenger.Messenger/PostMessage',
            proto_dot_messenger__pb2.MessageRequest.SerializeToString,
            proto_dot_messenger__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
