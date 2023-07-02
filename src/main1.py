
from parser1 import parser
import os
import sys
from lexer import arch


def borrarPantalla(): #Borra lo ya escrito en pantalla
      if os.name == "posix":
            os.system ("clear")
      elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")

print ("Hola este es el analizador Sintactico")
print ("1 para ingresar datos a mano\n2 si quiere cargar datos desde un archivo\n")
op = input()
errores = []
if op == "1":                                               #ingreso manual
    borrarPantalla()
    while True: #ciclo para ingresar datos hasta que eleccion sea 0
        print("ingrese lo que quiere analizar")
        cadena = input()   
        parser.parse(cadena)
        from parser1 import correcto
        if correcto == 0:
            print("sintaxis correcta")
        print("desea continuar?\n1 para continuar\n0 para terminar")
        eleccion = input()
        if eleccion == "0": break
        borrarPantalla()
    arch.close()
elif op == "2":                                       #ingreso por archivo
    n = 0
    dir = 'prueba/'                   #elegir el archivo
    with os.scandir(dir) as ficheros:
        print(type(ficheros))
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]    #ficheros es una lista con los archivos de la carpeta prueba
    for j in ficheros:
        if ".txt" in j:
            ficheros.remove(f"{j}")
    for i in ficheros:
            
        print(f"{n+1}: {ficheros[n]}")
        n +=1
    print("elegi el archivo para leer")
    op2 = input()
    borrarPantalla()
    if int(op2) <= n:
        ruta = ficheros[int(op2)-1]
        with open(f"prueba/{ruta}","r",encoding="utf-8") as maestro: #esto ya funciona para cualquier fichero en prueba/
            parser.parse(maestro.read())
            from parser1 import correcto
            if correcto == 0:
                print("sintaxis correcta")
            arch.close()
            cambio = ruta.replace(".xml","")
            with os.scandir('src/html_generados/') as htmls:
                for k in htmls:
                        if k.name == f"{cambio}.html":
                            os.remove(f"src/html_generados/{cambio}.html")
            os.rename("src/html_generados/archivo.html",f"src/html_generados/{cambio}.html" )
            input("Pulsa cualquier tecla para continuar...")
    else:
        print("numero invalido")
        input("Pulsa cualquier tecla para continuar...")
else:
      print("volve a empezar")
      input("Pulsa cualquier tecla para continuar...")


                  
                