from ip import *

class Network:

    def __init__ (self, address, mask):
        try:
            if not (isinstance(address, IPv4) and isinstance(mask, IPv4)):
                raise TypeError
            if not (int(address) | int(mask) == int(mask)):
                raise ValueError
            self.address = address
            self.mask = mask
        except TypeError:
            print('Wrong type of arguments')
        except ValueError:
            print('Wrong network address')

    def get_address_int(self):
        return int(self.address)

    def get_address_str(self):
        return str(self.address)

    def get_mask_int(self):
        return int(self.mask)

    def get_mask_str(self):
        return str(self.mask)

    def get_mask_length(self):
        return bin(int(self.mask)).count('1')

    def get_first_usable_address(self):
        return IPv4(int(self.address) + 1)

    def get_last_usable_address(self):
        return IPv4(int(self.get_broadcast_address()) - 1)

    def get_broadcast_address(self):
        return IPv4(int(self.address) + self.get_total_host() + 1)

    def contains(self, address):
        if isinstance(address, IPv4):
            return self.address < address < self.get_broadcast_address()

    def get_total_host(self):
        return 2**(32 - self.get_mask_length()) - 2

    def is_public(self):
        PRIVATE_1 = Network(IPv4('10.0.0.0'), IPv4('255.0.0.0'))
        PRIVATE_2 = Network(IPv4('172.16.0.0'), IPv4('255.240.0.0'))
        PRIVATE_3 = Network(IPv4('192.168.0.0'), IPv4('255.255.0.0'))

        if PRIVATE_1.contains(self.address) or PRIVATE_2.contains(self.address) or PRIVATE_3.contains(self.address):
            return False
        return True

    def subnets(self):
        new_mask = IPv4(int(self.mask) + 2**(31 - self.get_mask_length()))
        subnet1 = Network(self.address, new_mask)
        subnet2 = Network(IPv4(int(self.address) + 2**(31 - self.get_mask_length())), new_mask)
        return [subnet1, subnet2]

if __name__ == '__main__':
    network_mask = IPv4('255.255.248.0')
    network_address = IPv4('192.168.128.0')
    try:
        network = Network(network_address, network_mask)
        print(network.contains(IPv4('192.168.128.5')))
        print(network.contains(IPv4('192.168.5.5')))
        print(network.get_first_usable_address())
        print(network.get_last_usable_address())
        print(network.get_broadcast_address())
        print(network.get_total_host())
        print(network.is_public())
        for subnet in network.subnets():
            print(subnet.mask, subnet.address)
    except:
        pass
