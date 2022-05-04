import socket

from sniffer_functions.detalharCabecalho import show_header

# PORTA IPV4 DA INTERNET (REDE SEM FIO)
local_ip = socket.gethostbyname(socket.gethostname())

# CRIA O SOCKET
soquete = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

# MONITORA OS DADOS DA INTERFACE ESCOLHIDA
soquete.bind((local_ip, 0))

# DEFINE AS OPTIONS
soquete.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# DEFINE O MODO PROMISCUOUS
soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# ARMAZENA OS FUTUROS PACOTES DE DADOS CAPTURADOS
pacotes = []
for cont in range(3):
    # COLETA OS DADOS
    pacotes.append(soquete.recv(2000))  # DADOS BRUTOS (QUANTIDADE: BYTES DO ARGUMENTO; 65536: MAIOR VALOR PARA UDP)

# EXIBE OS DADOS COLETADOS
for (pos, buffer) in enumerate(pacotes):
    print(f"{'-='*25}  {pos+1}° Pacote  {'=-'*25}")
    # TRABALHAR COM LISTA -> DIFICULTA O DESEMPACOTAMENTO/MELHOR LEGIBILIDADE DOS DADOS
    buffer_dados = list(buffer)  # DADOS EM LISTA (REALIZA O TRANSLATE DOS DADOS PARA O DECIMAL)

    print(f"Dados Brutos:\n {buffer}")
    print(f"Dados em Decimal:\n {buffer_dados}\n")

    # EXIBE OS VALORES DOS CAMPOS DO IP HEADER
    show_header(buffer, local_ip)

# DESATIVA O MODO PROMISCUOUS
soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

# FECHA O SOCKET
soquete.close()
