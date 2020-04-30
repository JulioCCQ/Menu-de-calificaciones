#/IMPORTA LA LIBRERIA PANDAS CON UN ALIAS DE PD
import pandas as pd
#/MATERIAS ES  UNA LISTA DE LAS MATERIAS INSERTADAS POR EL USUARIO
materias = []
#/DICC ES UN DICCIONARIO DONDE EL KEY SON LOS ALUMNOS
# Y LOS VALORES ES UNA LISTA CON CALIFICACIONES
dicc = {}

#/FUNCION PARA REGISTRAR ALUMNOS
def reg_alum():
    numero_estudiantes = int(input("Ingrese la cantidad de estudiantes:"))
    print(" ")
    if numero_estudiantes >= 30:
        print("REGISTRO DE ALUMNOS")
        for numero_es in range(0, numero_estudiantes):
            numero_es = numero_es + 1
            print(" ")
            print ("Alumno No.",numero_es,)
            nombre_estudiante = input("Escriba aquí: ")
            dicc[nombre_estudiante]= []
    else:
        print("Mínimo tienen que ser 30 estudiantes.")
        print(" ")
        reg_alum()             
#/FUNCION PARA REGISTRAR MATERIAS
def reg_materias():
    num_arch = 0
    print("REGISTRAR MATERIAS")
    if num_arch == 0:
        num_arch = int(input("Cuantas materias quieres crear: "))
        print(" ")
        if num_arch >= 5:
            for nem in range(0,num_arch):
                nom = input ("Escribe nombre de la materia: ")
                materias.append(nom)
        else:
            print("Mínimo 5 materias")
            reg_materias()
    else:
        print("MATERIAS EXISTENTES")
#/FUNCION PARA REGISTRAR CALIFICACIONES
def reg_cali():
        print(" ")
        print("REGISTRAR CALIFICACIONES")
        for a in dicc:
            print(" ")
            print("Alumno:",a)
            for e in materias:
                print("Materia:",e)
                vec = 0
                vec = int(input("Escribe el Resultado: "))
                dicc[a].append(vec)
                print(" ")
#/FUNCION PARA MOSTRAR EL REGISTRO
def most_reg():
     notas = pd.DataFrame(dicc) #/CREAMOS UN DATA FRAME PARA ORDENAR LOS DATOS
     notas.index= [materias] #/UTILIZAMOS MATERIA COMO INDICE, ENSEGUIDA LO ALTERNAMOS POR NOMBRES
     op2 = 0                 #DE LOS ALUMNOS.
     #/MENU PARA FUNCION MOSTRAR
     while op2 != 4:
         print(" ")
         print("MENU MOSTRAR")
         print("1) CALIFICACIONES ORDENADAS")
         print("2) PROMEDIO DE TODAS LAS MATERIAS")
         print("3) ALUMNOS CON MATERIAS REPROBADAS")
         print("4) Salir")
         opcion2 = input("Elige una opcion: ")
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
             print("SELECCIONE UNA OPCION VALIDA")
#/MENU PRINCIPAL CICLICO
op = 0
while op != 4:
    print(" ")
    print("MENU PRINCIPAL")
    print("1) Registrar Alumnos")
    print("2) Registrar Materias")
    print("3) Registrar Calificaciones")
    print("4) Mostrar Registro")
    print("5) Salir")
    opcion = input("Elige una opcion: ")
#/CONDICIONALES DEL MENU PRINCIPAL
    if opcion == "1":
        reg_alum()
    elif opcion == "2":
        reg_materias()      
    elif opcion == "3":
        reg_cali()
    elif opcion == "4":
        most_reg()
    elif opcion == "5":
        print("Gracias por utilizar nuestra aplicación.")
        exit()
    else:
        print("SELECCIONE UNA OPCION VALIDA")