import cmd, Scanner, Output

class CLI(cmd.Cmd):
    scanner = Scanner.Scanner()
    output = Output.Output()

    prompt = ">> "
    intro = output.startup_image()

    # constructor
    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)

    # pre command hook that is executed right before a command is run
    def precmd(self, line):
        return super().precmd(line)
    
    # post command hook after command is run
    def postcmd(self, stop, line):
        return super().postcmd(stop, line)



#########################################
#                                       #
#           CONSOLE COMMANDS            #
#                                       #
#########################################

    # help command
    def do_help(self, line):
        self.output.print_results("help", None)

    # scan command
    def do_scan(self, line):
        args = ""
        words = line.split()
        if not words:
            self.output.error("No target provided")
            return
        if len(words) > 1:
            args = words[1]

        self.output.print_results("scan", self.scanner.scan(words[0], args))

    # lookup command
    def do_lookup(self, line):
        if not line:
            self.output.error("No webaddress provided")
            return
        self.output.print_results("lookup", self.scanner.lookup(line))

    # device discovery command
    def do_devices(self, line):
        self.output.print_results("devices", self.scanner.discover_devices())

    # exit the CLI
    def do_quit(self, line):
        return True

#########################################
#                                       #
#        END OF CONSOLE COMMANDS        #
#                                       #
#########################################


    
    # cleanup before exit
    def postloop(self):
        return super().postloop()