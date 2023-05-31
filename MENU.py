listanombres=[]
listaedades=[]
while(True):
    print("MENU")
    print("1. Registrar")
    print("2. Listar")
    print("3. Ver promedio de edad")
    print("4. Salir")
    opcion=int(input("Ingrese su opcion (1-4): "))
    if (opcion==1):
        varnombre=input("Ingrese el nombre de la persona: ")
        listanombres.append(varnombre)
        varedad=int(input("Ingrese la edad de la persona: "))
        listaedades.append(varedad)
    if (opcion==2): #agregar tabulador ver codigo listas
        print(listanombres)
        print(listaedades)
    if (opcion==3):
        print("Obteniendo el promedio.........")
        acum=0
        for i in range(len(listaedades)):
            acum=acum+listaedades[i]
        prom=acum/len(listaedades)
        print(f"el promedio es: {prom}")
    if (opcion==4):
        break

