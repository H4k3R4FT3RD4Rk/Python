def get_mac(ip):                                                                                                   
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast MAC
    arp_request_broadcast = broadcast/arp_request # combine the two varaibles (scapy allows us to do that) it is called packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print (answered_list[0][1].hwsrc)
    
ip="192.168.0.131"
print(get_mac)