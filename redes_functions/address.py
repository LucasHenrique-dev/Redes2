import ipinfo


def address(data, target, local_address):
    if target == 1 or target == 0:
        fonte = "Source" if target == 0 else "Destination"
        address_value = '.'.join(str(num) for num in data)

        print(f"{fonte} Address: {address_value}")
        address_info(address_value, local_address)
    else:
        print("Erro!\nVerifique o valor do 2° argumento de 'address(data, target)':"
              "\n- '0': Source Address\n- '1': Destination Address")


def address_info(address_value, local_address):
    access_token = 'ad92174bc9060f'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(address_value)
    if address_value != local_address:
        city, region, country, org, hostname, timezone = info_validation(details)

        print(f"     Foreign Address")
        print(f"        City: {city if city else '-'}\n"
              f"        Region: {region if region else '-'}\n"
              f"        Country: {country if country else '-'}\n"
              f"        Org: {org if org else '-'}\n"
              f"        hostname: {hostname if hostname else '-'}\n"
              f"        timezone: {timezone if timezone else '-'}")
    else:
        print("     Local Address")


def info_validation(infos):
    campos = infos.details.keys()

    city = infos.city if 'city' in campos else ""
    region = infos.region if 'region' in campos else ""
    country = infos.country_name if 'country_name' in campos else ""
    org = infos.org if 'org' in campos else ""
    hostname = infos.hostname if 'hostname' in campos else ""
    timezone = infos.timezone if 'timezone' in campos else ""

    return city, region, country, org, hostname, timezone


"""
Github da API para identificar a origem do IP Address: https://github.com/ipinfo/python
StackOverflow: https://stackoverflow.com/questions/24678308/how-to-find-location-with-ip-address-in-python
Site Extra (Identificar IP): https://nordvpn.com/pt-br/ip-lookup/
"""
