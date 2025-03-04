import nmap, whois, netifaces, ipaddress
from scapy.all import ARP, Ether, srp

class Scanner:

    def __init__(self):
        # create scanner
        self.scanner = nmap.PortScanner()


    def scan(self, target, args):

        # perform scan on target using input args
        self.scanner.scan(target, arguments=args)

        # return scanned hosts
        return self.scanner
    

    # used for checking out a webpages details (ip adress for example)
    def lookup(self, webpage):
        return whois.whois(webpage)
    
    # get local network
    def get_local_network(self):
        interfaces = netifaces.interfaces()

        for iface in interfaces:
            addrs = netifaces.ifaddresses(iface).get(netifaces.AF_INET)
            if addrs:
                for addr in addrs:
                    ip = addr['addr']
                    netmask = addr['netmask']
                    
                    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
                    return str(network)
    
    # device discovery for local network
    def discover_devices(self):

        network = self.get_local_network()

        # create request packet
        arp = ARP(pdst=network)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        # send packet and receive response
        result = srp(packet, timeout=2, verbose=False)[0]

        devices = []
        for sent, received in result:
            devices.append({"IP": received.psrc, "MAC": received.hwsrc})

        return devices