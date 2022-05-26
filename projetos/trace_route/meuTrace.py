from trace_functions.procurarSite import procurar_site
from trace_functions.criarSoqueteReceber import criar_soquete_receber
from trace_functions.criarSoqueteEnviar import criar_soquete_enviar
from trace_functions.alcancarRoteador import alcancar_rastreador
from trace_functions.exibir_rota import exibir_rota

ttl = 1
port = 33434
rejeicoes = 0
enderecos = []

site, alvo = procurar_site()

print(f"Alvo: {site} ({alvo})")

print("-=" * 50, end='-\n')
while ttl <= 60:
    # CRIA SOQUETE DE RECEBIMENTO DE PACOTES (ICMP)
    socket_recv = criar_soquete_receber(port)

    # CRIA SOQUETE DE ENVIO DE PACOTES (UDP)
    socket_sender = criar_soquete_enviar(ttl)

    # ENVIA UMA MENSAGEM (EM BYTES) PARA O "ALVO" NA PORTA "PORT"
    socket_sender.sendto(b'Hello World!', (alvo, port))

    print(f"\nTTL: {ttl}")

    tentativas, addr = alcancar_rastreador(socket_recv, socket_sender, port, ttl, alvo)

    print(tentativas)

    if addr == "*":
        rejeicoes += 1
    else:
        rejeicoes = 0

    enderecos.append(addr)

    if rejeicoes >= 15:
        break

    if addr == alvo:
        break

    ttl += 1
print("-=" * 50, end='-\n\n')

try:
    exibir_rota(enderecos)
except Exception as erro:
    print(f"Houve um erro ao tentar rastrear a rota: {erro}")

print("\nFim do Rastreamento")
