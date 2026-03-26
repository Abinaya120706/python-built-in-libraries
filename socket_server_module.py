import socket

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to IP and port
server.bind(('0.0.0.0', 9999))

# Start listening
server.listen(1)
print("Waiting for Client !!")

# Accept connection
conn, addr = server.accept()
print("Connected with:", addr)

while True:
    msg = conn.recv(1024).decode()
    print("Client:", msg)

    reply = input("Enter your message: ")
    conn.send(reply.encode())
