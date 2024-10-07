import sys

def fact_i(n):
    i = 1
    f = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f

def fact_r(n):
    if n == 0:
        return 1
    else:
        return n * fact_r(n-1)

if __name__ == '__main__':
    numero = int(input('Numero: '))
    print('Maximo: ', sys.getrecursionlimit())
    sys.setrecursionlimit(1100)
    resultado = fact_r(numero)
    print('Maximo: ', sys.getrecursionlimit())
    print(resultado)