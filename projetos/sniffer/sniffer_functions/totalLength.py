import struct


def total_length(data, header_length):
    total = struct.unpack("! H", data)[0]
    print(f"Total Length: {total:>7} Bytes")
    print(f"    Header Length: {header_length*4} Bytes")
    print(f"    Data Length: {total - (header_length*4):>4} Bytes")


"""
ARGUMENTOS:
- "!" -> USADO PARA TRABALHAR TANTO COM DADOS BIG-ENDIAN OU LITTLE-ENDIAN
- "H" -> UNSIGNED SHORT INTEGER OF 2 BYTES
- "6s" -> STRING DE 6 CARACTERES (1 CHAR == 1 BYTE)
- "B" -> UNSIGNED CHAR (1 BYTE)
PROCEDIMENTO:
DESEMPACOTAR "DATA" COM BASE NAS INFOS PASSADAS NO 1° ARGUMENTO
EX.: UNPACK('! H BB 3B H', DATA) DESEMPACOTA 4 INFOS:
    - 1ª: POSSUI TAMANHO DE 2 BYTES
    - 2ª: POSSUI TAMANHO DE 2 BYTES
    - 3ª: POSSUI TAMANHO DE 3 BYTES
    - 4ª: POSSUI TAMANHO DE 2 BYTES
"""
