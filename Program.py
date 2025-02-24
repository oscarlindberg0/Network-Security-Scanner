import nmap

# create scanner
scanner = nmap.PortScanner()

# target network to scan
target = "scanme.nmap.org"

# do a basic scan
scanner.scan(target)

# print scan results
for host in scanner.all_hosts():
    print("Host: ", host)
    print("State: ", scanner[host].state())
    for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)
        ports = scanner[host][proto].keys()
        for port in ports:
            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])