#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
    (options, argumenrs) = parser.parse_args()
    return options


def scan(ip):                                                                                                   
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #broadcast MAC
    arp_request_broadcast = broadcast/arp_request # combine the two varaibles (scapy allows us to do that) it is called packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #two varaibles to hold answered and unaswered data
    print("\n")
    print("                      :::!~!!!!!:.")
    print("                  .xUHWH!! !!?M88WHX:.")
    print("                .X*#M@$!!  !X!M$$$$$$WWx:.")
    print("               :!!!!!!?H! :!$!$$$$$$$$$$8X:")
    print("              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:")
    print("             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!")
    print("             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!")
    print("               !:~~~ .:!M'T#$$$$WX??#MRRMMM!")
    print("               ~?WuxiW*`   `'#$$$$8!!!!??!!!            ________________")
    print("             :X- M$$$$       `;T#$T~!8$WUXU~           |               |")
    print("            :%`  ~#$$$m:        ~!~ ?$$$$$$            |               |")
    print("          :!`.-   ~T$$$$8xx.  .xWW ~""##*%*              |   I SEE YOU!  |")
    print(".....   -~~:<` !    ~?T#$$@@W@*?$$      /`             |               |")
    print("W$@@M!!! .!~~ !!     .:XUW$W!~ `""~:     :               |_______________|")
    print("#""~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+`             -")
    print("##~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`         -")
    print(":::~:!!`:X~ .: ?H.!u #$$$B$$$!W:U!T$$M~      -")
    print(".~~   :X@!.-~   ?@WTWo('*$$$W$TH$! `      -")
    print("Wi.~!X$?!-~    : ?$$$B$Wu('**$RM!      -")
    print("$R@i.~~ !     :   ~$$$$$B$$en:``    - ")
    print("?MXT@Wx.~    :     ~##*$$$$M~")
    print("")
    
    
    
    
    #print(answered_list.summary())
    #poneje srp vrushta dva seta ot danni answered i unanswered packets shte gi kombinirame v 2 promenlivi
    
    
    clients_list = []
    for element in answered_list: #prints lists elements
        client_dict = {"ip":element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        return clients_list
        #print("---------------------------------------------------------------------------------")
    
    
#    print(arp_request_broadcast.summary())
#    arp_request_broadcast.show()                  # shows the whole content of the packet
#    scapy.ls(scapy.ARP())   list of all fields and description in APR (ls does that)
#    print(broadcast.summary())


def print_result(result_list):
    print("IP\t\t\tMAC Address\n---------------------------------------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()       
scan_result = scan(options.target)
print_result(scan_result)

