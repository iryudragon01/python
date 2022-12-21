from scapy.all import *
from scapy.utils import rdpcap
from time import sleep

pkts=rdpcap("ir.pcap")  # could be used like this rdpcap("filename",500) fetches first 500 pkts
sleep(5)
for pkt in pkts:
     #pkt[Ether].src= new_src_mac  # i.e new_src_mac="00:11:22:33:44:55"
     #pkt[Ether].dst= new_dst_mac
     #pkt[IP].src= new_src_ip # i.e new_src_ip="255.255.255.255"
     #pkt[IP].dst= new_dst_ip
     sendp(pkt) #sending packet at layer 2
     print(pkt[Ether].dst,pkt[IP].dst)