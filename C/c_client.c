#include <grpc/grpc.h>
#include <service.grpc.pb-c.h>

int main() {
    grpc_init();

    Service__HelloRequest request = SERVICE__HELLO_REQUEST__INIT;
    request.name = "C";

    grpc_channel *channel = grpc_insecure_channel_create("localhost:50051", NULL, NULL);
    grpc_completion_queue *cq = grpc_completion_queue_create_for_next(NULL);

    grpc_call *call = grpc_channel_create_call(channel, NULL, 0, cq, "/service.Service/SayHello", NULL, GRPC_TIMEOUT_SECONDS_TO_DEADLINE(10), NULL);

    grpc_metadata_array meta = grpc_metadata_array_create(NULL, 0);
    grpc_op ops[6];
    memset(ops, 0, sizeof(ops));

    ops[0].op = GRPC_OP_SEND_INITIAL_METADATA;
    ops[0].data.send_initial_metadata.count = 0;
    ops[0].flags = 0;
    ops[0].reserved = NULL;

    ops[1].op = GRPC_OP_SEND_MESSAGE;
    ops[1].data.send_message.send_message = service__hello_request__pack(&request, NULL);
    ops[1].flags = 0;
    ops[1].reserved = NULL;

    ops[2].op = GRPC_OP_SEND_CLOSE_FROM_CLIENT;
    ops[2].flags = 0;
    ops[2].reserved = NULL;

    grpc_call_start_batch(call, ops, 3, NULL, NULL);
    grpc_completion_queue_shutdown(cq);
    grpc_completion_queue_destroy(cq);
    grpc_channel_destroy(channel);
    grpc_shutdown();
    return 0;
}
