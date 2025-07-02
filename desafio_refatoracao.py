# Código anterior
# CONSTANTE_BONUS = 1000

# nome = input("Digite o seu nome: ")
# salario = float(input("Digite o seu salário atual: "))
# bonus = float(input("Digite o seu bônus: "))

# valor_bonus = CONSTANTE_BONUS + (salario * bonus)

# print(f"Parabéns {nome}, seu bônus será de R$ {valor_bonus}")

CONSTANTE_BONUS = 1000

# Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

valor_bonus = CONSTANTE_BONUS + (salario * bonus_recebido)

print(f"Parabéns {nome}, seu bônus será de R$ {valor_bonus}")