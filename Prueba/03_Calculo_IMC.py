
def alternativa(IMC, Edad):
    if Edad < 45:
        if IMC < 22.0:
            return "Bajo"
        else:
            return "Medio"
    else:
        if IMC>=22.0:
            return "Alto"
        else:
            return "Medio"

def calcula_IMC(Peso, Estatura):
    IMC= (Peso / Estatura**2 )
    return IMC

if __name__ == '__main__':
    estatura= 2.0
    peso= 80
    edad= 38
    imc = calcula_IMC(peso, estatura)
    respuesta = alternativa(imc, edad)
    print(imc , '-', respuesta)



