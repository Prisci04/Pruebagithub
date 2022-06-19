
#Calcular IVA
def calcular_iva(precio):
    iva = precio * 0.19
    return iva

#Calcular descuento

def calcular_descuento(precio, descuento):
    valor_final = precio - precio * (descuento/100)
    return valor_final

#Calcular imc

def  calcular_imc(peso, estatura):
    imc = peso / estatura**2
    return imc

def obtener_estado(imc):
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc >= 18.5 and imc < 25:
        estado = "Adecuado"
    elif imc >= 25 and imc < 30:
        estado = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        estado = "Obesidad grado 1"
    elif imc >= 35 and imc < 40:
        estado = "Obesidad grado 2"
    else:
        estado = "Obesidad grado 2"
    return estado
    