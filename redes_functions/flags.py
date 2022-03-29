def flags(data):
    primeiro_bit, segundo_bit, terceiro_bit = calcular_bits(data)

    print(f"Flags: {data:>14}")
    print(f"    Reserved bit: {primeiro_bit:>3}")
    print(f"    Don't Fragment: {segundo_bit}")
    print(f"    More Fragments: {terceiro_bit}")


def calcular_bits(data):
    primeiro_bit = bin(data & 0b100)[2:3]
    segundo_bit = bin(data & 0b010)[2:3]
    terceiro_bit = bin(data & 0b001)[2:3]

    return primeiro_bit, segundo_bit, terceiro_bit
