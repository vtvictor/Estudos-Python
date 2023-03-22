import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for i in range(tamanho):
        senha += random.choice(caracteres)
    return senha

tamanho = int(input("Digite o tamanho da senha: "))
senha = gerar_senha(tamanho)
print(f"A senha gerada é: {senha}")
