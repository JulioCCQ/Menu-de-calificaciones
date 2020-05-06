import pandas as pd
import json

materias = []
dicc = {}

def reg_alum():
    numero_estudiantes = int(input("Ingrese la cantidad de estudiantes:"))
    print(" ")
    if numero_estudiantes >= 30:
        print("* REGISTRO DE ALUMNOS *")
        for numero_es in range(0, numero_estudiantes):
            numero_es = numero_es + 1
            print(" ")
            print("*****")
            print ("Alumno No.",numero_es)
            nombre_estudiante = input("Escriba aquí: ")
            dicc[nombre_estudiante]= []
    else:
        print("Mínimo tienen que ser 30 estudiantes.")
        print(" ")
        reg_alum()             

def reg_materias():
    num_arch = 0
    print(" ")
    print("* REGISTRO DE MATERIAS *")
    num_arch = int(input("Cuantas materias quieres crear: "))
    if num_arch >= 5:
        for nem in range(0,num_arch):
            nem = nem + 1
            print("**********")
            print("Nombre de la materia",nem,":")
            nom = input ("Escriba aquí: ")
            materias.append(nom)
            print(" ")

    else:
        print("Mínimo 5 materias")
        reg_materias()

def reg_cali():
        print(" ")
        print("REGISTRAR CALIFICACIONES")
        alumn_num = 0
        for a in dicc:
            alumn_num = alumn_num + 1
            print("********")
            print("Alumno No.",alumn_num)
            print("Nombre:",a)
            for e in materias:
                print("Materia:",e)
                vec = 0
                vec = int(input("Escribe el Resultado: "))
                dicc[a].append(vec)
                print(" ")

def most_reg():
     notas = pd.DataFrame(dicc)
     notas.index= [materias] 
     op2 = 0                 
     while op2 != 4:
         print(" ")
         print("*************")
         print("MENU MOSTRAR")
         print("1) CALIFICACIONES ORDENADAS")
         print("2) PROMEDIO DE TODAS LAS MATERIAS")
         print("3) ALUMNOS CON MATERIAS REPROBADAS")
         print("4) Volver al Menú Principal")
         opcion2 = input("Elige una opcion: ")
         print("*************")
         if opcion2 == "1":
             print(" ")
             print("CALIFICACIONES")
             print(" ")
             print(notas.T)  #/ALTERNA LA MATERIA POR NOMBRE COMO INDICE PARA MEJOR VISION
         elif opcion2 == "2": 
             print(" ")
             print("PROMEDIO DE MATERIAS")
             print(" ")
             print(notas.T.mean())  #/HACE EL PROMEDIO EN BASE A LAS NOTAS DE CADA MATERIA
         elif opcion2 == "3":
             print("ALUMNOS CON MÁS DE DOS MATERIAS REPROBADAS")
             valor2 = dicc.keys()
             for a in valor2:
                 valor = dicc.get(a,())
                 print(" ")
                 print("Alumno:",a)
                 print("Notas Reprobadas")
                 for e in valor: #/FILTRO PARA EXTRAER CALIFICACIONES REPROBADAS
                     if e < 70:
                         print(e)
         elif opcion2 == "4":
             op2 = 4
         else:
             print("Atención! Seleccione una opción válida.")
             
def exportar_reg():
    notas = pd.DataFrame(dicc) #/Exportamos a CSV y JSON
    notas.index= [materias]
    notas_nuevas = notas.T
    op3 = 0
    while op3 != 3:
        print(" ")
        print("*************")
        print("MENU EXPORTAR")
        print("1) Exportar Registro a CSV")
        print("2) Exportar Registro a JSON")
        print("3) Volver al Menú Principal")
        opcion3 = input("Elige una opcion: ")
        print(" ")
        if opcion3 == "1":
            notas_nuevas.to_csv (r'Actividad 2 CSV.csv', index=True, header=True)
            print("Exportación a CSV realizada con éxito!")
        elif opcion3 == "2":
            notas.to_json('Actividad 2 JSON.json', orient="index") 
            print("Exportación a JSON realizada con éxito!")
        elif opcion3 == "3":
            op3 = 3
        else:
            print("Atención! Seleccione una opción válida.")
            
def reporte_estadistico():
    notas = pd.DataFrame(dicc)
    notas.index= [materias]
    op4 = 0
    while op4 != 4:
        print(" ")
        print("*************")
        print("MENU REPORTE ESTADISTICO")
        print("1) Reporte por Materia")
        print("2) Reporte por Alumno")
        print("3) Exportar Reportes a un Archivo de Texto")
        print("4) Volver al Menú Principal")
        opcion4 = input("Elige una opcion: ")
        print(" ")
        if opcion4 == "1":
            print("REPORTE POR MATERIA")
            print(notas.T.describe()) 
        elif opcion4 == "2":
            print("REPORTE POR ALUMNO")
            for e in dicc:
                print(" ")
                print("Alumno:",e)
                describiendo = notas[e].describe()
                print(describiendo)

        elif opcion4 == "3":
            archivo = open('Reporte Estadistico Act 2.txt','a')
            archivo.write('REPORTE POR MATERIA\n')
            rep_por_alumn = str(notas.T.describe())
            archivo.write(rep_por_alumn)
            archivo.write(' \n')
            archivo.write(' \n')
            archivo.write('REPORTE POR ALUMNO\n')
            for e in dicc:
                describiendo = notas[e].describe()
                print(describiendo)
                enstr = str(describiendo)
                archivo.write(enstr)
            print(" ")
            print("Reporte Generado con éxito!")
        
        elif opcion4 == "4":
            op4 = 4 
        else:
            print("Atención! Seleccione una opción válida.")
      
op = 0
while op != 7:
    print(" ")
    print("**********")
    print("Menu Principal")
    print("1) Registrar Alumnos")
    print("2) Registrar Materias")
    print("3) Registrar Calificaciones")
    print("4) Mostrar Registro")
    print("5) Exportar Registro")
    print("6) Reporte Estadistico")
    print("7) Salir")
    opcion = input("Elige una opcion: ")
    print("**********")

    if opcion == "1":
        reg_alum()
    elif opcion == "2":
        reg_materias()      
    elif opcion == "3":
        reg_cali()
    elif opcion == "4":
        most_reg()
    elif opcion == "5":
        exportar_reg()
    elif opcion == "6":
        reporte_estadistico()
    elif opcion == "7":
        print("Gracias por utilizar nuestra aplicación.")
        exit()
    else:
        print("SELECCIONE UNA OPCION VALIDA")