def inicializar():
    elemento = 0
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return elemento, lista

def busqueda(elemento, lista):
    ini = 0
    fin = len(lista) - 1
    ok = False
    while ini <= fin and ok == False:
        piv = (fin + ini) // 2
        if lista[piv] == elemento:
            ok = True
        elif elemento < lista[piv]:
            fin = piv - 1
        else:
            ini = piv + 1
    return ok

def mostrar(resultado, elemento):
    if resultado:
        print('El elemento ', elemento, 'existe')
    else:
        print('El elemento ', elemento, 'NO existe')

if __name__ == '__main__':
    elemento, lista = inicializar()
    resultado = busqueda(elemento, lista)
    mostrar(resultado, elemento)
