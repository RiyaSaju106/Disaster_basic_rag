# import socket

# server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)  # RFCOMM specific protocol
# server.bind(("38:ba:f8:18:ac:e4", 4))  # MAC Address and Channel 4
# server.listen(1)

# print("Waiting for connection...")

# client, addr = server.accept()
# print(f"Accepted connection from {addr}")

# try:
#     while True:
#         data = client.recv(1024)
#         if not data:
#             break
#         # print(f"Received: {data.decode('utf-8')}")


#         message = "Hello from server"
#         client.send(message.encode('utf-8'))
#         print("Message sent to client")


#         message = input("Enter message: ")
#         client.send(message.encode('utf-8'))
# except OSError:
#     pass

# print("Disconnected")

# client.close()
# server.close()


import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("38:ba:f8:18:ac:e4", 2))
server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()
print(f"Accepted connection from {addr}")

try:
    while True:
        data = client.recv(1024)
        if not data:
            print("No data received, breaking...")
            break
        print(f"Received: {data.decode('utf-8')}")
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
except OSError as e:
    print(f"Error: {e}")

print("Disconnected")
client.close()
server.close()
