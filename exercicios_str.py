# #### Strings (`str`)
# Alguns exemplos de métodos e operações:
# .upper() (converte para maiúsculas)
# .lower() (converte para minúsculas)
# .strip() (remove espaços em branco no início e no final)
# .split(sep) (divide a string em uma lista, utilizando sep como delimitador)
# + (concatenação de strings)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# valor = input("Digite uma palavra em minúsculo: ")

# resultado = valor.upper()

# print(resultado)
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Digite seu nome:")

# nome_lower_case = nome.lower()

# print(nome_lower_case)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite algo acrescentando espaços no início e ao fim: ")

# resultado = frase.strip()

# print(resultado)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma data no formato dd/mm/yyyy: ")
# data_separada_split = data.split('/')

# dia = data_separada_split[0]
# mes = data_separada_split[1]
# ano = data_separada_split[2]

# print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# nome = input("Digite seu primeiro nome: ")
# sobrenome = input("Digite seu último nome: ")

# nome_sobrenome = nome + ' ' + sobrenome

# print(nome_sobrenome)