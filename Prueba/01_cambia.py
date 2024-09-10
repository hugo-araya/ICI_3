
def lee_raw(nombre):
    ent = open(nombre)
    crudo = []
    for linea in ent:
        linea = linea.rstrip('\n')
        crudo.append(linea)
    ent.close()
    return crudo

def cambia(crudo):
    datos = []
    for linea in crudo:
        salida = ''
        i = 0
        while i < len(linea):
            caracter = linea[i]
            if caracter == '"':
                salida = salida + caracter
                i = i + 1
                caracter = linea[i]
                while caracter != '"':
                    if caracter == ',':
                        caracter = ';'
                    salida = salida + caracter
                    i = i + 1
                    caracter = linea[i]
                salida = salida + caracter +','
            i = i + 1
        salida = salida.rstrip(',')
        datos.append(salida)
    return datos

def nuevo(datos):
    for dato in datos:
        print(dato)

if __name__ == "__main__":
    crudo = ['1,"Perez, Sra. Juana Soto",femenino,29,0,0,24160,"Talca, Maule"']
    datos = cambia(crudo)
    nuevo(datos)
