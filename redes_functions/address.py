import struct


def address(data, target):
    if target == 1 or target == 0:
        fonte = "Source" if target == 0 else "Destination"

        print(f"{fonte} Address: {'.'.join(str(num) for num in data)}")
    else:
        print("Erro!\nVerifique o valor do 2° argumento de 'address(data, target)':"
              "\n- '0': Source Address\n- '1': Destination Address")
