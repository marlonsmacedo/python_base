#!/usr/bin/python3

"""Imprime a tabuada do 1 ao 10.

Formaro de exibição do script:

    TABUADA DO 1:
        1x1 = 1
        1x2 = 2
        ...


    _______________

    TABUADA DO 2
        2x1 = 2
        2x2 = 4
        ...

"""

__version__ = "0.1.0"
__author__ = "Marlon Macedo"

#criando uma lista para os multipplicadores:
multiplicadores = [1,2,3,4,5,6,7,8,9,10]

print(multiplicadores)

for multiplicandos in multiplicadores:
    print("tabuada do:", multiplicandos)
    for multiplicador in multiplicadores:
        print(multiplicador, "x", multiplicandos, "=", multiplicador * multiplicandos)
    print("----------------")

