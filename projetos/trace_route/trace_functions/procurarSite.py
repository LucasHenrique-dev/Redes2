import socket


def procurar_site():
    site = site_addr = ""

    while site_addr == "":
        try:
            site = input("Nome do site: ")
            site_addr = socket.gethostbyname(site)
        except socket.error:
            print("Site fora de alcance, por favor verifique a escrita ou tente outro!")

    return [site, site_addr]
