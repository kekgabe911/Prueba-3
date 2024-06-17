import csv
plan=[]
listaplanes=[]
def porcentaje(x):
    valido=False
    if x>0 and x<=100:
        valido=True
    else:
        valido=False
    return valido
def categoria(x):
    catego=''
    if x>=0 and x<=25:
        catego='Chiste'
    if x>=26 and x<=50:
        catego='Anécdota'
    if x>=51 and x<=75:
        catego='Peligro'
    if x>=76 and x<=99:
        catego='Atencion'
    if x==100:
        catego='Esclavitud'
    return catego
def promedio(e):
    ac=0
    prom=0
    for x in listaplanes:
        ac=ac+x[2]
    cant=len(listaplanes)
    prom=ac/cant
    print(f'El promedio de goles es de {prom}')
def mayor(e):
    for x in listaplanes:
        mayor=0
        if mayor<x[2]:
            mayor=x[2]
    print(f'El mayor porcentaje fue de {mayor}')       
try:
    while True:
        print("---Menú---")
        print("1.- Agregar Plan.")
        print("2.- Lista de Planes.")
        print("3.- Eliminar Plan por ID.")
        print("4.- Generar bbdd.")
        print("5.- Cargar Archivo bbdd.")
        print("6.- Estadisticas.")
        print("0.- Salir.")
        op=int(input("Ingrese su opcion: "))
        
        if op==1:
            print("--Agregar Plan--")
            planid=int(input("Ingrese su id de plan: "))
            nombre=input("Ingrese Nombre del plan: ")
            porcent=int(input("Ingrese porcentaje de efecividad: "))
            valido=porcentaje(porcent)
            if valido:
                print("Porcentaje del plan valido.")
            else:
                print("Porcentaje del plan invalido")
                porcent=int(input("Ingrese porcentaje de efecividad: "))
                valido=porcentaje(porcent)
            cate=categoria(porcent)
            plan=[planid,nombre,porcent,cate]
            listaplanes.append(plan)   
        elif op==2:
            print("--Lista de Planes--")
            for x in listaplanes:
                print(f'Id: {x[0]} Nombre: {x[1]} Porcentaje: {x[2]} Categoria: {x[3]}')
            print("\n")       
        elif op==3:
            print("--Eliminar Plan por ID--")
            n1=int(input("Ingrese ID del plan: "))
            for x in listaplanes:
                if n1==x[0]: 
                    print(f'Id: {x[0]} Nombre: {x[1]} Porcentaje: {x[2]} Categoria: {x[3]}')
                    preg=input("¿Desea Eliminar plan?")
                    preg.lower()
                    if preg=='si' or preg=='s':
                        listaplanes.remove(x)
                        print("Se ha eliminado correctamente.")
                        break
                    else:
                        print("Proceso cancelado...")
                        break
        elif op==4:
            print("--Generar bbdd--")
            with open ('planes.csv','w',newline='') as planes_csv:
                escritor_csv=csv.writer(planes_csv)
                escritor_csv.writerow('Id','Nombre','Porcentaje','Categoria')
                escritor_csv.writerows(listaplanes)
                print("Archivo Guardado")
        elif op==5:
            print("--Cargar Archivo bbdd--")
            print('\n')
            listaplanes.clear()
            cont=0
            with open ('planes.csv','r',newline='') as planes_csv:
                lector_csv=csv.reader(planes_csv)
                for row in lector_csv:
                    if cont==0:
                        cont=cont+1
                        continue
                    planid=int(row[0])
                    nombre=row[1]
                    porcent=int(row[2])
                    cate=row[3]
        elif op==6:
            print("--Estadisticas--")
            promedio(listaplanes)
            mayor(listaplanes)
        elif op==0:
            print("Finalizando Programa...")
            break
        else:
            print("Ingrese opcion valida.")
except:
    print("Ha ocurrio un error.")
