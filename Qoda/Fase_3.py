'''Crie um algoritmo em Python que peça uma nota, entre zero e 100. Mostre uma mensagem caso o valor seja inválido e continue pedindo 
até que o usuário informe um valor válido.'''

while True:
    nota = int(input('Digite a nota entre 0 e 100: '))
    if nota < 0 or nota > 100:
        print('Erro. Nota inválida!')
        continue
    break
    
    
    
'''Crie um algoritmo em Python que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.'''

while True:
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite a senha de usuário: ')
    if nome == senha:
        print('A senha não pode ser igual ao usuário!')
        continue
    break
    
    
'''
Crie um algoritmo em Python que leia e valide as seguintes informações:

  Nome: maior que 3 caracteres;
  Idade: entre 0 e 150;
  Salário: maior que zero;
  Sexo: 'f' ou 'm';
  Estado Civil: 's', 'c', 'v', 'd'
'''

while True:
    try:
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        sal = float(input('Digite o salário: '))
        sexo = input('Digite f(feminino) ou m(masculino): ')
        estado_civil = input('Digite s(solteiro), c(casado), v(viúvo) ou d(divorciado): ')

        if len(nome) < 3:
            raise ValueError('Nome deve ser maior que 3 caracteres! ')

        if idade < 0 or idade > 150:
            raise ValueError('Idade deve ser estar entre 0 e 150! ')

        if sal < 0:
            raise ValueError('Salário deve ser maior que 0! ')

        if sexo != 'f' and sexo != 'm':
            raise ValueError('Sexo deve ser f(feminino) ou m(masculino)! ')

        if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
            raise ValueError('Estado civil deve ser s(solteiro), c(casado), v(viúvo) ou d(divorciado)! ')

        break

    except ValueError as ve:
        print(ve)


'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.

Crie um algoritmo em Python que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou 
iguale a população do país B, mantidas as taxas de crescimento.'''

pop_a = 80000
tx_a = 0.03

pop_b = 200000
tx_b = 0.015

anos = 0

while pop_a < pop_b:
    crescimento_pop_a = pop_a * tx_a
    pop_a += crescimento_pop_a

    crescimento_pop_b = pop_b * tx_b
    pop_b += crescimento_pop_b

    anos += 1

    print(f'População A: {int(pop_a)}')
    print(f'População B: {int(pop_b)}')

    print(f'{anos} Ano(s) \n')


'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar
de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: Tabuada de 5:

  5 X 1 = 5
  5 X 2 = 10
  ...
  5 X 10 = 50
'''

while True:
    num = int(input('Digite um número entre 1 e 10: '))

    if num < 1 or num > 10:
        print('O número deve estar entre 1 e 10! ')
        continue

    print(f'Tabuada do {num}: \n')

    for i in range(1,11):
        print(f'{num} x {i} = {num * i} ')
    break


# Crie um algoritmo em Python que leia três números e mostre o maior e o menor deles.

lista = []

num1 = int(input('Digite o 1º número: '))
lista.append(num1)
num2 = int(input('Digite o 2º número: '))
lista.append(num2)
num3 = int(input('Digite o 3º número: '))
lista.append(num3)

print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')


'''Crie um algoritmo em Python que peça 2 números, base e expoente, calcule e mostre o primeiro 
número elevado ao segundo número. Não utilize a função de potência da linguagem.'''

base = int(input('Digite a base: '))
exp = int(input('Digite o expoente: '))

if exp == 0:
    calc = 1
    print(f'{base} ^ {exp} = {calc}')

else:
    calc = base
    i = 1

    while i < exp:
        calc *= base
        i += 1

    print(f'{base} ^ {exp} = {calc}')


# Crie um algoritmo em Python que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

lista = []

for i in range(1,11):
    num = int(input(f'Digite o {i} número: '))
    lista.append(num)

pares = 0
impares = 0

for x in lista:
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Pares: {pares}')
print(f'Impares: {impares}')


'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que: Esse funcionário foi contratado em 1995, 
com salário inicial de R$ 1.000,00; Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de 1997 (inclusive), 
os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Crie um algoritmo em Python que determine 
o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial 
do funcionário.'''

import datetime
year_today = datetime.date.today().year

sal = float(input('Digite o salário: '))

ano_inicio = 1996
tx = 0.015

while ano_inicio < year_today:
    aumento = sal * tx
    sal += aumento
    ano_inicio += 1
    tx *= 2
    print(f'Ano: {ano_inicio}')
    print(f'taxa: {tx}')
    print(f'Aumento: {aumento:.2f}')
    print(f'Salario: {sal:.2f}\n')

print(f'O salário atual é R$ {sal}')



'''Crie um algoritmo em Python com uma função que necessite de um argumento. A função retorna o valor 
de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.'''

def funcao(argumento):
    if int(argumento) >= 0:
        print('P')
    else:
        print('N')


def main():
    funcao(7)


if __name__ == '__main__':
    main()



'''Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato 
D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.'''

from datetime import datetime
from time import strptime


def data(data):

    data_dia = datetime.strptime(data, "%d/%m/%Y").strftime('%d')
    data_mes = datetime.strptime(data, "%d/%m/%Y").strftime('%B')
    data_ano = datetime.strptime(data, "%d/%m/%Y").strftime('%Y')

    return print(f'{data_dia} de {data_mes} de {data_ano} ')


def main():
    data('7/11/2000')


if __name__ == '__main__':
    main()


'''
Crie uma classe que modele uma pessoa:

  Atributos: nome, idade, peso e altura
  Métodos: Envelhercer, engordar, emagrecer, crescer.

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def engordar(self):
        self.peso += 1
        return print(f'Peso: {self.peso} kg')


    def emagrecer(self):
        self.peso -= 1
        return print(f'Peso: {self.peso} kg')


    def crescer(self):
        self.altura += 0.05
        return print(f'Altura: {self.altura} m')


    def envelhercer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.05
            print(f'Altura: {self.altura} m')
        return print(f'Idade: {self.idade}')


def main():
    pessoa = Pessoa('Fulano', 19, 50, 1.67)

    # print(pessoa.nome)
    # print(pessoa.idade)
    # print(pessoa.peso)
    # print(pessoa.altura)
    
    pessoa.crescer()
    pessoa.engordar()
    pessoa.emagrecer()
    pessoa.envelhercer()


if __name__ == '__main__':
    main()
