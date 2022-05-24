import socket

ttl = 1
port = 33434
alvo = '8.8.8.8'

while True:
    # SOQUETE DE RECEBIMENTO DE PACOTE (RECEBE PACOTES ICMP)
    socket_recv = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    socket_recv.settimeout(2)  # ATIVA UM ERRO DEPOIS DE 2 SEGUNDOS DE ESPERA PELA RESPOSTA
    socket_recv.bind(('', port))

    # SOQUETE DE ENVIO DE PACOTE (ENVIA PACOTES UDP)
    socket_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # DEFINE AS OPTIONS DO HEADER (NESSE CASO TRABALHA COM PROTOCOLO IP E ALTERA O CAMPO TTL)
    socket_sender.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    # ENVIA UMA MENSAGEM (EM BYTES) PARA O "ALVO" NA PORTA "PORT"
    socket_sender.sendto(b'Hello World!', (alvo, port))

    print(f"TTL: {ttl}")

    try:
        addr, info = socket_recv.recvfrom(2000)
        print(f"ADDR: {addr}, info: {info}")
    except socket.error:
        socket_recv.close()
        socket_sender.close()
        print("TIME OUT!")

    if ttl > 10:
        break
    else:
        ttl += 1

socket_recv.close()
socket_sender.close()
print("Fim")
