import socket

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (same device → use 127.0.0.1)
client.connect(('127.0.0.1', 9999))

while True:
    msg = input("Enter any message: ")
    client.send(msg.encode())

    msg1 = client.recv(1024).decode()
    print("Server:", msg1)
