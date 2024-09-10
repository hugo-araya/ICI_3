
import math

def pi_Leibniz(fin):
    n = 0
    suma = 0
    while n < fin:
        suma = suma + (-1)**n / (2*n + 1)
        n = n + 1
    return suma

def pi_Wallis(fin):
    n = 1
    prod = 1
    while n < fin:
        prod = prod * (2*n/(2*n-1))*(2*n/(2*n+1))
        n = n + 1
    return prod

def calcula_pi(valor, numero):
    return valor * numero

def facto(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f

def pi_Euler(fin):
    n = 0
    suma = 0
    while n < fin:
        suma = suma + (2**n * facto(n)**2)/facto(2*n + 1)
        n = n + 1
    return suma

if __name__ == '__main__':
    fin = 5000
    p_Leibniz = pi_Leibniz(fin)
    pipi = calcula_pi(p_Leibniz, 4)
    print("Leibniz: ", pipi)
    p_Wallis = pi_Wallis(fin)
    pipi = calcula_pi(p_Wallis, 2)
    print("Wallis : ", pipi)
    p_Euler = pi_Euler(fin)
    pipi = calcula_pi(p_Euler, 2)
    print("Euler  : ",pipi)
    print("Python : ",math.pi)
