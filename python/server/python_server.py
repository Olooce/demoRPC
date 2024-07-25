from concurrent import futures
import grpc
import service.service_pb2 as service_pb2
import service.service_pb2_grpc as service_pb2_grpc

class ServiceServicer(service_pb2_grpc.ServiceServicer):
    def SayHello(self, request, context):
        response = service_pb2.HelloResponse(
            message=f"Hello, {request.name}"
        )
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServiceServicer_to_server(ServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
