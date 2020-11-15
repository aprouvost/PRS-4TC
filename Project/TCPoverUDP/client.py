import socket
import Project.TCPoverUDP.common as Common
import os

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

#Handshake
handshake_done = False
sock.sendto(Common.SYN, (Common.UDP_IP, Common.UDP_PORT_CONTROL)) # Send SYN
data, addr = sock.recvfrom(Common.BUFFER)
if data == Common.SYNACK + b" " + str(Common.UDP_PORT_DATA).encode('utf-8'):
    print(data)
    port_data = int(str(data).split(" ")[1][:-1])
    sock.sendto(Common.ACK, (Common.UDP_IP, Common.UDP_PORT_CONTROL))
    print(f"Received  {data}, sent  {Common.ACK}")
    handshake_done = True

else:
    print(f"Expected : {Common.SYNACK}, received : {data}")

print(f"Handshake {'done' if handshake_done else 'failed'}")


if handshake_done:
    while True:
        message = input("Enter a string : ").encode('utf-8')
        sock.sendto(message, (Common.UDP_IP, port_data))

        if message == Common.bonjour:
            data, addr = sock.recvfrom(Common.BUFFER)
            print(f"Server say : {data}")

        # client demande image au serveur
        if message == Common.sendimg:
            print("Send Nudes plz")
            cop = "copy_"
            file_name_received, addr = sock.recvfrom(Common.BUFFER)
            file_size, addr = sock.recvfrom(Common.BUFFER)
            file_name_received = cop +file_name_received
            #creating new file
            f = open(file_name_received, "x")






