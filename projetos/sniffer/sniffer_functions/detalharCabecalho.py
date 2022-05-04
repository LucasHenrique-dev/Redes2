import struct

from projetos.sniffer.sniffer_functions.typeOfService import type_of_service
from projetos.sniffer.sniffer_functions.totalLength import total_length
from projetos.sniffer.sniffer_functions.flags import flags
from projetos.sniffer.sniffer_functions.protocol import protocol
from projetos.sniffer.sniffer_functions.checksum import checksum
from projetos.sniffer.sniffer_functions.address import address


def show_header(buffer, local_ip):
    print(f"{'*'*40} Dados do IP HEADER {'*'*40}")
    print(f"Version: {buffer[0] >> 4}")  # CAPTURA OS 4 PRIMEIROS BITS DO 1° BYTE
    ip_header_len = buffer[0] & 0x0f  # CAPTURA OS 4 LAST BITS DO 1° BYTE
    print(f"Header Length: {ip_header_len}")
    print(f"    Existe(m): {ip_header_len - 5} options")
    print(f"DS Field (Differentiated Services) - TOS Byte:")
    type_of_service(buffer[1])  # TOS == DSCP + ECN
    total_length(buffer[2:4], ip_header_len)
    print(f"ID: {struct.unpack('! H', buffer[4:6])[0]}")  # IDENTIFICA OS FRAGMENTOS DO DATAGRAMA IP
    flags(buffer[6] >> 5)
    print(f"Fragment Offset: {struct.unpack('! H', buffer[6:8])[0] & 0x1FFF}")
    print(f"Time to Live: {buffer[8]}")  # TEMPO EM QUE O PACOTE DEVE EXISTIR NO COMPUTADOR OU REDE ANTES DO DESCARTE
    protocol(buffer[9])
    print(f"Header Checksum: {struct.unpack('! H', buffer[10:12])[0]}")  # VERIFICA A INTEGRIDADE DOS DADOS DO IP HEADER
    checksum(buffer[0:ip_header_len * 4], ip_header_len)
    address(buffer[12:16], 0, local_ip)  # SOURCE IGUAL AO DO PC -> ENVIO DE PACOTE
    address(buffer[16:20], 1, local_ip)  # DESTINATION IGUAL AO DO PC -> RECEBIMENTO DE PACOTE
    print("*"*100)
