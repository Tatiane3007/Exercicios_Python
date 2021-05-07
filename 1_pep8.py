"""
import this **


PEP8 - Python Enhancement Proposal

A idéia da PEP8 é que escrever códigos Python de forma Pythônica.



[1] - Utilize Camel Case para nomes de classes;

    class CalculadoraCientifica:
        pass

#-----------------------------------------------------------------------------------------------------------------------
[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

    def soma():
        pass

    numero_impar = 7

#-----------------------------------------------------------------------------------------------------------------------
[3] - Utilize 4 espaços para identação!!! (NÃO use tab)

#-----------------------------------------------------------------------------------------------------------------------
[4] - Linhas em branco
    - separar funções e definições de classe com duas linhas em branco;
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco;

#-----------------------------------------------------------------------------------------------------------------------
[5] - Imports

    - Imports devem ser sempre feitos em linhas separadas;

    # Import errado
        import sys, os

    # Import certo
        import sys
        import os

    # Não há problemas em utilizar:
        from types import StringType, ListType

    # Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
        from types import (
            StringType,
            ListType,
            SetType
        )

    # Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
    # antes de constantes ou variáveis globais.

#-----------------------------------------------------------------------------------------------------------------------
[6] - Espaços em expressões e instruções

    # Errado:
        funcao(_algo[_1_], {_outro: 2_}_)
    # Certo:
        funcao(algo[1], {outro: 2})

    # Errado:
        algo_(1)
    # Certo:
        algo(1)

    # Errado:
        dict_['chave'] = lista_[indice]
    # Certo:
        dict['chave'] = lista[indice]

    # Errado:
        x              = 1
        y              = 3
        variavel_longa = 5
    # Certo:
        x = 1
        y = 3
        variavel_longa = 5

#-----------------------------------------------------------------------------------------------------------------------
[7] - SEMPRE termine uma instrução com uma nova linha vazia
"""
