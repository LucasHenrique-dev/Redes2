import struct


def checksum(data, header_len):
    grupos_16_bytes = agrupar_bytes(data, header_len)

    if grupos_16_bytes == '-':  # IP HEADER POSSUI OPTIONS (DIFICULDADE EM REALIZAR O UNPACK)
        print(f"    Sem Detalhamento")
    else:
        bytes_lista = list(grupos_16_bytes)
        bytes_lista[5] = 0
        soma = sum(bytes_lista)

        print(f'    Original: {grupos_16_bytes}')
        print(f'    Alterado: {bytes_lista}\n')

        while soma > 0xFFFF:
            carry = soma // 0xFFFF  # \\: INTEGER DIVISION
            soma &= 0x00FFFF
            soma += carry

        binario = formatar_binario(bin(soma)[2:])
        complemento = complemento_1(binario)

        print(f"    Soma: {binario:>23}")
        print(f'    Complemento: {complemento} == {int(complemento, 2)}')


def agrupar_bytes(data, campos):
    header_info = struct.unpack('! H H H H H H H H H H', data[0:20])

    if campos > 5:
        header_info = '-'

    return header_info


def formatar_binario(bits):
    binario = bits

    while len(binario) < 16:
        binario = '0' + binario

    return binario


def complemento_1(bits):
    complemento = ''

    for bit in bits:
        complemento += '1' if bit == '0' else '0'

    return complemento
