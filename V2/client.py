import socket
import pickle

# Define the arguments and response formats
def pack_args(a, b):
    return pickle.dumps((a, b))

def unpack_response(response):
    return pickle.loads(response)

def main():
    # Create a socket to connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5678))

        # Define the arguments
        a = 7
        b = 8
        packed_args = pack_args(a, b)

        # Send the request
        s.sendall(b'Call Multiply' + b'\n' + packed_args)

        # Receive the response
        response = s.recv(4096)  # Adjust buffer size if needed
        result = unpack_response(response)

        # Print the result
        print(f'The result of multiplying {a} and {b} is {result}')

if __name__ == '__main__':
    main()
