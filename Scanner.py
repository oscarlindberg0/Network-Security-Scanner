import nmap

class Scanner:
    def __init__(self):
        # create scanner
        self.scanner = nmap.PortScanner()

    def scan(self, target, args):

        # perform scan on target
        self.scanner.scan(target, arguments=args)

        # return scanned hosts
        return self.scanner