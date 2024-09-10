

def sumatoria(m, n, a):
    suma = 0
    i = 0
    while i < m:
        suma = suma + a[i] * n**i
        i = i + 1
    return suma

if __name__ == '__main__':
    n = 15
    a = [1,2,3,4,5]
    m = len(a)
    x = sumatoria(m, n, a)
    print(x)
