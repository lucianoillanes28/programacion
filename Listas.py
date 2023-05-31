
edades=[]
personas=[]
continuar="S" #LA VARIABLE DEBE COINCIDIR SI ES MAYUSCULA

while(continuar=="S"):
    varnombre=input("Ingrese su nombre: ")
    personas.append(varnombre)
    varedad=int(input("ingrese la edad: "))
    edades.append(varedad)
    continuar=input("desea continuar S/N: ").upper()

print(personas) #PRINT ECONOMICO Y RAPIDO
print(edades)   #PRINT ECONOMICO Y RAPIDO

for i in range(len(personas)):
    print(f"nombre: {personas[i]} / edad: {edades[i]}")

print("LISTADO DE PERSONAS")
print("-------------------")
print("NOMBRE\t\t EDAD")#LAS \t SON TABULADORES DE ESPACIO PARA QUE HAYA UN ESPACIAMIENTO UNIFORME
print("-------------------")
for i in range(len(personas)):
    print(f"{personas[i]}:\t\t{edades[i]}" )
print("-------------------")