#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, struct, binascii

# prepara socket e conecta a interface ether
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind(('enp1s0', 0))
# s.getsockname

# atribui valor a campos do cabecalho Ethernet
McDest1 = 0xFF
McDest2 = 0xFF
McDest3 = 0xFF
McDest4 = 0xFF
McDest5 = 0xFF
McDest6 = 0xFF
# EMcO = 00:23:5a:63:c1:a8 (do meu Notebook Acer, RJ45)
McOrig1 = 0x00
McOrig2 = 0x23
McOrig3 = 0x5a
McOrig4 = 0x63
McOrig5 = 0xc1
McOrig6 = 0xa8
# Pay-load é IP
Tipo1 = 0x08
Tipo2 = 0x00

# atribui valor a campos do cabeçalho IP
Version = 4 << 4
HdrLen = 5
VH = Version + HdrLen
ToS = 0
LenIP = 28
LenIPe = (LenIP & 0xFF00) >> 8
LenIPd = (LenIP & 0xFF)
PktID = 0
PktIDe = (PktID & 0xFF00) >> 8
PktIDd = (PktID & 0xFF)
FlagOff = 0  # flags e offset
FlagOffe = (FlagOff & 0xFF00) >> 8
FlagOffd = (FlagOff & 0xFF)
TTL = int(input(b'Digite o TTL pretendido: '))
Proto = 1
TtlProto = TTL << 8 + Proto
ChkIP = 0  # = 0 para cálculo do checksum (no final)

# Pega endereço IP de origem (EIPO)
saux = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
saux.connect(('8.8.8.8', 53))
EIPO = saux.getsockname()[0]
print('Endereço IP atual ', EIPO)

EIPO = EIPO.split('.')
EIPO0 = int(EIPO[0])
EIPO1 = int(EIPO[1])
EIPOe = (EIPO0 << 8) + EIPO1  # Usado para cálculo do checksum
EIPO2 = int(EIPO[2])
EIPO3 = int(EIPO[3])
EIPOd = (EIPO2 << 8) + EIPO3  # Usado para cálculo do checksum
EIPD = input('Digite end. IP, destino: ')
EIPD = EIPD.split('.')
EIPD0 = int(EIPD[0])
EIPD1 = int(EIPD[1])
EIPDe = (EIPD0 << 8) + EIPD1  # Usado para cálculo do checksum
EIPD2 = int(EIPD[2])
EIPD3 = int(EIPD[3])
EIPDd = (EIPD2 << 8) + EIPD3  # Usado para cálculo do checksum

SUM = 0
SUM = SUM + TtlProto
if SUM > 65535:
    SUM = (SUM & 0xFFFF) + 1
SUM = 17949 + EIPOe  # 17949 fixo, representa Versao(4), HdrLen(5) e ToS, ID, Flags, Offset = 0
#####################TTL(1), Proto(1), Length(28)
if SUM > 65535:
    SUM = (SUM & 0xFFFF) + 1
SUM = SUM + EIPOd
if SUM > 65535:
    SUM = (SUM & 0xFFFF) + 1
SUM = SUM + EIPDe
if SUM > 65535:
    SUM = (SUM & 0xFFFF) + 1
SUM = SUM + EIPDd
if SUM > 65535:
    SUM = (SUM & 0xFFFF) + 1
ChkIP = SUM
ChkIP = 0xFFFF - ChkIP
ChkIPe = (ChkIP & 0xFF00) >> 8
ChkIPd = (ChkIP & 0xFF)

# atribui valor a campos do cabeçalho ICMP
Tipo = 8
Code = 0
Id = 1
Ide = (Id & 0xFF00) >> 8
Idd = (Id & 0xFF)
SeqNo = 0
SeqNoe = (SeqNo & 0xFF00) >> 8
SeqNod = (SeqNo & 0xFF)

# calculo do checksum ICMP
SUM = 0
SUM = SUM + ((Tipo << 8) + Code)
if SUM > 65535:
    SUM = (SUM & 0xFFFF) + 1
