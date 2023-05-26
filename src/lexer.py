import ply.lex as lex
import re
import codecs
import os
import sys
error_caracter_ilegal=[]

tokens = [ 'DT1','DT2','APERTURA_ARTICLE', 'CIERRE_ARTICLE' , 'APERTURA_PARA', 'CIERRE_PARA', 'TEXTO', 
          'APERTURA_INFO' , 'CIERRE_INFO' , 'APERTURA_TITLE' , 'CIERRE_TITLE' , 'APERTURA_ITEMIZEDLIST',
          'CIERRE_ITEMIZEDLIST', 'APERTURA_IMPORTANT' , 'CIERRE_IMPORTANT' , 'APERTURA_SIMPARA',
          'CIERRE_SIMPARA' , 'APERTURA_ADDRESS' , 'CIERRE_ADDRESS' , 'APERTURA_MEDIAOBJECT' , 'CIERRE_MEDIAOBJECT' , 
          'APERTURA_INFORMALTABLE' , 'CIERRE_INFORMALTABLE' , 'APERTURA_COMMENT' , 'CIERRE_COMMENT' , 
          'APERTURA_ABSTRACT' , 'CIERRE_ABSTRACT' , 'APERTURA_SECTION' , 'CIERRE_SECTION' , 'APERTURA_SIMPLESECT' ,
          'CIERRE_SIMPLESECT' , 'APERTURA_EMPHASIS' , 'CIERRE_EMPHASIS' , 'APERTURA_LINK' , 'CIERRE_LINK' , 
          'APERTURA_FIRSTNAME' , 'CIERRE_FIRSTNAME' , 'APERTURA_SURNAME' , 'CIERRE_SURNAME' , 'APERTURA_STREET' , 
          'CIERRE_STREET' , 'APERTURA_CITY' , 'CIERRE_CITY' , 'APERTURA_STATE' , 'CIERRE_STATE' , 'APERTURA_PHONE' , 
          'CIERRE_PHONE' , 'APERTURA_EMAIL' , 'CIERRE_EMAIL' , 'APERTURA_DATE' , 'CIERRE_DATE' , 'APERTURA_YEAR' , 
          'CIERRE_YEAR' , 'APERTURA_HOLDER' , 'CIERRE_HOLDER'
		]

t_ignore = '\t '   #nose que hace pero vi en varios, creo q ignora espacios en blanco o tabulacion


t_APERTURA_ARTICLE = r'<article>'
t_CIERRE_ARTICLE = r'</article>'
#t_APERTURA_INFO = r'<info>'
#t_CIERRE_INFO = r'</info>'
#t_APERTURA_TITLE = r'<title>'
#t_CIERRE_TITLE = r'</title>'
t_APERTURA_ITEMIZEDLIST = r'<itemizedlist>'
t_CIERRE_ITEMIZEDLIST = r'</itemizedlist>'
t_APERTURA_IMPORTANT = r'<important>'
t_CIERRE_IMPORTANT = r'</important>'
t_APERTURA_SIMPARA = r'<simpara>'
t_CIERRE_SIMPARA = r'</simpara>'
t_APERTURA_ADDRESS = r'<address>'
t_CIERRE_ADDRESS = r'</address>'
t_APERTURA_MEDIAOBJECT = r'<mediaobject>'
t_CIERRE_MEDIAOBJECT = r'</mediaobject>'
t_APERTURA_INFORMALTABLE = r'<informaltable>'
t_CIERRE_INFORMALTABLE = r'</informaltable>'
t_APERTURA_COMMENT = r'<comment>'
t_CIERRE_COMMENT = r'</comment>'
t_APERTURA_ABSTRACT = r'<abstract>'
t_CIERRE_ABSTRACT = r'</abstract>'
t_APERTURA_SECTION = r'<section>'
t_CIERRE_SECTION = r'</section>'
t_APERTURA_SIMPLESECT = r'<simplesect>'
t_CIERRE_SIMPLESECT = r'</simplesect>'
t_APERTURA_EMPHASIS = r'<emphasis>'
t_CIERRE_EMPHASIS = r'</emphasis>'
t_APERTURA_LINK = r'<link>'
t_CIERRE_LINK = r'</link>'
t_APERTURA_FIRSTNAME = r'<firstname>'
t_CIERRE_FIRSTNAME = r'</firstname>'
t_APERTURA_SURNAME = r'<surname>'
t_CIERRE_SURNAME = r'</surname>'
t_APERTURA_STREET = r'<street>'
t_CIERRE_STREET = r'</street>'
t_APERTURA_CITY = r'<city>'
t_CIERRE_CITY = r'</city>'
t_APERTURA_STATE = r'<state>'
t_CIERRE_STATE = r'</state>'
t_APERTURA_PHONE = r'<phone>'
t_CIERRE_PHONE = r'</phone>'
t_APERTURA_EMAIL = r'<email>'
t_CIERRE_EMAIL = r'</email>'
t_APERTURA_DATE = r'<date>'
t_CIERRE_DATE = r'</date>'
t_APERTURA_YEAR = r'<year>'
t_CIERRE_YEAR = r'</year>'
t_APERTURA_HOLDER = r'<holder>'
t_CIERRE_HOLDER = r'</holder>'
arch= open("src/archivo.html","w",encoding="utf-8")

#funciones
def t_DT1(t):
      r'<[!]DOCTYPE\sarticle>'
      arch.write("<!DOCTYPE html>")
def t_TEXTO (t):
    r'[a-zA-Z][a-zA-Z0-9]*'  #falta ver caraxteres especiales
    arch.write(f'{t.value} ')
    return (t)
def t_error(t):
      
	#print ("caracter ilegal %s" % t.value[0])
	t.lexer.skip(1)
def t_APERTURA_PARA(t):
      r'<para>'
      arch.write("<p>")
      return(t)
def t_CIERRE_PARA(t):
      r'</para>'
      arch.write("</p>")
      return(t)
def t_APERTURA_TITLE(t):
      r'<title>'
      arch.write("<h1>")
      return(t)
def t_CIERRE_TITLE(t):
      r'</title>'
      arch.write("</h1>")
      return(t)
def t_APERTURA_INFO(t):
      r'<info>'
      arch.write('<p style="color:white;background-color:green">')   #todavia no consigo que ande
      return(t)
def t_CIERRE_INFO(t):
      r'</info>'
      arch.write('</p>')
      return(t)



lexer = lex.lex()
contador = 0