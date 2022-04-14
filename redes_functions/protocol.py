def protocol(data):
    print(f"Protocol: {data}\n    Protocol Type:", end=" ")

    if data == 6:
        print("TCP")
    elif data == 17:
        print("UDP")
    elif data == 1:
        print("ICMP")
