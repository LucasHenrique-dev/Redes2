def typeOfService(data):
    precedence = data >> 5
    delay = data & 0x10
    throughput = data & 0x08
    reliability = data & 0x04
    cost = data & 0x02
    print(f"    Precedence: {precedence:>2}")
    print(f"    Delay: {delay:>7}")
    print(f"    Throughput: {throughput:>2}")  # TAXA DE DADOS TRANFERIDOS
    print(f"    Reliability: {reliability}")
    print(f"    Cost: {cost:>8}")

# >> VALORIZA (ADICIONA ZEROS)
# << DEPRECIA (REDUZ ZEROS)
