# %% # Exercícios 
# Aqui estão cinco exercícios que envolvem TypeError, verificação de tipo ( type check), 
# o uso de try-exceptpara tratamento de abordagem e a utilização da estrutura condicional if. 
# Esses exercícios aumentam progressivamente em dificuldades e abordam situações práticas onde você pode aplicar esses conceitos.

# %% # Exercício 1: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# try:
#     c = float(input("Digite a temperatura em Celsius:"))
#     f = 32 + (9/5)*c
#     print(f"A temperatura em Fahrenheit é:",f,"°F")
# except ValueError:
#     print("Por favor, digite um número válido para a temperatura.")


 
# %% # Exercício 2: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e esperados). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize uma função isinstance()para verificar o tipo de entrada.
entrada = input("Digite uma palavra ou frase: ")
formatado = entrada.replace(" ", "").lower()
if formatado == formatado[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")

# %% # Exercício 3: Calculadora Simples
# Desenvolva uma calculadora simples que aceita duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro.

try: 
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    operacao = input('Escolha a operação: \n para soma (+),\n para subtração (-),\n para multiplicação (*),\n para divisão (/)')

    if operacao == '+':
        soma = n1 + n2
        print(f'O resultado da soma de {n1} + {n2} = {soma}')
    elif operacao == '-':
        subtracao = n1 - n2
        print(f'O resultado da subtração de {n1} - {n2} = {subtracao}')
    elif operacao == '*':
        multiplicacao = n1 * n2
        print(f'O resultado da multiplicação de {n1} * {n2} = {multiplicacao}')
    elif operacao == '/':
        divisao = n1 / n2
        print(f'O resultado da multiplicação de {n1} / {n2} = {divisao}')
    else: 
        print("Operador inválido ou divisão por zero.")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")


# %% #Exercício 4: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-exceptpara garantir que a entrada seja numérica e utilize 
# if-elif-elsepara classificar o número como "positivo", "negativo" ou "zero". 
# Além disso, identifique se o número é "par" ou "ímpar".

try:
    n1 = float(input("Digite um número: "))
    if n1 < 0:
        print(f'{n1} é um número negativo')
    elif n1 > 0:
        print(f'{n1} é um número positivo')
    else:
        print(f'Esse número é Zero')
    if n1 % 2 == 0:
        print(f'{n1} é um número par')
    else: 
        print(f'{n1} é um número impar')
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")   


 
# %% # Exercício 5: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter uma string de entrada em uma lista de números inteiros. 
# Utilize try-exceptpara tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")   
# %%
