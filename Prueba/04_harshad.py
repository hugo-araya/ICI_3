def suma_digitos(numero):
    suma = 0
    nume = list(str(numero))
    for digito in nume:
        suma = suma + int(digito)
    return suma

def busca_numeros(inicio, fin):
    lista = []
    for nume in range(inicio, fin):
        suma_dig = suma_digitos(nume)
        if (nume % suma_dig) == 0:
            lista.append(nume)
    return lista 

def mostrar_numeros(lista_numeros):
    print(lista_numeros, '-', len(lista_numeros))

def determina_secuencia(lista):
    secuencia = []
    
    return secuencia

if __name__ == '__main__':
    lista_numeros = busca_numeros(10, 10000)
    resultado = determina_secuencia(lista_numeros)
    mostrar_numeros(lista_numeros)
    print(resultado)