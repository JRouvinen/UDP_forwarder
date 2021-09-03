from socket import *
from datetime import datetime
from UDP_sender import *
from UDP_listener import *

class UDP_forwarder():

    def __init__(self):
        print("Give local IP address to listen:")
        #This is ip address of local interface #1
        #self.listenIP = str(input())
        self.interf_1 = '127.0.0.1'

        # This is ip address of local interface #2
        self.interf_2 = '127.0.0.1'
        self.interf_2_port = 0

        print("Give IP where to forward traffic from " + self.interf_1)
        #self.targetHost = str(input())
        self.targetHost = '211.130.10.145'

        print("Give port to listen/send:")
        #self.listenPort = int(input())
        self.listenPort = 50060

        #Buffer size
        self.bufsize = 1536  # Modify to suit your needs

        # local ip listen flag
        self.listen_local_ip = True

        #Local rx / tx packet counters

        #remote rx / tx packet counters

        #rem1
        self.rem1_ip = '0.0.0.0'
        self.rem1_port = 0

        self.listen()

    def forward(self, data):
        now = datetime.now()
        time_tag = now.strftime('%H:%M:%S')
        if not self.listen_local_ip:
            print(str(time_tag)+" - Forwarding from: "+str(self.rem1_ip)+" to "+str(self.targetHost))
            data = interf2_sender(self.targetHost, self.listenPort, data)
            local_ip_port = self.local_ip_resolver(self.targetHost, data)
            self.interf_2_port = int(local_ip_port[1])
            self.interf_2 = str(local_ip_port[0])
            self.listen()
        else:
            print(str(time_tag) + " - Forwarding from: " + str(self.targetHost) + " to " + str(self.rem1_ip))
            data = interf1_sender(self.rem1_ip, self.rem1_port, data)

    def listen(self):
        if self.listen_local_ip:
            data = local_listener(self.interf_1, self.listenPort)
        else:
            data = remote_listener(self.interf_2, self.interf_2_port)
        packet = data[0]
        if self.rem1_ip == '0.0.0.0':
            self.rem1_ip = data[1]
            self.rem1_port = data[2]
        if self.listen_local_ip:
            self.listen_local_ip = not self.listen_local_ip
            self.forward(packet)
        else:
            self.listen_local_ip = not self.listen_local_ip
            self.forward(packet)

    def local_ip_resolver(self, to_ip, data):
        ip_to_rtn = '0.0.0.0'
        ip_to_tx = to_ip
        get_last_dot = ip_to_tx.rfind('.')
        ip_to_comp = ip_to_tx[:get_last_dot]
        port = data[1]
        ip_addresses = data[0]

        for x in ip_addresses:
            get_last_dot = x.rfind('.')
            local_ip_to_comp = x[:get_last_dot]
            if local_ip_to_comp != ip_to_comp:
                continue
            else:
                ip_to_rtn = x

        return ip_to_rtn, port

UDP_forwarder()