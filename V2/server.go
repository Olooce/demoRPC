package main

import (
	"fmt"
	"net"
	"net/rpc"
)

// Args defines the arguments structure for the RPC methods
type Args struct {
	A, B int
}

// Arith defines an arithmetic service with RPC methods
type Arith int

// Multiply is an RPC method that multiplies two integers
func (t *Arith) Multiply(args *Args, reply *int) error {
	*reply = args.A * args.B
	return nil
}

// main sets up the server and listens for RPC calls
func main() {
	arith := new(Arith)
	rpc.Register(arith)
	listener, err := net.Listen("tcp", ":5678")
	if err != nil {
		fmt.Println("Error listening:", err)
		return
	}
	defer listener.Close()
	fmt.Println("Server started, waiting for RPC calls...")
	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}
		go rpc.ServeConn(conn)
	}
}
