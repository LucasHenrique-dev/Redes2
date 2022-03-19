import socket
import binascii
import os

# host to listen on
host = "192.168.1.68"   # PORTA IPV4 DA INTERNET (REDE SEM FIO)

# create a raw socket and bind it to the public interface
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

# CRIA UM SOCKET
##########################################################################
soquete = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
##########################################################################

# CAPTURA INFOS DE UMA PORTA ESPECÍFICA DE UMA INTERFACE ESPECÍFICA: BIND(INTERFACE, PORTA)
##########################################################################
soquete.bind((host, 0))
##########################################################################

soquete.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
    soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

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

# A DESVENDAR (ALGO SOBRE REMOVER O PORMISCUO)
##########################################################################
if os.name == "nt":
    soquete.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
##########################################################################

# FECHA O SOCKET
##########################################################################
soquete.close()
##########################################################################
