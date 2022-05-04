import socket
import binascii
import os

# host to listen on
host = "192.168.1.68"   # PORTA IPV4 DA INTERNET (REDE SEM FIO)

# create a raw socket and bind it to the public interface
# VERIFICA O SISTEMA OPERACIONAL. "nt" INDICA O USO SISTEMA WINDOWS
##########################################################################
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP
##########################################################################

# CRIA UM SOCKET
##########################################################################
soquete = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
##########################################################################

# CAPTURA INFOS DE UMA DETERMINADA PORTA DE UMA INTERFACE ESCOLHIDA: BIND(INTERFACE, PORTA)
##########################################################################
soquete.bind((host, 0))
##########################################################################

# DEFINE AS OPTIONS DO SOCKET
#   IP_HDRINCL: GARANTE UM IP HEADER
##########################################################################
soquete.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
##########################################################################

# ATIVA O MODO PROMISCUOUS
##########################################################################
if os.name == "nt":
    soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
##########################################################################

# RECEBIMENTO DOS DADOS
##########################################################################
buffer = soquete.recv(2000)
##########################################################################

# AJUSTE DOS DADOS: FORMA BINARY
##########################################################################
print(f"DADOS:\n {buffer}\n\n")

hexa = binascii.hexlify(buffer)
inteiro = int(hexa, 16)
binario = bin(inteiro)
print(f"DADOS BINARIO: {binario[2:]}")
##########################################################################

# DESATIVA O MODO PROMISCUOUS
##########################################################################
if os.name == "nt":
    soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
##########################################################################

# FECHA O SOCKET
##########################################################################
soquete.close()
##########################################################################
