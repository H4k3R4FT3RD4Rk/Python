import socket

def receive_message(client_socket):
    data = client_socket.recv(1024)
    return data.decode()

def send_message(client_socket, message):
    client_socket.sendall(message.encode())

def main():
    # Server address
    server_host = '167.71.38.236'
    server_port = 8080

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))

        # Receive the initial prompt from the server
        initial_prompt = receive_message(client_socket)
        print("Server says:", initial_prompt)

        # Your logic to process the server's prompt and formulate a response
        response = "Your response here"

        # Send your response to the server
        send_message(client_socket, response)

        # Receive and print the server's response to your answer
        server_response = receive_message(client_socket)
        print("Server says:", server_response)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
