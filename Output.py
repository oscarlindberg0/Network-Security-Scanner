from colorama import Fore, Style

class Output:

    def startup_image(self):
        print("""
            ########################################
            #                                      #
            #             PLACEHOLDER              #
            #                                      #
            ########################################
            """)

    def print_results(self, type, input):

        # find the right output format
        match type:

            # scan output
            case "scan":

                for host in input.all_hosts():
                    print("Host: ", host)
                    print("State: ", input[host].state())
                    print(f"{"PORT":<10}{"STATE":<12}{"SERVICE":<20}")
                    for proto in input[host].all_protocols():
                        ports = input[host][proto].keys()
                        for port in ports:
                            port_info = f"{port}/{proto}"
                            state = input[host][proto][port]["state"]
                            service = input[host][proto][port].get("name", "unknown")

                            print(f"{port_info:<10}{state:<12}{service:<20}")

            # lookup output
            case "lookup":
                for dict in input:
                    print(f"{dict + ":":<25} {input[dict]}")

            # wrong output format has been used to call the function
            case _:
                self.error("Script is broken, wrong output type")
                    
    # error generator
    def error(self, text):
        print(Fore.RED + "ERROR: " + Style.RESET_ALL + text)