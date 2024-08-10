# %% Strings (str)

# %% 1. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome = input('Digite seu nome: ').upper()

nome

# %% 2. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input('Digite seu nome: ').lower()

nome

# %% 3. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input('Digite uma frase: ').strip()

frase

# %% 4. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input('Digite sua data de nascimento: '.format ("dd/mm/aaaa")).split('/')

data

#  %% 5. Escreva um programa que concatene duas strings fornecidas pelo usuário.
name = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

print((name + ' ' + sobrenome).title())