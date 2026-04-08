import socket

# server address and port 
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

# creating UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server address
server_add = (SERVER_HOST, SERVER_PORT)

# get user input 
message = input("Enter a word: ")
print(f'Your client program sends: "{message}"')

# sending message to server
client_socket.sendto(message.encode("ascii"), server_add)

# receive response from server
response, _ = client_socket.recvfrom(1024)
print(f'Your client program would receive the string: "{response.decode("ascii")}"')

# close socket
client_socket.close()