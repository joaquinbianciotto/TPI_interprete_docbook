import ply.lex as lex
import re
import codecs
import os
import sys


tokens = [ 'APERTURAARTICULO', 'CIERREARTICULO' , 'APERTURAPARRAFO', 'CIERREPARRAFO', 'TEXTO' 
		]

t_ignore = '\t '   #nose que hace pero vi en varios, creo q ignora espacios en blanco o tabulacion
t_APERTURAARTICULO = r'<article>'
t_CIERREARTICULO = r'</article>'
t_APERTURAPARRAFO = r'<para>'
t_CIERREPARRAFO = r'</para>'



def t_TEXTO (t):
    r'[a-zA-Z][a-zA-Z0-9]*'  #falta ver caraxteres especiales
    return (t)
def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)
	
print ("Hola este es el analizador Lexico")
print ("Ingrese el codigo a analizar \n")
cadena = ''
while True:
	cad = input()
	cadena = cadena+cad+ '\n'
	break
	if not cadena: continue
	print ('\n')	
lexer = lex.lex()
#ciclo para mostrar tokens 
lexer.input(cadena)
while True:
    tok = lexer.token()
    if not tok : break
    print (tok)

