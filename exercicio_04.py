# %% Booleanos (bool)

# %% 1. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
def str_to_bool(value):
    return value.lower() in ("true", "1", "t", "y", "yes")

# Solicita ao usuário para inserir duas expressões booleanas
expr1 = input("Insira a primeira expressão booleana (True/False): ")
expr2 = input("Insira a segunda expressão booleana (True/False): ")

# Converte as entradas para booleano
bool1 = str_to_bool(expr1)
bool2 = str_to_bool(expr2)

# Realiza a operação AND entre as duas expressões booleanas
resultado = bool1 and bool2

# Exibe o resultado
print(f"O resultado da operação AND entre {bool1} e {bool2} é {resultado}")

# %% 2. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Função para converter entrada do usuário em booleano
def str_to_bool(value):
    return value.lower() in ("true", "1", "t", "y", "yes")

# Solicita ao usuário para inserir dois valores booleanos
val1 = input("Insira o primeiro valor booleano (True/False): ")
val2 = input("Insira o segundo valor booleano (True/False): ")

# Converte as entradas para booleano
bool1 = str_to_bool(val1)
bool2 = str_to_bool(val2)

# Realiza a operação OR entre os dois valores booleanos
resultado = bool1 or bool2

# Exibe o resultado
print(f"O resultado da operação OR entre {bool1} e {bool2} é {resultado}")

# %% 3. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# Função para converter entrada do usuário em booleano
def str_to_bool(value):
    return value.lower() in ("true", "1", "t", "y", "yes")

# Solicita ao usuário para inserir um valor booleano
val = input("Insira um valor booleano (True/False): ")

# Converte a entrada para booleano
bool_val = str_to_bool(val)

# Inverte o valor booleano
inverted_val = not bool_val

# Exibe o resultado
print(f"O valor invertido de {bool_val} é {inverted_val}")

# %% 4. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# Solicita ao usuário para inserir dois números
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

# Compara se os dois números são iguais
sao_iguais = num1 == num2

# Exibe o resultado
if sao_iguais:
    print(f"Os números {num1} e {num2} são iguais.")
else:
    print(f"Os números {num1} e {num2} são diferentes.")

# %% 5. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# Solicita ao usuário para inserir dois números
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

# Compara se os dois números são diferentes
sao_diferentes = num1 != num2

# Exibe o resultado
if sao_diferentes:
    print(f"Os números {num1} e {num2} são diferentes.")
else:
    print(f"Os números {num1} e {num2} são iguais.")