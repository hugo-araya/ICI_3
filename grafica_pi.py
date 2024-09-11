import matplotlib.pyplot as plt
x = []
y = []
ent = open('log.txt')
for linea in ent:
    lista = linea.rstrip('\n').split(';')
    x.append(int(lista[0]))
    y.append(float(lista[1]))
ent.close()
plt.plot(x, y)
plt.show()

