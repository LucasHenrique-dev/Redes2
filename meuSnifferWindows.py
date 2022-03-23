import socket
from redes_functions.typeOfService import typeOfService

# PORTA IPV4 DA INTERNET (REDE SEM FIO)
local_ip = socket.gethostbyname(socket.gethostname())

# CRIA O SOCKET
soquete = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

# MONITORA OS DADOS DA INTERFACE ESCOLHIDA
soquete.bind((local_ip, 0))

# DEFINE AS OPTIONS (CRIA UM HEADER?)
# soquete.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# DEFINE O MODO PROMISCUOUS
soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# COLETA OS DADOS
buffer = soquete.recv(2000)  # DADOS BRUTOS
buffer_dados = list(buffer)  # DADOS EM LISTA?

print(buffer)
print(buffer_dados)

print("*" * 30)
print("Dados do IP HEADER: ")
print(f"Version: {buffer_dados[0] >> 4}")  # CAPTURA OS 4 PRIMEIROS BITS DO 1° BYTE
ip_header_len = buffer_dados[0] & 0x0f  # CAPTURA OS 4 LAST BITS DO 1° BYTE
print(f"Header Length: {ip_header_len}")
print(f"    Existe(m): {ip_header_len-5} options")
print(f"Type of Service: {buffer_dados[1]}")
typeOfService(buffer_dados[1])
print("*" * 30)

# DESATIVA O MODO PROMISCUOUS
soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

# FECHA O SOCKET
soquete.close()
