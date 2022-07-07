#! /usr/bin/env python3

from scapy.all import *
from scapy.layers.dns import DNS
from pwn import *
import binascii

context.endian = 'big'
context.arch = 'x86'
shellcode = b''

#Gather data from C2 server in pcap
packets = rdpcap('capture.pcap')
for packet in packets:
    if packet.haslayer(DNS):
        for x in range (packet[DNS].ancount):
            
            #Check for AAAA records from wtf.lolasl.com
            if (packet[DNS].an[x].type == 28 and 'wtf.lolasl.com' in str(packet[DNS].an[x].rrname)):

                #Split IPV6 address to hex representation of the shellcode and XOR with the key (0x21) as found in the malicious executable
                for operation in packet[DNS].an[x].rdata.split(':'):
                    shellcode += p16(int(operation.encode(), 16) ^ 0x2121)                 
                  

#Disassemble shellcode to find offset for the pushstring
context.endian= 'little'
print(disasm(shellcode))
#seems like it starts at b'\xf7\xe1\xb0\x44\x50'

#Print shellcode from offset in reverse order as ascii to get the correct string
idx = shellcode.index(b'\xf7\xe1\xb0\x44\x50') + 5
pushoperations = [shellcode[i:i+5] for i in range(idx, idx+130, 5)]
for bytestring in pushoperations[::-1]:
    print(bytestring[1:].decode('ascii'), end='')
print()
