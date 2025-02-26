from colorama import Fore, Style

class Output:
    
    def print_results(self, type, input):

        # find the right output format
        match type:

            case "scan":
                for host in input.all_hosts():
                    print("Host: ", host)
                    print("State: ", input[host].state())
                    for proto in input[host].all_protocols():
                        print("Protocol: ", proto)
                        ports = input[host][proto].keys()
                        for port in ports:
                            print("Port: ", port, "State: ", input[host][proto][port]['state'])

            case "lookup":
                for dict in input:
                    print(f"{dict}: {input[dict]}")

            case _:
                print(Fore.RED + "print_results: invalid type" + Style.RESET_ALL)