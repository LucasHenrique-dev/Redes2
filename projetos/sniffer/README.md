# 💻 Sniffer

![PYTHON](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

## 🎯 Proposta

O objetivo da aplicação é criar um programa Sniffer o qual realiza um monitoramento dos pacotes na rede e exibe detalhadamente os campos do cabeçalho IPv4.

<p align="center">
   <img src="https://github.com/LucasHenrique-dev/Redes2/blob/main/images/sniffer/sniffer_img1.png" alt="foto 1 do programa sniffer">
</p>
<p align="center">
   <img src="../../images/sniffer/sniffer_img2.png" align="center" alt="foto 2 do programa sniffer">
</p>

> O programa exibe até o campo "Endereço de Destino" (Destination Address) do cabeçalho IPv4.

## 🚀 Funcionalidades

- [x] Analisa 3 pacotes
- [x] Exibe dados brutos e em decimal do cabeçalho IPv4
- [x] Detalha os campos Header Length, DS/ToS, Total Length, Flags, Protocol, Header Checksum, Source Address e Destination Address
- [x] Implementa cálculo do Checksum (como o valor do campo é calculado)
- [x] Exibe localização dos endereços de origem e destino

## ☕ Usando o Sniffer

Execute o arquivo **meuSnifferWindows.py** usando privilégios de administrador: [Sniffer](meuSnifferWindows.py)</br>
-  OBS: Para que funcione você irá precisar da pasta **sniffer_functions** </br>
   Considere clonar o projeto para facilitar seu uso </br>
   Clone: `git clone https://github.com/LucasHenrique-dev/Redes2.git`

[⬆ Voltar ao topo](#-sniffer)
