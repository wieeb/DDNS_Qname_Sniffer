# dns.py
from datetime import datetime
from scapy.all import DNSQR, IP, UDP

def sniffed_pkt(pkt, domains_to_listen, args):
    if DNSQR in pkt:
        qname = pkt[DNSQR].qname.decode().strip()
        packet_time = datetime.fromtimestamp(pkt.time)
        timestamp_str = packet_time.strftime("%Y-%m-%d %H:%M:%S")
        qname_normalized = qname.lower().rstrip('.')
        if any(qname_normalized.endswith(domain.lower()) for domain in domains_to_listen):
            print(f"DNS Query Detected for Domain: {qname}")
            write_data(pkt, timestamp_str, args)
def write_data(pkt, timestamp, args):
    src_ip = pkt[IP].src
    dst_ip = pkt[IP].dst
    pkt_len = pkt[IP].len
    dst_port = pkt[UDP].dport
    qname = pkt[DNSQR].qname.decode().strip()
    with open(args.output_name, 'a') as file:
        file.write(f"\n# Timestamp: {timestamp} # Source IP: {src_ip} # DNS Server: {dst_ip} # Domain: {qname} "
                   f"# Packet Length: {pkt_len} # Destination Port: {dst_port}\n")
