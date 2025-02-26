import nmap, whois

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