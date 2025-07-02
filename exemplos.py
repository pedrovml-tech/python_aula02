# Exemplo TypeError
# try:
#     resultado = len(5)
# except TypeError as e:
#     print(e)



# Exemplo Type Check
# numero = 12

# if isinstance(numero, int):
#     print("A variável é um inteiro.")
# else:
#         print("A variável não é um interno.")



# Exemplo try-except

# try:
#     resultado = 10 / "2"
# except ZeroDivisionError:
#     print("A divisão por zero não é permitida.")
# except KeyboardInterrupt:
#     print("Parece que você desistiu.")
# except Exception as e:
#     print(f"Erro não mapeado: {e}")
# else:
#     print("Tudo ocorreu bem.")
# finally:
#     print("Sempre executa")