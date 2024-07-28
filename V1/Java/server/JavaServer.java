import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import service.ServiceGrpc;
import service.HelloRequest;
import service.HelloResponse;

public class JavaServer extends ServiceGrpc.ServiceImplBase {
    @Override
    public void sayHello(HelloRequest request, StreamObserver<HelloResponse> responseObserver) {
        HelloResponse response = HelloResponse.newBuilder()
            .setMessage("Hello, " + request.getName())
            .build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    public static void main(String[] args) throws Exception {
        Server server = ServerBuilder.forPort(50051)
            .addService(new JavaServer())
            .build()
            .start();
        server.awaitTermination();
    }
}
