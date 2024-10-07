def hanoi(n, com, aux, fin):
    if n == 1:
        print ("Mover desde ", com, " a ", fin)
    else:
        hanoi(n-1, com, fin, aux)
        print ("Mover desde ", com, " a ", fin)
        hanoi(n-1, aux, com, fin)

if __name__=="__main__":
    n = int(input("Cantidad de discos: "))
    hanoi(n, 1, 2, 3)