import random
import time
import socket
from datetime import datetime


class UDP_tx_rx_sim():

    def __init__(self):

        print("Give IP where to send traffic")
        self.targetHost = str(input())

        print("Give port to send:")
        self.listenPort = int(input())

        #Buffer size
        self.bufsize = 1536  # Modify to suit your needs

        #data packet to send
        self.data = b'From machine#1'
        # local packet counters
        self.t1_packets = 0
        self.L1_packets = 0

        #rem1
        self.rem1_ip = '0.0.0.0'
        self.rem1_port = 0

        self.sender(self.targetHost, self.listenPort, self.data)
        #self.listen(self.listenIP, self.listenPort)

    def sender(self, ip, port, data):
        UDP_IP = ip
        UDP_PORT = port
        MESSAGE = data
        now = datetime.now()
        time_tag = now.strftime('%H:%M:%S')

        sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP

        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        print(str(time_tag) + " - Sending data to: " + str(ip) + ":" + str(port) + " Packets Tx:" + str(self.t1_packets))
        self.t1_packets = self.t1_packets + 1
        port2 = str(sock)
        port2 = port2[-7:-2]
        tx_address = socket.gethostbyname_ex(socket.gethostname())[-1]
        ip_to_listen = self.local_ip_resolver(tx_address)
        self.listener(ip_to_listen, port2)

    def local_ip_resolver(self, to_ip, addr_list):
        ip_to_rtn = '0.0.0.0'
        ip_to_tx = to_ip
        get_last_dot = ip_to_tx.rfind('.')
        ip_to_comp = ip_to_tx[:get_last_dot]
        ip_addresses = addr_list

        for x in ip_addresses:
            get_last_dot = x.rfind('.')
            local_ip_to_comp = x[:get_last_dot]
            if local_ip_to_comp != ip_to_comp:
                continue
            else:
                ip_to_rtn = x

        return ip_to_rtn

    def listener(self, host, port):
        UDP_IP = host
        UDP_PORT = port

        sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP
        sock.bind((UDP_IP, UDP_PORT))

        while True:
            now = datetime.now()
            time_tag = now.strftime('%H:%M:%S')
            print(str(time_tag) + " - Listening " + str(UDP_IP) + ":" + str(UDP_PORT))
            data, addr = sock.recvfrom(self.bufsize)  # buffer size is set by bufsize
            self.L1_packets = self.L1_packets + 1
            print(str(time_tag) + " - " + str(UDP_IP) + ":" + str(UDP_PORT) + " Packets Rx:" + str(self.L1_packets))
            self.rem1_ip = addr[0]
            self.rem1_port = addr[1]
            # print("received message: %s" % data)
            #return data, addr[0], addr[1]
            self.sleeper()

    def sleeper(self):
        random_wait = random.randint(1,12)
        time.sleep(random_wait)
        self.sender(self.targetHost, self.listenPort, self.data)


UDP_tx_rx_sim()