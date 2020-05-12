import netifaces
import struct
import socket

# variable
INTERFACE = 'lo'

# get local info
# local_network_detail = netifaces.ifaddresses(INTERFACE)
# local_ip_address = local_network_detail[2][0]['addr']
# local_mac_address = local_network_detail[17][0]['addr']
# bytes_local_mac_address = bytes.fromhex(local_mac_address.replace(':', ''))

# arp_hdr = struct.pack("!2s2s1s1s2s", b'\x00\x01', b'\x08\x00', b'\x06', b'\x04', b'\x00\x01')

# ethernet2
dist_mac = b'\xff\xff\xff\xff\xff\xff'
sour_mac = b'\xff\xff\xff\xff\xff\xff'
eth_type = b'\x00\x01'

arp_hdr = dist_mac + sour_mac + eth_type

sk = socket.socket(socket.PF_PACKET, socket.SOCK_RAW)
sk.bind((INTERFACE, 0))
sk.send(arp_hdr)

