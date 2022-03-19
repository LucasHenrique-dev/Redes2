import socket
import binascii
# import os

# ret = os.system("ifconfig wlp2s0 promisc") QUAL A NECESSIDADE DE SE USAR ?
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))  # CRIA UM SOCKET

print("###########################################")
bf = s.recv(2000)   # RECEBE OS DADOS DO SOCKET
print(f"DADOS SOCKET:\n {bf} \n")
print("###########################################")
h = binascii.hexlify(bf)
print(f"DADOS EM HEXA:\n {h} \n")
# l = h.split(b'\n')  # [ , , ]  # PODE OMITIR
print("###########################################")
i = int(h, 16)
b = bin(i)
print(f"Resultado Final:\n {b[2:]}")  # 0b  # MOSTRA DADOS DO SOCKET EM BINARY
print("###########################################")
# print(f"Resultado Final:\n {bf.decode('utf-8')}")  # 0b  # MOSTRA DADOS DO SOCKET EM STRING

# ret = os.system("ifconfig wlp2s0 -promisc") AQUI ELE FECHA O DE CIMA
s.close()
