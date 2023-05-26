from lexer import lexer
import os
print ("Hola este es el analizador Lexico")
print ("Ingrese 1 si quiere ingresar datos a mano y 2 si quiere desde un archivo de prueba \n")
op = input()

if op == "1":                                               #ingreso manual
      print("ingrese lo que quiere analizar")
      cadena = input()    
      lexer.input(cadena)
      while True:
            tok = lexer.token()
            
            if not tok : break
            print (tok)

elif op == "2":                                       #ingreso por archivo
      print("todavia no esta listo")
      n = 0
      
      ejemplo_dir = 'prueba/'                   #elegir el archivo
      with os.scandir(ejemplo_dir) as ficheros:
            ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]    #ficheros es una lista con los archivos de la carpeta prueba
      for i in ficheros:
            
            print(f"{n+1}: {ficheros[n]}")
            n +=1
      print("elegi el archivo pa")
      op2 = input()
      if int(op2) <= n:
            with open(f"prueba/{ficheros[n-1]}","r",encoding="utf-8") as maestro: #esto ya funciona para cualquier fichero en prueba/
                  print("hola abri el archivo jejej")
                  lexer.input(maestro.read())               #lo lee bien pero tira errores raros, despues lo arreglo
                  while True:
                        tok = lexer.token()
    
                        if not tok:break
                        print(tok)
else:
      print("volve a empezar")
