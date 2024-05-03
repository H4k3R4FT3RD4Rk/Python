#!/usr/bin/python
#to trap all the requests in queue -- iptables -I OUTPUT -j NFQUEUE --queue-num 0 

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):         #check if the packet has dns 
        print(scapy_packet.show())
            
            
            
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


