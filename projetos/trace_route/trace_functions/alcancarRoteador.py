import socket

from projetos.trace_route.trace_functions.criarSoqueteEnviar import criar_soquete_enviar
from projetos.trace_route.trace_functions.criarSoqueteReceber import criar_soquete_receber


def alcancar_rastreador(socket_recv, socket_sender, port, ttl, alvo):
    busca = ""
    finalizado = False

    for cont in range(3):
        try:
            info, (addr, _) = socket_recv.recvfrom(2000)

            if addr != "*":
                busca += addr
                finalizado = True
                break

        except socket.error:
            busca += "* "
        finally:
            socket_recv.close()
            socket_sender.close()

            if not finalizado:
                socket_recv, socket_sender = reenviar_mensagem(alvo, port, ttl)

    return busca, definir_addr(busca)


def reenviar_mensagem(alvo, port, ttl):
    socket_recv = criar_soquete_receber(port)
    socket_sender = criar_soquete_enviar(ttl)
    socket_sender.sendto(b'Hello World!', (alvo, port))

    return socket_recv, socket_sender


def definir_addr(busca):
    busca = busca.strip("* ")

    addr = "*" if busca == "" else busca

    return addr
