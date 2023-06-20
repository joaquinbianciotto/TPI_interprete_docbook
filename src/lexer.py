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
          'CIERRE_YEAR' , 'APERTURA_HOLDER' , 'CIERRE_HOLDER', 'APERTURA_IMAGEDATA' , 'APERTURA_VIDEOOBJECT' ,
          'CIERRE_VIDEOOBJECT' , 'APERTURA_IMAGENOBJECT' , 'CIERRE_IMAGENOBJECT' , 'APERTURA_VIDEODATA', 'APERTURA_LISTITEM' ,
          'CIERRE_LISTITEM' , 'APERTURA_TGROUP' , 'CIERRE_TGROUP' , 'APERTURA_THEAD' , 'CIERRE_THEAD' , 'APERTURA_TFOOT' ,
          'CIERRE_TFOOT' , 'APERTURA_TBODY' , 'CIERRE_TBODY' , 'APERTURA_ROW' , 'CIERRE_ROW' , 'APERTURA_ENTRY' ,
          'CIERRE_ENTRY' , 'APERTURA_ENTRYTBL' , 'CIERRE_ENTRYTBL','APERTURA_AUTHOR','CIERRE_AUTHOR','ERROR_1','ERROR_2','ERROR_3','newline' ,
          'APERTURA_COPYRIGHT' , 'CIERRE_COPYRIGHT'
		]

t_ignore = '\t '   #nose que hace pero vi en varios, creo q ignora espacios en blanco o tabulacion


t_APERTURA_ARTICLE = r'<article>'
t_CIERRE_ARTICLE = r'</article>'
t_APERTURA_SIMPARA = r'<simpara>'
t_CIERRE_SIMPARA = r'</simpara>'
t_APERTURA_ADDRESS = r'<address>'
t_CIERRE_ADDRESS = r'</address>'
t_APERTURA_MEDIAOBJECT = r'<mediaobject>'
t_CIERRE_MEDIAOBJECT = r'</mediaobject>'
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
t_APERTURA_AUTHOR = r'<author>'
t_CIERRE_AUTHOR = r'</author>'
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
t_APERTURA_VIDEOOBJECT = r'<videoobject>'
t_CIERRE_VIDEOOBJECT = r'</videoobject>'
t_APERTURA_IMAGENOBJECT = r'<imagenobject>'
t_CIERRE_IMAGENOBJECT = r'</imagenobject>'
t_APERTURA_TGROUP = r'<tgroup>'
t_CIERRE_TGROUP = r'</tgroup>'
t_APERTURA_THEAD = r'<thead>'
t_CIERRE_THEAD = r'</thead>'
t_APERTURA_TFOOT = r'<tfood>'
t_CIERRE_TFOOT = r'</tfood>'
t_APERTURA_TBODY = r'<tbody>'
t_CIERRE_TBODY = r'</tbody>'
t_APERTURA_ENTRYTBL = r'<entrytbl>'
t_CIERRE_ENTRYTBL = r'</entrytbl>'
t_APERTURA_COPYRIGHT = r'<copyright>'
t_CIERRE_COPYRIGHT = r'</copyright>'
t_ERROR_1 = r'<[\w]+>'
t_ERROR_2 = r'<[\w]+\s[\w]+=*[\w"]+\s*/*>'
t_ERROR_3 = r'</[\w]+>'

arch= open("src/html_generados/archivo.html","w",encoding="utf-8")

#funciones
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_DT1(t):
      r'<[!]DOCTYPE\sarticle>'
      arch.write("<!DOCTYPE html>")
def t_TEXTO (t):
    r'[\w.,:;_%/+?¿¡!()"\'_|°¬~$&=^`{}\#@*\-,\[\]\\]+'  #falta ver caraxteres especiales
    arch.write(f'{t.value} ')
    return (t)
def t_error(t):
	print ("caracter ilegal %s" % t.value[0])
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
      arch.write('<div style="color:white;background-color:green;font-size:8pts"><p>')   #anda bien
      return(t)
def t_CIERRE_INFO(t):
      r'</info>'
      arch.write('</p></div>')
      return(t)
def t_APERTURA_IMPORTANT(t):
      r'<important>'
      arch.write('<div style="background-color:red;color:white">') #anda bien
      return(t)
def t_CIERRE_IMPORTANT(t):
      r'</important>'
      arch.write('</div>')
      return(t)
def t_APERTURA_IMAGEDATA (t):
      r'<imagedata\s+fileref="[(http(s)?|ftp(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"\s*[/]>'
      return(t)
def t_APERTURA_VIDEODATA (t):
      r'<videodata\s+fileref="[(http(s)?|ftp(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"\s*[/]>'
      return(t)
def t_APERTURA_LINK (t):
      r'<link\s+xlink:href ="[(http(s)?|ftp(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"\s*[/]>'
      arch.write(f'<a href="{t.value}">esto es un link</a>')
      return (t)
def t_APERTURA_INFORMALTABLE(t):
      r'<informaltable>'
      arch.write("<table>")
      return (t)
def t_CIERRE_INFORMALTABLE(t):
      r'</informaltable>'
      arch.write("</table>")
      return (t)
def t_APERTURA_ROW(t):                                #un problema con esto es que en html todos son tr y se diferencian adentro usando 
      r'<row>'                                        #<th></th> para los encabezados y pies de la tabla
      arch.write("<tr>")
      return (t)
def t_CIERRE_ROW(t):
      r'</row>'
      arch.write("</tr>")
      return (t)
def t_APERTURA_ENTRY(t): 
      r'<entry>'
      arch.write("<td>")
      return (t)
def t_CIERRE_ENTRY(t): 
      r'</entry>'
      arch.write("</td>")
      return (t)
def t_APERTURA_ITEMIZEDLIST(t):
      r'<itemizedlist>'
      arch.write("<ul>")
      return (t)
def t_CIERRE_ITEMIZEDLIST(t):
      r'</itemizedlist>'
      arch.write("</ul>")
      return (t)
def t_APERTURA_LISTITEM(t):
      r'<listitem>'
      arch.write("<il>")
      return (t)
def t_CIERRE_LISTITEM(t):
      r'</listitem>'
      arch.write("</il>")
      return (t)

lexer = lex.lex()
