import whois

class Whois:
    # used for checking out a webpages details (ip adress for example)
    def lookup(self, webpage):
        return whois.whois(webpage)
