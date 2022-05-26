import socket


def criar_soquete_enviar(ttl):
    # SOQUETE DE ENVIO DE PACOTE (ENVIA PACOTES UDP)
    socket_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # DEFINE AS OPTIONS DO HEADER (NESSE CASO TRABALHA COM PROTOCOLO IP E ALTERA O CAMPO TTL)
    socket_sender.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    return socket_sender
