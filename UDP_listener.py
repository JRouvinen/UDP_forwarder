import socket
from datetime import datetime

def local_listener(host, port):
    UDP_IP = host
    UDP_PORT = port
    bufsize = 1536

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        now = datetime.now()
        time_tag = now.strftime('%H:%M:%S')
        print(str(time_tag)+" - Listening " + str(UDP_IP) + ":" + str(UDP_PORT))
        data, addr = sock.recvfrom(bufsize) # buffer size is set by bufsize
        print(str(time_tag)+" - "+str(UDP_IP)+":"+str(UDP_PORT))
        #print("received message: %s" % data)
        return data, addr[0], addr[1]#Needs to be revorked -> addr0/1 has to be in variables


def remote_listener(host, port, bufsize):

    UDP_IP = host
    UDP_PORT = port
    bufsize = 1536

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        now = datetime.now()
        time_tag = now.strftime('%H:%M:%S')
        print(str(time_tag) + " - Listening " + str(UDP_IP) + ":" + str(UDP_PORT))
        data, addr = sock.recvfrom(bufsize)  # buffer size is set by bufsize
        print(str(time_tag) + " - " + str(UDP_IP) + ":" + str(UDP_PORT))
        # print("received message: %s" % data)
        return data, addr[0], addr[1]