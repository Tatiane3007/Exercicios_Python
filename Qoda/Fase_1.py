# Crie um algoritmo em Python que mostre a mensagem "Alo mundo" na tela.

print('Alo mundo')


# Crie um algoritmo em Python que peça dois números e imprima a soma.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(f'{num1} + {num2} = {num1 + num2}')


# Crie um algoritmo em Python que peça um número e então mostre a mensagem O número informado foi [número].

num = int(input('Digite um número: '))
print(f'O número informado foi {num}')


# Crie um algoritmo em Python que converta metros para centímetros.

m = float(input('Digite uma distância em metros: '))
cent = m * 100
print(f'{m} convertido em centímetros é {cent} cm')


# Crie um algoritmo em Python que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input('Digite o raio de um círculo: '))
area = math.pi * raio**2
print(f'Área = {area}')


# Crie um algoritmo em Python que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

quad = float(input('Digite a aresta do quadrado: '))
area = quad **2
dobro = area * 2
print(dobro)


# Crie um algoritmo em Python que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor = float(input('Quanto você ganha por hora? '))
horas = int(input('Qual o número de horas trabalhadas no mês'))


# Crie um algoritmo em Python que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

farenheit = float(input('Digite a temperatura em Farenheit: '))
celsius = (5 * (farenheit - 32)) / 9
print(f'A temperatura em celsius é {celsius:.2f} °C')


# Crie um algoritmo em Python que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

celsius = float(input('Digite a temperatura em Celsius: '))
farenheit = celsius * (9/5) + 32
print(f'A temperatura em Farenheit é {farenheit:.2f} °F')


'''
Crie um algoritmo em Python que peça 2 números inteiros e um número real. Calcule e mostre:

  a soma do dobro do primeiro com metade do segundo .
  a soma do triplo do primeiro com o terceiro.
  o terceiro elevado ao cubo.
'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um número real: '))

soma1 = (num1*2) + (num2/2)
soma2 = (num1*3) + real
cubo = real**3

print(soma1)
print(soma2)
print(cubo)
