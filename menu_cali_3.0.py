import pandas as pd
import json
import sys
import sqlite3
from sqlite3 import Error


materias = []
dicc = {}

def reg_alum():
    try:
        print("***************")
        print("* Presione la tecla ""1"" para regresar       *")
        print("* Presione la tecla ""2"" para editar alumnos *")
        print("***************")
        print("Ingrese la cantidad de estudiantes a registrar")
        numero_estudiantes = int(input("Escriba aquí: "))
        print(" ")
        if numero_estudiantes >= 30:
            print("*********")
            print("* REGISTRO DE ALUMNOS *")
            print("*********")
            try:
                with sqlite3.connect("Actividad 3.db") as conn:
                    c = conn.cursor()
                    c.execute("CREATE TABLE IF NOT EXISTS alumno (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
                    for numero_es in range(0, numero_estudiantes):
                        numero_es = numero_es + 1
                        print(" ")
                        print("*****")
                        print ("Alumno No.",numero_es)
                        nombre_estudiante = input("Escriba aquí: ")
                        dicc[nombre_estudiante]= []
        
                        valores = {"clave":numero_es, "nombre":nombre_estudiante}
                        c.execute("INSERT INTO alumno VALUES(:clave,:nombre)", valores)
            finally:
                conn.close()
                
        elif numero_estudiantes == 1:
            pass
        elif numero_estudiantes == 2:
            continuar = True
            while continuar:
                print("")
                print("******************************")
                print("* Proporcione los datos del alumno a EDITAR, capture la clave 0 (cero) para terminar *")
                print("******************************")
                campo_clave = int(input("Clave del alumno a editar: "))
                if campo_clave == 0:
                    continuar = False
                    print("")
                else:
                    editar_alumno(campo_clave)
            
        else:
            print("Atención! Mínimo 30 estudiantes.")
            input("Para continuar, presione cualquier tecla")
            print(" ")
            reg_alum()  

    except ValueError:
        print(" ")
        print("Atención! Introduzca un valor númerico")
        input("Para continuar, presione cualquier tecla")
        print(" ")
        reg_alum()      
#
def reg_materias():
    try:
        num_arch = 0
        print(" ")
        print("****************")
        print("* Presione la tecla ""1"" para regresar        *")
        print("* Presione la tecla ""2"" para editar materias *")
        print("****************")
        print("Inserte número de materias a crear")
        num_arch = int(input("Escriba aquí: "))
        if num_arch >= 5:
            try:
                with sqlite3.connect("Actividad 3.db") as conn:
                    c = conn.cursor()
                    c.execute("CREATE TABLE IF NOT EXISTS materia (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
                    for nem in range(0,num_arch):
                        nem = nem + 1
                        print("**********")
                        print("Nombre de la materia",nem,":")
                        nom = input ("Escriba aquí: ")
                        materias.append(nom)
                        print(" ")
                        nam = nem + 99
                        valores = {"clave":nam, "nombre":nom}
                        c.execute("INSERT INTO materia VALUES(:clave,:nombre)", valores)
            finally:
                conn.close()          
        elif num_arch == 1:
            pass
        elif num_arch == 2:
            continuar = True
            while continuar:
                print("")
                print("*******************************")
                print("* Proporcione los datos de la materia a EDITAR, capture la clave 0 (cero) para terminar *")
                print("*******************************")
                campo_clave = int(input("Clave de la materia a editar: "))
                if campo_clave == 0:
                    continuar = False
                    print("")
                elif campo_clave in range (1,100):
                    print("Clave no valida vuelva a intentar")
                else: 
                    editar_materia(campo_clave)   
        else:
            print("Atención! Mínimo 5 materias")
            input("Para continuar, presione cualquier tecla")
            reg_materias()
    except ValueError:
        print("Atención! Introduzca un valor númerico")
        input("Para continuar, presione cualquier tecla")
        print(" ")
        reg_materias()
        print(" ")

def reg_cali():
    try:
        print(" ")
        print("**********")
        print("* REGISTRAR CALIFICACIONES *")
        print("**********")
        alumn_num = 0
        try:
            with sqlite3.connect("Actividad 3.db") as conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS calificacion (alumno INTERGET NOT NULL,materia INTEGER NOT NULL,calificacion INTERGER NOT NULL, FOREIGN KEY(materia) REFERENCES materia(clave),FOREIGN KEY(alumno) REFERENCES alumno(clave));")
                for a in dicc:
                    alumn_num = alumn_num + 1
                    print("********")
                    print("Alumno No.",alumn_num)
                    print("Nombre:",a)
                    mat_num = 99
                    for e in materias:
                        mat_num = mat_num + 1
                        print("Materia:",e)
                        try:
                            vec = 0
                            vec = int(input("Escribe el Resultado: "))
                            dicc[a].append(vec)
                            valores = {"alumno":alumn_num, "materia":mat_num, "calificacion":vec}
                            c.execute("INSERT INTO calificacion VALUES(:alumno,:materia,:calificacion)", valores)
                            print(" ")
                            
                        except ValueError:
                            print("Atención! Introduzca un valor númerico")
                            print(" ")
                            print("Materia:",e)
                            vec2 = 0
                            vec2 = int(input("Escribe el Resultado: "))
                            dicc[a].append(vec2)    
                            valores = {"alumno":alumn_num, "materia":mat_num, "calificacion":vec2}
                            c.execute("INSERT INTO calificacion VALUES(:alumno,:materia,:calificacion)", valores)                                       
        finally:
            conn.close()
                        
    except ValueError:
        print("Atención! Faltan datos por registrar")

def most_reg():
    try:
        notas = pd.DataFrame(dicc)
        notas.index= [materias] 
        op2 = 0                 
        while op2 != 4:
            print(" ")
            print("******")
            print("* MENU MOSTRAR *")
            print("******")
            print("1) CALIFICACIONES ORDENADAS")
            print("2) PROMEDIO DE TODAS LAS MATERIAS")
            print("3) ALUMNOS CON MATERIAS REPROBADAS")
            print("4) REGISTRO EN SQL")
            print("5) Volver al Menú Principal")
            opcion2 = input("Elige una opcion: ")
            print("******")
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
                try:
                    with sqlite3.connect("Actividad 3.db") as conn:
                        c = conn.cursor()
                        c.execute('SELECT * FROM calificacion')
                        data = c.fetchall()
                        for row in data:
                            print(row)
                except Error as e:
                    print(e)
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                    conn.close()
                
            elif opcion2 == "5":
                op2 = 4
            else:
                print("Atención! Seleccione una opción válida.")
                input("Para continuar, presione cualquier tecla")
    except ValueError:
        print("Atención!, Faltan datos por registrar")
             
def exportar_reg():
    notas = pd.DataFrame(dicc) #/Exportamos a CSV y JSON
    notas.index= [materias]
    op3 = 0
    while op3 != 3:
        print(" ")
        print("*******")
        print("* MENU EXPORTAR *")
        print("*******")
        print("1) Exportar Registro a CSV")
        print("2) Exportar Registro a JSON")
        print("3) Volver al Menú Principal")
        opcion3 = input("Elige una opcion: ")
        print(" ")
        if opcion3 == "1":
            notas_nuevas = notas.T
            notas_nuevas.to_csv (r'Actividad 2 CSV.csv', index=True, header=True)
            print("Exportación a CSV realizada con éxito!")
        elif opcion3 == "2":
            notas.to_json('Actividad 2 JSON.json', orient="table") 
            print("Exportación a JSON realizada con éxito!")
        elif opcion3 == "3":
            op3 = 3
        else:
            print("Atención! Seleccione una opción válida.")
            input("Para continuar, presione cualquier tecla")
            
def reporte_estadistico():
    notas = pd.DataFrame(dicc)
    notas.index= [materias]
    op4 = 0
    while op4 != 4:
        print(" ")
        print("**********")
        print("* MENU REPORTE ESTADISTICO *")
        print("**********")
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
                archivo.write(' \n')
                archivo.write(' \n')
            print(" ")
            print("Reporte Generado con éxito!")
        
        elif opcion4 == "4":
            op4 = 4 
        else:
            print("Atención! Seleccione una opción válida.")
            input("Continuar, presione cualquier tecla")
            

def editar_alumno(campo_clave): #SQlite alumno
    try:
        with sqlite3.connect("Actividad 3.db") as conn:
            c = conn.cursor()
            nueva_c = int(input("Clave nueva del alumno a agregar: "))
            nuevo_n = input("Nombre nuevo del alumno a agregar: ")
            
            valores = {"valor_clave":campo_clave,"nueva_clave":nueva_c,"nombre_nuevo":nuevo_n}
            
            c.execute("UPDATE alumno SET clave = :nueva_clave, nombre = :nombre_nuevo WHERE clave = :valor_clave;",valores)
            print("* ALUMNO EDITADO EXITOSAMENTE *")
            print("")
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
        
def editar_materia(campo_clave): #SQlite materia
    try:
        with sqlite3.connect("Actividad 3.db") as conn:
            c = conn.cursor()
            nueva_c = int(input("Clave nueva de la materia a agregar: "))
            if nueva_c > 99:
                nuevo_n = input("Nombre nuevo de la materia a agregar: ")
                valores = {"valor_clave":campo_clave,"nueva_clave":nueva_c,"nombre_nuevo":nuevo_n}
                c.execute("UPDATE materia SET clave = :nueva_clave, nombre = :nombre_nuevo WHERE clave = :valor_clave;",valores)
                print("* MATERIA EDITADA EXITOSAMENTE *")
                print("")
            else:
                print("Clave no valida, intente de nuevo!")
                editar_materia(campo_clave)
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close() 
op = 0
while op != 7:
    print(" ")
    print("******")
    print("* Menu Principal *")
    print("******")
    print("1) Registrar Alumnos")
    print("2) Registrar Materias")
    print("3) Registrar Calificaciones")
    print("4) Mostrar Registro")
    print("5) Exportar Registro")
    print("6) Reporte Estadistico")
    print("7) Salir")
    opcion = input("Elige una opcion: ")

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
        print("                ,;;;,   ,;;;,  ")
        print("               ;;;;;;;,;;;;;;; ")
        print("      .:::.   .::::;;;;;;;;;;; ")
        print("     :::::::.:::::::;;;;;;;;;' ")
        print("     :::::::::::::::;;;;;;;'   ")
        print("     ':::::::::::::';;;;;'     ")
        print("       ':::::::::'   ';'       ")
        print("         ':::::'               ")
        print("           ':'                 ")
        exit()
    else:
        print("Atención! Seleccione una opción válida.")
        input("Para continuar, presione cualquier tecla")