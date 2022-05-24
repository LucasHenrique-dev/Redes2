import socket
import time

port = 33434
ttl = 1
alvo = '200.133.2.18'

# alvo = input('Digite o endereco do alvo: ')
# ------------------------------------------------------------
# import dns.resolver as res

# rA = res.resolve('www.uol.com.br', 'A')
# xx = []
# for x in rA:
#     xx.append(x)
# print(xx)
# ------------------------------------------------------------------
while True:
    socket_recv = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    socket_recv.settimeout(5)
    socket_recv.bind(('', 0))

    socket_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    socket_sender.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    socket_sender.sendto(b'', (alvo, port))

    try:
        rcv = socket_recv.recvfrom(1024)
        aux = rcv
        rcv = rcv[0]
        addr = aux[1]
        print(rcv)

        # if ord(rcv[9]) == '1':
        print('Protocolo: ', rcv[9])
        print('TipoIcmp', rcv[20])  # deve ser 11
        print('CodIcmp', rcv[21])  # deve ser 0
        # print('IdIcmp', rcv[38], rcv[39])
        # print('SeqNo', rcv[40], rcv[41])
        print('Maquina remota: ', aux[1])

        if addr[0] == alvo or ttl > 30:
            break
        else:
            ttl += 1
            print('\nTTL: ', ttl)

    except socket.timeout:
        print('TIME OUT!!!')
        # socket_recv.close()
        # socket_sender.close()
        # exit()
    # break

socket_recv.close()
socket_sender.close()
