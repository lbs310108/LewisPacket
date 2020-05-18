import netifaces
import socket
import argparse
from sys import exit

parse = argparse.ArgumentParser(description='send arp packet. using example: arp_sender -d ens10 -i 192.168.1.1 -n 10')
parse.add_argument('-p', type=str, help='linux interface label. eg: ens10')
parse.add_argument('-i', type=str, help='target ip address. eg: 192.168.1.1')
parse.add_argument('-n', type=int, help='send number,max 10.eg: 10', default=10)
args = parse.parse_args()

# variable
INTERFACE = args.p
IP = args.i
COUNT = args.n

# license
if COUNT > 10:
    print('license only support:max count 10')
    print('if you need unlimited count, Please contact us to buy for 10 RMB, qq:838648292')
    print('if you want to change source ip address to use arp snooping, '
          'Please contact us to buy for 50 RMB, qq:838648292')
    print('The program is only used to test the security of the network and cannot be used as a malicious attack')
    print('The author is for programming only, and shall not be liable!')
    exit()

# get local MAC and IP
local_network_detail = netifaces.ifaddresses(INTERFACE)
local_ip_address = local_network_detail[2][0]['addr']
local_mac_address = local_network_detail[17][0]['addr']
bytes_local_mac_address = bytes.fromhex(local_mac_address.replace(':', ''))
bytes_local_ip_address = socket.inet_aton(local_ip_address)
bytes_target_ip_address = socket.inet_aton(IP)

# define ethernet2 variable
bytes_dest_mac_address = b'\xff\xff\xff\xff\xff\xff'
byte_ethernet_type = b'\x08\x06'
fr_eth = bytes_dest_mac_address + bytes_local_mac_address + byte_ethernet_type

# define arp request header
hardware_type = b'\x00\x01'
protocol_type = b'\x08\x00'
hardware_size = b'\x06'
protocol_size = b'\x04'
opcode = b'\x00\x01'
arp_reqeust_header = hardware_type + protocol_type + hardware_size + protocol_size + opcode

# define arp body
sender_mac_address = bytes_local_mac_address
sender_ip_address = bytes_local_ip_address
target_mac_address = b'\00\00\00\00\00\00'
target_ip_address = bytes_target_ip_address
arp_reqest_body = sender_mac_address + sender_ip_address + target_mac_address + target_ip_address

# padding
padding = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# make arp request
arp_packet = fr_eth + arp_reqeust_header + arp_reqest_body + padding

if __name__ == '__main__':
    sk = socket.socket(socket.PF_PACKET, socket.SOCK_RAW)
    sk.bind((INTERFACE, 0))
    number = 1
    while number <= COUNT:
        sk.send(arp_packet)
        print('send arp request packets for {} numbers'.format(number))
        number += 1
        if number == 11:
            break
    print('license only support,max count 10')
    print('if you need unlimited count or , Please contact us to buy for 10 RMB, qq:838648292')
    print('if you want to change source ip address to use arp snooping, '
          'Please contact us to buy for 50 RMB, qq:838648292')
    print('The program is only used to test the security of the network and cannot be used as a malicious attack')
    print('The author is for programming only, and shall not be liable!')
