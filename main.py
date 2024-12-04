from scapy.all import *
from config import get_arguments, build_filter
from dns import sniffed_pkt
from utils import read_file

def main():
    args = get_arguments()

    if args.domain_list:
        domains_to_listen = read_file(args.domain_list)
    elif args.domain:
        domains_to_listen = [args.domain.strip().lower()]
    else:
        domains_to_listen = []

    filter_str = build_filter(args)

    sniff(iface=args.iface, filter=filter_str, prn=lambda pkt: sniffed_pkt(pkt, domains_to_listen, args))

if __name__ == "__main__":
    main()
