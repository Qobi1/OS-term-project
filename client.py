import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)  # Replace with the server's IP address and port number
client_socket.connect(server_address)

# Send a message to the server
message = "Hello from Python!"
client_socket.send(message.encode())

# Receive a response from the server
response = client_socket.recv(1024)
print(f"Received response: {response.decode()}")

# Close the socket
client_socket.close()
