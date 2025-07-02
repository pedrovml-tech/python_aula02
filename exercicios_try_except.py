# #### try-except e if

# 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir
# que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit
# ou uma mensagem de erro se a entrada não for válida.

# try:
#     temp_celsius = float(input("Digite a temperatura em graus Celsius: "))
#     # Fórmula: °F = (°C * 1.8) + 32
#     temp_fahrenheit = temp_celsius * 1.8 + 32

#     print(f"{temp_celsius}°C equivalem a {temp_fahrenheit}°F")

# except ValueError as e:
#     print("O valor digitado deve ser um número.")


# 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços).
# Utilize try-except para garantir que a entrada seja uma string.
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# entrada = "arara"

# if isinstance(entrada, str):
#     entrada_formatada = entrada.replace(" ", "")
#     if entrada_formatada == entrada_formatada[::-1]:
#         print("É um palíndromo")
#     else:
#         print("Não é um palíndromo")
# else:
#     print("Entrada inválida. Digite uma frase ou palavra.")


# 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas não numéricas.
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido.
# Imprima o resultado ou uma mensagem de erro apropriada.

# try:
#     valor_1 = float(input("Digite o primeiro número: "))
#     valor_2 = float(input("Digite o segundo número: "))
#     operacao = input("Digite uma operação (+, -, *, /): ")
    
#     if operacao == '+':
#         resultado = valor_1 + valor_2
#         print("Resultado:", resultado)
#     elif operacao == '-':
#         resultado = valor_1 - valor_2
#         print("Resultado:", resultado)
#     elif operacao == '/' and valor_2 != 0:
#         resultado = valor_1 / valor_2
#         print("Resultado:", resultado)
#     elif operacao == '*':
#         resultado = valor_1 * valor_2
#         print("Resultado:", resultado)
#     else:
#         print("Operação inválida")
    
# except ValueError:
#     print("Número inválido.")


# 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para
# assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como
# "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# try:
#     numero = float(input("Digite um número: "))
#     sinal = ""
#     tipo = ""
#     if numero > 0:
#         sinal = "positivo"
#     elif numero < 0:
#         sinal = "negativo"
#     else:
#         sinal = "zero"

#     if numero % 2 == 0:
#         tipo = "par"
#     else:
#         tipo = "impar"

#     print(f"Este é um número {sinal}, do tipo {tipo}")
     
# except ValueError:
#     print("Número inválido.")

# 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve
# converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a
# conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão
# falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida
# para todos os elementos, imprima a lista de inteiros.

# entrada = input("Digite uma lista de números inteiros separados por vírgula: ")
# lista = entrada.split(",")
# lista_convertida = []

# try:
#     for numero in lista:
#         numero_convertido = int(numero.strip())
#         lista_convertida.append(numero_convertido)

#     print("Lista convertida com sucesso: ", lista_convertida)

# except ValueError as e:
#     print(f"Número inválido: {e}")
