# DDNS_Qname_Sniffer

**Shabby DDNS Sniffer matching QNAME from query packet**

**(WORK IN PROGRESS)**  
_# Works if target hasn't DNS over HTTPS (DoH) activated._

DNS packet sniffer that matches queries matching QNAME. Based on **Scapy** (https://scapy.net/).

---

### Requirements:
  - **Python 3.x**
  - **pip / scapy**

---

### How to Use:

Run the script with the following options:

  --iface, -i IFACE     Interface to sniff (ej:wlo1)
  --source, -s SOURCE   IP source (target to sniff)
  --protocol, -pr PROTOCOL
                        Protocol (default=UDP)
  --output-name, -o OUTPUT_NAME
                        Output file
  --port, -p PORT       Port
  --domain-list, -df DOMAIN_LIST
                        DNS list file

