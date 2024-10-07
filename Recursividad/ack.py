def A(m, n):
    global cont
    cont = cont + 1
    if m == 0 and n != 0:
        return n + 1
    elif m != 0 and n == 0:
        return A(m-1, 1)
    else:
        return A(m-1, A(m, n - 1))

if __name__ == '__main__':
    m = 3
    n = 4
    cont = 0
    resultado = A(m, n)
    print(resultado)
    print(cont)
