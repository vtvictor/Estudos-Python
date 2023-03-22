import requests

def converter_moeda(valor, moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    resposta = requests.get(url)
    dados = resposta.json()
    taxa = dados["rates"][moeda_destino]
    valor_convertido = valor * taxa
    return valor_convertido

valor = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem: ")
moeda_destino = input("Digite a moeda de destino: ")
valor_convertido = converter_moeda(valor, moeda_origem, moeda_destino)
print(f"O valor convertido é: {valor_convertido:.2f}")
