# Autor: Hugo Araya Carrasco
# Fecha: 07/08/2024
# Version: 0.0

import matplotlib.pyplot as plt

def collatz(numero):
    lista_col = []
    lista_col.append(numero)
    while numero != 1:
        if numero%2 == 0:
            numero = numero // 2
        else:
            numero = 3*numero + 1
        lista_col.append(numero)
    return lista_col

def es_primo(numero):
    num_primo = True
    inicio = 2
    fin = numero - 1
    while inicio <= fin:
        if numero % inicio == 0:
            num_primo = False
        inicio = inicio + 1
    return num_primo

def busca_primos(lista_col):
    lista_primos = []
    for num in lista_col:
        if es_primo(num) == True:
            lista_primos.append(num)
    return lista_primos

def grafica(lista_col, lista_primo):
    total = len(lista_col)
    primo = len(lista_primo)
    todos = "No Primos ("+str(total-primo)+")"
    solos = "Primos ("+str(primo)+")"
    valores = [primo, total-primo]
    etiquetas = [solos, todos]
    separacion = [0.2, 0]
    colores = ['Blue', 'Green']
    plt.pie(valores, labels = etiquetas, explode = separacion, shadow = False, colors = colores)
    #plt.legend()
    plt.show()

if __name__ == '__main__':
    numero = int(input('Numero: '))
    lista_col = collatz(numero)
    num_primo = es_primo(numero)
    lista_primos = busca_primos(lista_col)
    grafica(lista_col, lista_primos)



