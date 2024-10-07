def fib_i(n):
    pri = 0
    seg = 1
    i = 2
    while i <= n:
        ter = pri + seg
        pri = seg
        seg = ter
        i = i + 1
    return ter

def fib_r(n):
    global cont
    cont = cont + 1
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)

if __name__ == '__main__':
    n = 40
    cont = 0
#    resultado_i = fib_i(n)
    resultado_r = fib_r(n)
#    print(resultado_i)
    print(resultado_r)
    print(cont)