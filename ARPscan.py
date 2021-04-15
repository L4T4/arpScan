from scapy.all import ARP, Ether, srp
# import sys

# endereço IP para o destino com máscara de subrede definindo o range
target_ip = "192.168.43.1/24"

# cria pacote ARP na camada 3(rede)
arp = ARP(pdst=target_ip)

# cria o pacote de transmissão Ether na camada 2(enlace)
# ff:ff:ff:ff:ff:ff endereço MAC indica transmissão para qualquer endereço
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# o operador "/" empilha os pacotes
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# um array de clientes, nos iremos preencher isso no loop que virá
clients = []

for sent, received in result:
    # Para cada resposta, acrescente IP e endereço MAC na lista 'clientes'
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# imprimir na tela os clientes
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
