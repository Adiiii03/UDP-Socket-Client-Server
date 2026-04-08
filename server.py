import socket

# server address and port 
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

# creating UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binding socket to address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))
print(f"Server is running on {SERVER_HOST} : {SERVER_PORT}...")

# Keep the server running
while True:
    # receive message from client
    message, client_add = server_socket.recvfrom(1024)

    # decode message
    original = message.decode("ascii")
    print(f'Received from client: "{original}"')

    # create reply
    reply = original +  " - Why did the network packet break up with the router? Too many connections! :p"

    # send reply back to client
    server_socket.sendto(reply.encode("ascii"), client_add)

