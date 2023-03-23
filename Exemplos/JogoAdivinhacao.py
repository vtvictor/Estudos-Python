import random

# Define o número máximo que o jogador pode adivinhar
max_number = 100

# Gera um número aleatório entre 1 e o número máximo
number_to_guess = random.randint(1, max_number)

# Define o número de tentativas que o jogador tem
max_attempts = 5
attempts = 0

# Loop para permitir que o jogador faça suas tentativas
while attempts < max_attempts:
    # Solicita ao jogador que digite uma tentativa
    guess = input("Adivinhe um número entre 1 e {}: ".format(max_number))
    guess = int(guess)
    
    # Verifica se a tentativa do jogador está correta
    if guess == number_to_guess:
        print("Parabéns! Você adivinhou o número em {} tentativas.".format(attempts + 1))
        break
    
    # Informa se a tentativa é maior ou menor do que o número correto
    elif guess < number_to_guess:
        print("Tente novamente. O número é maior que {}.".format(guess))
    else:
        print("Tente novamente. O número é menor que {}.".format(guess))
    
    # Incrementa o número de tentativas
    attempts += 1

# Se o jogador não acertar após o número máximo de tentativas, exibe a resposta correta
if attempts == max_attempts:
    print("Você não adivinhou o número. Era {}.".format(number_to_guess))
