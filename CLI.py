import cmd, Scanner, Output
from colorama import Fore, Style

class CLI(cmd.Cmd):
    scanner = Scanner.Scanner()
    output = Output.Output()

    prompt = ">> "
    intro = "här kommer det finnas lite schysst ascii art sen"

    # constructor
    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)

    # pre command hook that is executed right before a command is run
    def precmd(self, line):
        return super().precmd(line)
    
    # post command hook after command is run
    def postcmd(self, stop, line):
        return super().postcmd(stop, line)
    
    # error generator
    def error(self, text):
        print(Fore.RED + "ERROR: " + Style.RESET_ALL + text)



#########################################
#                                       #
#           CONSOLE COMMANDS            #
#                                       #
#########################################

    # help command
    def do_help(self, line):
        print("helptext")

    # scan command
    def do_scan(self, line):
        args = ""
        words = line.split()
        if not words:
            self.error("No target provided")
            return
        if len(words) > 1:
            args = words[1]

        self.output.print_results("scan", self.scanner.scan(words[0], args))

    # lookup command
    def do_lookup(self, line):
        if not line:
            self.error("No webaddress provided")
            return
        self.output.print_results("lookup", self.scanner.lookup(line))

#########################################
#                                       #
#        END OF CONSOLE COMMANDS        #
#                                       #
#########################################


    
    # cleanup before exit
    def postloop(self):
        return super().postloop()

    # exit the CLI
    def do_quit(self, line):
        return True