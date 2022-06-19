import funcionesS as fn


flag = True

while flag:
    print("1: Calcular IVA")
    print("2: Calcular descuento")
    print("3: Calcular IMC")
    print("4: Salir")
    
    try:
        opc = int(input("Ingrese opción:\n"))
        
        if opc == 1:
            print("Calcular IVA")
            precio = int(input("Ingrese precio: "))
            iva = fn.calcular_iva(precio)
            print(f"El IVA de {precio} es: {iva}")
            print("---------------------")
            
        elif opc == 2:
            print("Calcular descuento")
            precio = int(input("Ingrese precio: "))
            porcentaje = int(input("Ingrese dexuento: %"))
            precio_pagar = fn.calcular_descuento(precio, porcentaje)
            print(f"El precio es {precio}, su descuento es {porcentaje}%")
            print(f"Total a pagar: ${precio_pagar}")
            print("--------------------------")
            
            
        elif opc == 3:
            print("Calcular IMC")
            peso = float(input("Ingrese su pes en kg: "))
            estatura = float(input("Ingrese su estatura en m: "))
            imc= fn.calcular_imc(peso, estatura)
            estado= fn.obtener_estado(imc)
            print(f"Su peso es: {peso}")
            print(f"Su IMC es: {imc}")
            print(f"Su estado: {estado}")
            print("---------------------------")
            
        elif opc == 4:
            flag = False
        else:
            print("Ingrese un número entre 1 y 4\n")
        

    except:
        print("\nIngrese un número entero!!\n")