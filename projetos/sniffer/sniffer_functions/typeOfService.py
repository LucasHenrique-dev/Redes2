def type_of_service(data):
    dscp, ecn = calcular_bits(data)

    print(f"    DSCP (Differentiated Services Code Point): {dscp}")
    print(f"    ECN (Explicit Congestion Notification): {ecn:>4}")


def calcular_bits(data):
    dscp = data >> 2
    ecn = bin(data & 0x03)[2:]

    return dscp, ecn


"""
BITWISEOPERATORS:
- '<<' VALORIZA (ADICIONA ZEROS -> x*[2**y])
- '>>' DEPRECIA (REDUZ ZEROS -> x//[2**y])
"""
