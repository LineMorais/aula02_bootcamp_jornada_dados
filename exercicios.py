# %%
# #### Inteiros (int)
# %% 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero_01 = int(input('Digite um número inteiro: '))
numero_02 = int(input('Digite outro número inteiro: '))

resultado_soma = numero_01 + numero_02

print(f"A soma é:", resultado_soma)

# %% 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_01 = int(input('Digite um número inteiro: '))

resultado_resto = numero_01 % 5

print(f"O resto da divisão por 5 é:", resultado_resto)

# %% 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_01 = int(input('Digite um número inteiro: '))
numero_02 = int(input('Digite outro número inteiro: '))

resultado_multiplicacao = numero_01 * numero_02

print(f"O resultado da multiplicação é:", resultado_multiplicacao)

# %% 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_01 = int(input('Digite um número inteiro: '))
numero_02 = int(input('Digite outro número inteiro: '))

resultado_divisao = numero_01 // numero_02

print(f"O resultado da divisão inteira é:", resultado_divisao)

# %% 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário
numero_02 = int(input('Digite outro número inteiro: '))

resultado_quadrado = numero_01 ** 2

print(f"O quadrado do número é:", resultado_quadrado)