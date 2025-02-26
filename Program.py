from Scanner import Scanner

scanner = Scanner()

# target network to scan
target = "scanme.nmap.org"
args = ""

# print scan results
def print_results(scans):
    for host in scans.all_hosts():
        print("Host: ", host)
        print("State: ", scans[host].state())
        for proto in scans[host].all_protocols():
            print("Protocol: ", proto)
            ports = scans[host][proto].keys()
            for port in ports:
                print("Port: ", port, "State: ", scans[host][proto][port]['state'])

scans = scanner.scan(target, args)

print_results(scans)