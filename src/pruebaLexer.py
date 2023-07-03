from lexer import lexer
import os
import sys
from lexer import arch
#
# Este es el archivo entregado en la segunda presentacion, se mantiene para probar unicamente la tokenizacion.
#
def borrarPantalla(): #Borra lo ya escrito en pantalla
      if os.name == "posix":
            os.system ("clear")
      elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")
print ("Hola este es el analizador Lexico")
print ("1 para ingresar datos a mano\n2 si quiere cargar datos desde un archivo\n")
op = input()
errores = []
lexico = 0
if op == "1":                                               #ingreso manual
      borrarPantalla()
      while True: #ciclo para ingresar datos hasta que eleccion sea 0
            print("ingrese lo que quiere analizar")
            cadena = input()    
            lexer.input(cadena)
            while True:
                  tok = lexer.token()

                  if not tok : break
                  if tok.type == "ERROR_1" or tok.type == "ERROR_2" or tok.type == "ERROR_3":
                        print(f"error lexico en linea {tok.lineno} ({tok.value})")
                        lexico = 1
                  else:
                        print(tok)
                  if lexico == 0:
                         print("Analisis Lexico exitoso")
              
            print("desea continuar?\n1 para continuar\n0 para terminar")
            eleccion = input()
            if eleccion == "0": break
            borrarPantalla()

elif op == "2":                                       #ingreso por archivo
      n = 0
      dir = 'doc/prueba/'                   #elegir el archivo
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
            with open(f"doc/prueba/{ruta}","r",encoding="utf-8") as maestro: 
                  print(f"abierto archivo: {ruta}")
                  lexer.input(maestro.read())               
                  while True:
                        tok = lexer.token()
                        
                        if not tok:break
                        if tok.type == "error":
                              errores.append(tok.value)
                        if tok.type == "ERROR_1" or tok.type == "ERROR_2" or tok.type == "ERROR_3":
                              print(f"error lexico en linea {tok.lineno} ({tok.value})")
                              lexico = 1
                        else:
                              print(tok)
                  cambio = ruta.replace(".xml","")
                  if lexico == 0:
                        print("Analisis Lexico exitoso")
              
                  with os.scandir('src/html_generados/') as htmls:
                        for k in htmls:
                              if k.name == f"{cambio}.html":
                                    os.remove(f"src/html_generados/{cambio}.html")
                  os.rename("src/html_generados/archivo.html",f"src/html_generados/{cambio}.html" )
                  os.system("pause")
      else:
            print("numero invalido")
            os.system("pause")
else:
      print("volve a empezar")
      os.system("pause")





