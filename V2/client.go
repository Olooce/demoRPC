package main

import (
	"fmt"
	"log"
	"net/rpc"
)

// Args defines the arguments structure for the RPC methods
type Args struct {
	A, B int
}

func main() {
	// Connect to the RPC server
	client, err := rpc.Dial("tcp", "localhost:5678")
	if err != nil {
		log.Fatalf("Error connecting to server: %v", err)
	}
	defer client.Close()

	// Define the arguments
	args := Args{A: 7, B: 8}
	var reply int

	// Call the Multiply method on the server
	err = client.Call("Arith.Multiply", args, &reply)
	if err != nil {
		log.Fatalf("Error calling Arith.Multiply: %v", err)
	}

	// Print the result
	fmt.Printf("The result of multiplying %d and %d is %d\n", args.A, args.B, reply)
}
