#!/usr/bin/env python3

import socket
import time
# import dns.resolver as res
# import re

port = 33434
ttl = 0
# alvo = '200.133.2.18'
alvo = '200.133.2.18'
flag = False
# x = re.search("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", alvo)

# if x:
#     print("IP Address")
# else:
#     print("Domain Name: ", alvo)
#     rA = res.resolve(alvo, 'A')
#     for ipval in rA:
#         x = ipval.to_text()
# print('Endereco IP do alvo: ', x)
# alvo = input('Digite o endereco do alvo: ')
# alvo = input('Digite o dominio do alvo: ')
# ------------------------------------------------------------------
while True:
    ttl += 1
    print('\nTTL: ', ttl)
    socket_recv = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    socket_recv.settimeout(1)
    socket_recv.bind(('', 0))

    socket_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    socket_sender.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    # socket_sender.sendto(b'', (alvo, port))
    socket_sender.sendto(b'', (alvo, port))

    try:
        rcv = socket_recv.recvfrom(1024)
        data = rcv[0]
        addr = rcv[1]
        print('Data: ', data)

        # if ord(rcv[9]) == '1':
        print('Protocolo: ', data[9])
        print('TipoIcmp', data[20])  # deve ser 11
        print('CodIcmp', data[21])  # deve ser 0
        print('Maquina remota: ', addr[0])

        # print('\n', addr[0], ttl)
        # if addr[0] == x or ttl > 30:
        # break

        # print('\n', addr[0], ttl)
        if addr[0] == alvo:
            flag = True

    except socket.timeout:
        print('TIME OUT!!!')

    # print('\n', addr[0], ttl)
    if flag or ttl > 30:
        break

socket_recv.close()
socket_sender.close()
