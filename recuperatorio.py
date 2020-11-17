import csv
import os




def pedirNombre():
    while True:
        nombre = input("\n\tingrese nombre del archivo:  ")
        try:
            return str(f"{nombre}.csv")
        except ValueError:
            print("error al nombrar archivo")


def cargarDatos():
    modo = ""
    campos = ['Legajo','Apellido','Nombre']
    guardar = "si"
    filaCargada = []

    while guardar == "si":
        empleadosCargado = {}

        for campo in campos:
            empleadosCargado[campo] = input(f"Ingrese {campo} del Empleado: ")
        filaCargada.append(empleadosCargado)
        guardar = input("\tDesea seguir agregando empleados? Si/No:  ")


    try:
        archivo = pedirNombre()
        hayAlgunArchivo = os.path.isfile(archivo)
        verificarExistencia = os.path.exists(archivo)
        if verificarExistencia:
            print("el archivo ya existe. desea Agregar los registros al final del archivo existente? ")
            opcion = input("\tsi/no:  ")
            if opcion == "si":
                with open(archivo, 'a', newline='') as file:
                    archivoAGrabar = csv.DictWriter(file, fieldnames=campos)

                    if not hayAlgunArchivo:
                        archivoAGrabar.writeheader()

                    archivoAGrabar.writerows(filaCargada)
                    print("Empleado Cargado Exitosamente!")
                    return
            if opcion == "no":
                with open(archivo, 'w', newline='') as file:
                    archivoAGrabar = csv.DictWriter(file, fieldnames=campos)

                    if not hayAlgunArchivo:
                        archivoAGrabar.writeheader()

                    archivoAGrabar.writerows(filaCargada)
                    print("Empleado Cargado Exitosamente! Se eliminaron los registros anteriores, Se sobreescribio el archivo!")
                    return
        if not verificarExistencia:
            print("el archivo NO existe. desea crearlo?:  ")
            opcion = input("\tsi/no:  ")
            if opcion == "si":
                with open(archivo, 'a', newline='') as file:
                    archivoAGrabar = csv.DictWriter(file, fieldnames=campos)

                    if not hayAlgunArchivo:
                        archivoAGrabar.writeheader()

                    archivoAGrabar.writerows(filaCargada)
                    print("Empleado Cargado Exitosamente! - Se Creó el archivo!")
                    return
            if opcion == "no":
                print("Se optó por no crear el archivo! ")
                return
    except IOError:
        print("no se reconoce el archivo.")



#------------------------------------------------------
#opcion 2

def recupero(archivo):
   verificarExistencia = os.path.exists(archivo)
   archivo2 = "legajo.csv"
   try:
       with open(archivo, 'r', newline='') as file:
         with open(archivo2, "r", newline='') as file2:
           fileCSV = csv.reader(file)
           file2CSV = csv.reader(file2, delimiter=";")

           itemEmpleados = next(file2, None)
           itemLegajos = next(file, None)
           busqueda = input("legajo a buscar: ")

           contador = 0


           numeroLegajo = 0
           for linea in fileCSV:

             if busqueda in linea[0]:

                 print(f"Legajo {linea[0]},{linea[2]} {linea[1]}")


                 for vuelta in file2CSV:

                   numeroLegajo = int(vuelta[0])



                   if busqueda in vuelta[0]:
                      contador += int(vuelta[1])




       montoSuperado = 0
       MONTOMENSUAL = 5000
       montoSuperado = contador - MONTOMENSUAL

       if contador > MONTOMENSUAL:

           print(f'\tGastó: {contador} pesos, se ha pasado del presupuesto {montoSuperado}')
           print("\t*******************************")
       else:

           print(f'\tGastó: {contador} pesos')
           print("\t********************************")

   except IOError:
       print("Hubo un error al abrir el archivo, es posible que no exista o este mal escrito.")
   except ValueError:
       print("Debe ingresar un entero!")



def main():


    while True:
        print("----------------------------------------------------------")
        print("\tElija una opcion:\n\t 1.Cargar datos de Empleados: \n\t 2.Consulta Gastos por Viatico: \n\t 3.Salir: ")
        opcion = input("")


        if opcion == "1":


            cargarDatos()


        if opcion == "2":
            archivo = input("ingrese nombre del archivo a recuperar: ")
            try:
                recupero(f"{archivo}.csv")
            except IOError:
                print("error de lectura I/O")
            


        if opcion == "3":
            exit()
        else:
            print("elija una opcion valida")
main()
