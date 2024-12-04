# DDNS_Qname_Sniffer
Shabby DDNS Sniffer matching QNAME from query packet


(WORK IN PROGRESS) #Works if target hasn't DNS over HTTPS (DoH) activated.

DNS packet sniffer matching queries matching QNAME. Scapy BASED (https://scapy.net/)

Requeriments: 
  ·Pythron 3.X
  ·pip / scapy


How to use: 

  options:
  -h, --help            show this help message and exit
  --iface, -i IFACE     Interface to sniff (ej:wlo1)
  --source, -s SOURCE   IP source (target to sniff) 
  --protocol, -pr PROTOCOL
                        Protocol (default=UDP)
  --output-name, -o OUTPUT_NAME #
                        Output file
  --domain-list, -df DOMAIN_LIST
                        DNS list file

