continuar = "si"  

while continuar == "si":
    print("Buenas señor usuario, te vamos a decir que tan saludable estás de acuerdo a tu índice de masa corporal")
    Nombre = input("Por favor deme sus nombres: ")
    Peso = int(input("Por favor deme su peso: "))
    Estatura = float(input("Por favor deme su estatura: "))

    IndiceMasa = (Peso / (Estatura * Estatura))
    saludable = 24.9
    riesgo = 35.0

    print ("----------------------------------------------------------------------------------")
    if IndiceMasa >= riesgo:
        print("Su estado de salud es riesgoso, debido a que sobrepasas el índice.")
        print("Buenas señor, sus nombres son: " + Nombre + " y su indice de masa corporal es: " + str(IndiceMasa))
    elif IndiceMasa >= saludable: 
        print("Su estado de salud es moderado, debido a que estás en un punto medio del índice.")
        print("Buenas señor, sus nombres son: " + Nombre + " y su indice de masa corporal es: " + str(IndiceMasa))
    else:
        print("Su estado de salud es saludable, debido a que estás en el índice correctamente.")
        print("Buenas señor, sus nombres son: " + Nombre + " y su indice de masa corporal es: " + str(IndiceMasa))

    print ("----------------------------------------------------------------------------------")
    continuar = input("Desea agregar otra persona al programa (si o no) ")
    print ("Gracias por utiizar el programa señor usario")
