from Scanner import Scanner
from Output import Output

scanner = Scanner()
output = Output()

# target network to scan
target = "instagram.com"
args = ""

scans = scanner.scan(target, args)
lookup = scanner.lookup(target)

#output.print_results("scan", scans)
output.print_results("lookup", lookup)
