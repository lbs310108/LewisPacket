import socket


# only support linux,
# interface: send interface label name.
# packet: byte string
# count: sent number
def main_procedure(interface, packet, count):
    sk = socket.socket(socket.PF_PACKET, socket.SOCK_RAW)
    sk.bind((interface, 0))
    number = 1
    if count == -1:
        while count == 1:
            sk.send(packet)
            print('send arp request packets for {} numbers'.format(number))
            number += 1
    else:
        while number <= count:
            sk.send(packet)
            print('send arp request packets for {} numbers'.format(number))
            number += 1
    exit()