import socket


def criar_soquete_receber(port):
    # SOQUETE DE RECEBIMENTO DE PACOTE (RECEBE PACOTES ICMP)
    socket_recv = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    # ATIVA UM ERRO DEPOIS DE 3 SEGUNDOS DE ESPERA PELA RESPOSTA
    socket_recv.settimeout(3)

    socket_recv.bind(('', port))

    return socket_recv
