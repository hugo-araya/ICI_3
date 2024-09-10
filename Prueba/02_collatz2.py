def sumar(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma

def multiplicar(lista):
    multi = 1
    for numero in lista:
        multi = multi * numero
    return multi

def es_par(numero):
    if numero%2 == 0:
        return True
    else:
        return False
    
def supuesto(numero):
    lista = [numero]
    while numero != 1:
        if es_par(numero):
            numero = numero // 2
        else:
            numero = numero * 3 + 1
        lista.append(numero)
    return lista

def calcular(ini):
    lista = supuesto(ini)
    numero = len(lista)
    return numero

if __name__ == '__main__':
    ini = 4
    numero = calcular(ini)
    lista = supuesto(numero)
    resultado1 = sumar(lista)
    print(lista, '-', resultado1)