SUM = SUM + Id
if SUM > 65535:
    SUM = (SUM & 0xFFFF) + 1
SUM = SUM + SeqNo
if SUM > 65535:
    SUM = (SUM & 0xFFFF) + 1
ChkICMP = SUM
ChkICMP = 0xFFFF - ChkICMP  # complemento de 1
ChkICMPe = (ChkICMP & 0xFF00) >> 8
ChkICMPd = (ChkICMP & 0xFF)

# MONTA O BUFFER DE SAÍDA
Q = []
# Monta cabecalho Ethernet
Q.append(chr(McDest1))  # Byte[0]
Q.append(chr(McDest2))  # Byte[1]
Q.append(chr(McDest3))  # Byte[2]
Q.append(chr(McDest4))  # Byte[3]
Q.append(chr(McDest5))  # Byte[4]
Q.append(chr(McDest6))  # Byte[5]
Q.append(chr(McOrig1))  # Byte[6]
Q.append(chr(McOrig2))  # Byte[7]
Q.append(chr(McOrig3))  # Byte[8]
Q.append(chr(McOrig4))  # Byte[9]
Q.append(chr(McOrig5))  # Byte[10]
Q.append(chr(McOrig6))  # Byte[11]
Q.append(chr(0x08))  # Byte[12]
Q.append(chr(0x00))  # Byte[13]
# Monta cabecalho IP
Q.append(chr(VH))  # Byte 14
Q.append(chr(ToS))  # Byte 15
Q.append(chr(LenIPe))  # Byte 16
Q.append(chr(LenIPd))  # Byte 17
Q.append(chr(PktIDe))  # Byte 18
Q.append(chr(PktIDd))  # Byte 19
Q.append(chr(FlagOffe))  # Byte 20
Q.append(chr(FlagOffd))  # Byte 21
Q.append(chr(TTL))  # Byte 22
Q.append(chr(Proto))  # Byte 23
Q.append(chr(ChkIPe))  # Byte 24
Q.append(chr(ChkIPd))  # Byte 25
Q.append(chr(EIPO0))  # Bytes 26
Q.append(chr(EIPO1))  # Bytes 27
Q.append(chr(EIPO2))  # Byte 28
Q.append(chr(EIPO3))  # Byte 29
Q.append(chr(EIPD0))  # Byte 30
Q.append(chr(EIPD1))  # Byte 31
Q.append(chr(EIPD2))  # Byte 32
Q.append(chr(EIPD3))  # Byte 33
# Monta cabecalho ICMP
Q.append(chr(Tipo))  # Byte 34
Q.append(chr(Code))  # Byte 35
Q.append(chr(ChkICMPe))  # Bytes 36
Q.append(chr(ChkICMPd))  # Bytes 37
Q.append(chr(Ide))  # Bytes 38
Q.append(chr(Idd))  # Bytes 39
Q.append(chr(SeqNoe))  # Bytes 40
Q.append(chr(SeqNod))  # Bytes 41 --- fazer loop aumentando +1

# print(Q)
# converte de lista para string
Q = ''.join(Q)
Q = str.encode(Q)
print(Q, type(Q))

b = ' '
for i in range(len(EIPD)):
    b += EIPD[i] + '.'

# envia frame e encerra
s.send(Q)
print('Enviado ...')
while True:
    buffer = s.recvfrom(1024)
    S = buffer[0]
    # print ord(S[23]), type(S[23])
    if ord(S[23]) == 1:
        print('Protocolo: ', ord(S[23]))
        print('TipoIcmp', ord(S[34]))  # deve ser 11
        print('CodIcmp', ord(S[35]))  # deve ser 0
        print('IdIcmp', ord(S[38]), ord(S[39]))
        print('SeqNo', ord(S[40]), ord(S[41]))
        print('Maquina remota: ', buffer[1])
        #		print 'Nome maquina remota: ', socket.gethostbyname(buffer[1][0])
        break
s.close()
