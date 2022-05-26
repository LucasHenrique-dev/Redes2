import ipinfo


def exibir_rota(enderecos):
    roteadores = []

    for endereco in enderecos:
        roteador = address_info(endereco)
        roteadores.append(roteador)

    print(f"Rota percorrida:\n{' -> '.join(roteadores)}")


def address_info(endereco):
    if endereco != "*":
        details = conectar_ip_info(endereco)

        info = info_validation(details)
    else:
        info = "_"

    return info


def info_validation(infos):
    campos = infos.details.keys()

    city = infos.city if 'city' in campos else ""
    region = infos.region if 'region' in campos else ""
    country = infos.country_name if 'country_name' in campos else ""
    org = infos.org if 'org' in campos else ""

    return formatar_mensagem(city, region, country, org)


def formatar_mensagem(city, region, country, org):
    if not city and not region and not country and not org:
        return "_"

    city = city if city else "?"
    region = region if region else "?"
    country = country if country else "?"
    org = org if org else "?"

    return f"{org} ({city}, {region} - {country})"


def conectar_ip_info(address_value):
    access_token = 'ad92174bc9060f'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(address_value)

    return details


"""
Github da API para identificar a origem do IP Address: https://github.com/ipinfo/python
StackOverflow: https://stackoverflow.com/questions/24678308/how-to-find-location-with-ip-address-in-python
Site Extra (Identificar IP): https://nordvpn.com/pt-br/ip-lookup/
"""
