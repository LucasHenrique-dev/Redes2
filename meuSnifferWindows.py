import socket
import struct

from redes_functions.typeOfService import type_of_service
from redes_functions.totalLength import total_length
from redes_functions.flags import flags
from redes_functions.address import address

# PORTA IPV4 DA INTERNET (REDE SEM FIO)
local_ip = socket.gethostbyname(socket.gethostname())

# CRIA O SOCKET
soquete = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

# MONITORA OS DADOS DA INTERFACE ESCOLHIDA
soquete.bind((local_ip, 0))

# DEFINE AS OPTIONS (CRIA UM HEADER?)
soquete.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# DEFINE O MODO PROMISCUOUS
soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# COLETA OS DADOS
buffer = soquete.recv(2000)  # DADOS BRUTOS (QUANTIDADE: BYTES DO ARGUMENTO; 65536: MAIOR VALOR PARA UDP)
buffer_dados = list(buffer)  # DADOS EM LISTA (REALIZA O TRANSLATE DOS DADOS PARA O DECIMAL)

print(f"Dados Brutos:\n {buffer}")
# TRABALHAR COM LISTA -> DIFICULTA O DESEMPACOTAMENTO/MELHOR LEGIBILIDADE DOS DADOS
print(f"Dados em Decimal:\n {buffer_dados}\n")

print("*" * 50)
print("Dados do IP HEADER: ")
print(f"Version: {buffer[0] >> 4}")  # CAPTURA OS 4 PRIMEIROS BITS DO 1° BYTE
ip_header_len = buffer[0] & 0x0f  # CAPTURA OS 4 LAST BITS DO 1° BYTE
print(f"Header Length: {ip_header_len}")
print(f"    Existe(m): {ip_header_len - 5} options")
print(f"Type of Service: {buffer[1]}")  # DSCP? PESQUISAR MAIS
type_of_service(buffer[1])
total_length(buffer[2:4], ip_header_len)
print(f"ID: {struct.unpack('! H', buffer[4:6])[0]}")  # IDENTIFICA OS FRAGMENTOS DO DATAGRAMA IP
flags(buffer[6] >> 5)
print(f"Fragment Offset: {struct.unpack('! H', buffer[6:8])[0] & 0x1FFF}")  # ANALISAR MAIS (VALORES INTERNOS?)
print(f"Time to Live: {buffer[8]}")  # ANALISAR MAIS (VALORES INTERNOS?)
print(f"Protocol: {buffer[9]}")  # ANALISAR MAIS (VALORES INTERNOS?)
print(f"Header Checksum: {struct.unpack('! H', buffer[10:12])[0]}")  # ANALISAR MAIS (VALORES INTERNOS?)
address(buffer[12:16], 0, local_ip)   # SOURCE IGUAL AO DO PC -> ENVIO DE PACOTE
address(buffer[16:20], 1, local_ip)   # DESTINATION IGUAL AO DO PC -> RECEBIMENTO DE PACOTE
print("*" * 50)

# DESATIVA O MODO PROMISCUOUS
soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

# FECHA O SOCKET
soquete.close()
