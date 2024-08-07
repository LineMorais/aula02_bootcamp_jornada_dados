# %% #### Números de Ponto Flutuante (float)
import math

# %% 1. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_01 = float(input('Digite um número: '))
numero_02 = float(input('Digite outro número: '))

soma = numero_01 + numero_02

soma

# %% 2. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_01 = float(input('Digite um número: '))
numero_02 = float(input('Digite outro número: '))

media = (numero_01 + numero_02)/2

media 

# %% 3.Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_01 = float(input('Digite um número: '))
numero_02 = float(input('Digite o expoente: '))

potencia = numero_01**numero_02

potencia

# %% 4.Faça um programa que converta a temperatura de Celsius para Fahrenheit.
c = float(input("Digite a temperatura em Celsius:"))
f = 32 + (9/5)*c

print(f"A temperatura em Fahrenheit é:",f,"°F")

#%% 5. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input('Digite o raio: '))
area_do_circulo = math.pi * raio_do_circulo ** 2

print(f'{area_do_circulo:2f}')