#config.py

import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="DNS sniffer")
    parser.add_argument('--iface', '-i', help="Interface to sniff (ej:wlo1)", default="wlo1", type=str)
    parser.add_argument('--source', '-s', help='IP source (target to sniff)', required=True)
    parser.add_argument('--protocol', '-pr', help='Protocol (default=UDP)', default="udp", type=str)
    parser.add_argument('--output-name', '-o', help='Output file', default="log_dns.txt", type=str)
    parser.add_argument('--port', '-p', help='Port', default=53, type=int)
    parser.add_argument('--domain-list', '-df', help="DNS list file", required=True)
    return parser.parse_args()

def get_iface():
    return 0
def build_filter(args):
    filter_list = []
    if args.source:
        filter_list.append(f'src host {args.source}')
        filter_list.append(f'port {args.port}')
    if args.protocol:
        filter_list.append(f'{args.protocol.lower()}')
    return " and ".join(filter_list)

