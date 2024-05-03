#!/usr/bin/python
#to trap all the requests in queue -- iptables -I OUTPUT -j NFQUEUE --queue-num 0 

import netfilterqueue
import scapy.all as scapy



def set_Load(packet, load):
    packet[scapy.Raw].load = load
    del scapy_packet[scapy.IP].len
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.TCP].chksum
    return packet
    
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())    
    if scapy_packet.haslayer(scapy.Raw):                                                    #check if the packet has dns
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request")
            print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            print(scapy_packet.show())                    


    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()



