import socket
from datetime import datetime

def interf1_sender(ip, port, data):

    UDP_IP = ip
    UDP_PORT = port
    MESSAGE = data
    now = datetime.now()
    time_tag = now.strftime('%H:%M:%S')

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP

    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print(str(time_tag) + " - Sending data to: " + str(ip) + ":" + str(port))
    port2 = str(sock)
    port2 = port2[-7:-2]
    tx_address = socket.gethostbyname_ex(socket.gethostname())[-1]

    return tx_address, port2


def interf2_sender(ip, port, data):
    UDP_IP = ip
    UDP_PORT = port
    MESSAGE = data
    now = datetime.now()
    time_tag = now.strftime('%H:%M:%S')

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print(str(time_tag) + " - Sending data to: " + str(ip) + ":" + str(port))
    port2 = str(sock)
    port2 = port2[-7:-2]
    tx_address = socket.gethostbyname_ex(socket.gethostname())[-1]

    return tx_address, port2