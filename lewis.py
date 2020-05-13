import netifaces
import socket

# variable
INTERFACE = 'lo'

# get local MAC and IP
local_network_detail = netifaces.ifaddresses(INTERFACE)
local_ip_address = local_network_detail[2][0]['addr']
local_mac_address = local_network_detail[17][0]['addr']
bytes_local_mac_address = bytes.fromhex(local_mac_address.replace(':', ''))
bytes_local_ip_address = bytes.fromhex(local_ip_address.replace('.', ''))

# define ethernet2 variable
bytes_dest_mac_address = b'\xff\xff\xff\xff\xff\xff'
byte_ethernet_type = b'\x08\x06'
fr_eth = bytes_dest_mac_address + bytes_local_mac_address + byte_ethernet_type

# define arp request header
hardware_type = b'\x01\x00'
protocol_type = b'\x08\x00'
hardware_size = b'\x06'
protocol_size = b'\x04'
opcode = b'\x00\x01'
arp_reqeust_header = hardware_type + protocol_type + hardware_size + protocol_size + opcode

# make arp request
arp_packet = fr_eth + arp_reqeust_header

sk = socket.socket(socket.PF_PACKET, socket.SOCK_RAW)
sk.bind((INTERFACE, 0))
sk.send(arp_packet)

