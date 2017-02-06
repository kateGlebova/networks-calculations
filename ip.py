import ipaddress

class IPv4:

    def __init__ (self, ip):
        try:
            self.ip_int = int(ipaddress.IPv4Address(ip))
            self.ip_str = str(ipaddress.IPv4Address(ip))
        except:
            print('Invalid input')

    def __lt__ (self, ip_object):
        if isinstance(ip_object, IPv4):
            return self.ip_int < int(ip_object)

    def __gt__ (self, ip_object):
        if isinstance(ip_object, IPv4):
            return self.ip_int > int(ip_object)

    def __eq__ (self, ip_object):
        if isinstance(ip_object, IPv4):
            return self.ip_int == int(ip_object)

    def __int__(self):
        return self.ip_int

    def __str__(self):
        return self.ip_str
