texto = input("Digite o texto: ")

palavras = texto.split()
total_palavras = len(palavras)
frequencia_palavras = {}
for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1

print(f"Total de palavras: {total_palavras}")
print("Frequência de palavras:")
for palavra, frequencia in frequencia_palavras.items():
    print(f"{palavra}: {frequencia}")