def type_of_service(data):
    precedence = data >> 5

    delay, throughput, reliability, cost, reserved = calcular_bits(data)

    print(f"    Precedence: {precedence:>2}")  # MUITAS CATEGORIAS? (VER DSCP, SLIDES; MOSTRAR CASO HAJA?)
    print(f"    Delay: {delay:>7}")
    print(f"    Throughput: {throughput:>2}")  # TAXA DE DADOS TRANFERIDOS
    print(f"    Reliability: {reliability}")
    print(f"    Cost: {cost:>8}")
    print(f"    Reserved: {reserved:>4}")


def calcular_bits(data):
    delay = bin(data & 0x10)[2:3]
    throughput = bin(data & 0x08)[2:3]
    reliability = bin(data & 0x04)[2:3]
    cost = bin(data & 0x02)[2:3]
    reserved = bin(data & 0x01)[2:3]

    return delay, throughput, reliability, cost, reserved


"""
BITWISEOPERATORS:
- '<<' VALORIZA (ADICIONA ZEROS -> x*[2**y])
- '>>' DEPRECIA (REDUZ ZEROS -> x//[2**y])
"""
