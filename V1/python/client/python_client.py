import grpc
import service.service_pb2 as service_pb2
import service.service_pb2_grpc as service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.ServiceStub(channel)
        response = stub.SayHello(service_pb2.HelloRequest(name='Python'))
        print("Server responded:", response.message)

if __name__ == '__main__':
    run()
