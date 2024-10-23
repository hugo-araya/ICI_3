class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def imprimir(self):
        print ('Nombre:', self.nombre)

    def __str__(self):
        return self.apellido + " " +self.nombre

if __name__ == '__main__':
    persona1 = Persona("Hugo", "Araya")
    persona1.imprimir()
    persona2 = Persona("Mago", "Valdivia")
    persona2.imprimir()
    print(persona1)