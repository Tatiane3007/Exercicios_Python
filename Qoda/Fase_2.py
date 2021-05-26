# Crie um algoritmo em Python que peça 2 números e imprima o maior deles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(num1)
else:
    print(num2)
    
    
# Crie um algoritmo em Python que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Digite um número: '))

if num >= 0:
    print('Positivo')
else:
    print('Negativo')
    
    
# Crie um algoritmo em Python que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if letra in vogais:
    print('Vogal')
else:
    print('Consoante')
    
    
''' 
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

  "Aprovado", se a média alcançada for maior ou igual a sete;
  "Reprovado", se a média for menor do que sete;
  "Aprovado com Distinção", se a média for igual a 10.

'''

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

med = (nota1 + nota2) / 2

if med == 10:
    print('Aprovado com Distinção')
elif med >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    
    
    
# Crie um algoritmo em Python que leia três números e mostre o maior deles.

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

if num1 > num2 > num3:
    print(num1)
elif num1 > num3 > num2:
    print(num1)
elif num2 > num1 > num3:
    print(num2)
elif num2 > num3 > num1:
    print(num2)
elif num3 > num1 > num2:
    print(num3)
elif num3 > num2 > num1:
    print(num3)
    
    
# Crie um algoritmo em Python que leia três números e mostre o maior e o menor deles.

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

if num1 > num2 > num3:
    print(f'Maior -> {num1}')
    print(f'Menor -> {num3}')
elif num1 > num3 > num2:
    print(f'Maior -> {num1}')
    print(f'Menor -> {num2}')
elif num2 > num1 > num3:
    print(f'Maior -> {num2}')
    print(f'Menor -> {num3}')
elif num2 > num3 > num1:
    print(f'Maior -> {num2}')
    print(f'Menor -> {num1}')
elif num3 > num1 > num2:
    print(f'Maior -> {num3}')
    print(f'Menor -> {num2}')
elif num3 > num2 > num1:
    print(f'Maior -> {num3}')
    print(f'Menor -> {num1}')
    
    
# Faça um programa que pergunte o preço de 5 produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

lista_precos = []

prod1 = int(input('Digite o preço do 1º produto: '))
lista_precos.append(prod1)

prod2 = int(input('Digite o preço do 2º produto: '))
lista_precos.append(prod2)

prod3 = int(input('Digite o preço do 3º produto: '))
lista_precos.append(prod3)

prod4 = int(input('Digite o preço do 4º produto: '))
lista_precos.append(prod4)

prod5 = int(input('Digite o preço do 5º produto: '))
lista_precos.append(prod5)

menor = lista_precos[0]

for x in range(5):
    if menor > lista_precos[x]:
        menor = lista_precos[x] # recebe o valor menor do que ele

print(f'\nO produto mais barato é: R${menor}')


# Crie um algoritmo em Python que leia três números e mostre-os em ordem decrescente.

lista_dec = []

num1 = int(input('Digite o 1º número: '))
lista_dec.append(num1)

num2 = int(input('Digite o 2º número: '))
lista_dec.append(num2)

num3 = int(input('Digite o 3º número: '))
lista_dec.append(num3)

lista_dec.sort(reverse=True)

print(lista_dec)


'''
As Organizações Mendéz resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes em Python. Faça um programa que receba o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

  salários entre 680,00 e 800,00 : aumento de 15%
  salários entre 800,00 e 2500,00 : aumento de 10%
  salários de 2500,00 em diante : aumento de 5% 
  
Após o aumento ser realizado, informe na tela:

  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.
'''

sal = float(input('Digite o salário R$ '))

if 680.00 < sal < 800.00:
    perc = 0.15
    aumento = sal * perc
elif 800.00 < sal < 2500.00:
    perc = 0.10
    aumento = sal * perc
elif sal > 2500.00:
    perc = 0.05
    aumento = sal * perc

sal_aumentado = sal + aumento

print(f'\nSalário antes do reajuste: R$ {sal}')
print(f'Percentual de aumento aplicado: {perc * 100}%')
print(f'Valor do aumento: R$ {aumento}')
print(f'Novo salário: R$ {sal_aumentado}')
