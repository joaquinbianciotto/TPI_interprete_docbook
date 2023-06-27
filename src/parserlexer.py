import ply.lex as lex
import ply.yacc as yacc
import re
import codecs
import os
import sys
error_caracter_ilegal=[]

tokens = [ 'DT1','APERTURA_ARTICLE', 'CIERRE_ARTICLE' , 'APERTURA_PARA', 'CIERRE_PARA', 'TEXTO', 
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
      return(t)
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

def p_sigma(p):
    ''' sigma : DT1 APERTURA_ARTICLE y x z CIERRE_ARTICLE
        | DT1 APERTURA_ARTICLE y x CIERRE_ARTICLE 
        | DT1 APERTURA_ARTICLE x z CIERRE_ARTICLE
        | DT1 APERTURA_ARTICLE x CIERRE_ARTICLE''' 
def p_y(p):
    ''' y : info title
        | info 
        | title'''
def p_x(p):
    ''' x : itemlist x 
        | important x 
        | para x 
        | spara x 
        | address x 
        | mobj x 
        | inftable x 
        | comment x 
        | abstract x
        | itemlist 
        | important 
        | para 
        | spara 
        | address 
        | mobj 
        | inftable 
        | comment 
        | abstract'''
def p_z(p):
    ''' z : sec z 
        | ssec z 
        | sec 
        | ssec'''
def p_sec(p):
    ''' sec : APERTURA_SECTION y x z CIERRE_SECTION
        | APERTURA_SECTION y x CIERRE_SECTION
        | APERTURA_SECTION x z CIERRE_SECTION
        | APERTURA_SECTION x CIERRE_SECTION''' 
def p_ssec(p):
    ''' ssec : APERTURA_SIMPLESECT y x CIERRE_SIMPLESECT
        | APERTURA_SIMPLESECT x CIERRE_SIMPLESECT'''  
    

#basicas de parrafo
def p_info(p):
    ''' info : APERTURA_INFO a CIERRE_INFO'''
def p_a(p):
    ''' a : mobj a 
        | abstract a 
        | address a 
        | author a 
        | date a 
        | copy a 
        | title a
        | mobj 
        | abstract 
        | address 
        | author 
        | date 
        | copy 
        | title'''                         
def p_abstract(p):
    ''' abstract : APERTURA_ABSTRACT title b CIERRE_ABSTRACT'''
def p_b(p):
    ''' b : para b 
        | spara b 
        | para 
        | spara'''
def p_address(p):
    ''' address : APERTURA_ADDRESS c CIERRE_ADDRESS'''
def p_c(p):
    ''' c : TEXTO c 
        | street c 
        | city c 
        | state c 
        | phone c 
        | email c
        | TEXTO 
        | street 
        | city 
        | state 
        | phone 
        | email'''   
def p_author(p):
    ''' author : APERTURA_AUTHOR d CIERRE_AUTHOR'''
def p_d(p):
    ''' d : fname d 
        | sname d 
        | fname 
        | sname'''
def p_copy(p):
    ''' copy : APERTURA_COPYRIGHT e f CIERRE_COPYRIGHT
        | APERTURA_COPYRIGHT e CIERRE_COPYRIGHT'''   
def p_e(p):
    ''' e : year e 
        | year'''
def p_f(p):
    ''' f : holder f 
        | holder'''
def p_title(p):
    ''' title : APERTURA_TITLE g CIERRE_TITLE'''
def p_g(p):
    ''' g : TEXTO g 
        | emphasis g 
        | link g 
        | email g 
        | TEXTO 
        | emphasis 
        | link 
        | email'''
def p_spara(p):
    ''' spara : APERTURA_SIMPARA h CIERRE_SIMPARA'''
def p_emphasis(p):
    ''' emphasis : APERTURA_EMPHASIS h CIERRE_EMPHASIS'''
def p_comment(p):
    ''' comment : APERTURA_COMMENT h CIERRE_COMMENT'''
def p_link(p):
    ''' link : APERTURA_LINK h'''   
def p_h(p):
    ''' h : TEXTO h 
        | emphasis h 
        | link h 
        | email h 
        | author h 
        | comment h
        | TEXTO 
        | emphasis 
        | link 
        | email 
        | author 
        | comment'''   
def p_para(p):
    ''' para : APERTURA_PARA i CIERRE_PARA'''
def p_i(p):
    ''' i : TEXTO i 
        | emphasis i 
        | link i 
        | email i 
        | author i 
        | comment i 
        | itemlist i 
        | important i 
        | address i 
        | mobj i 
        | inftable i
        | TEXTO 
        | emphasis 
        | link 
        | email 
        | author 
        | comment 
        | itemlist 
        | important 
        | address 
        | mobj 
        | inftable'''   
def p_important(p):
    ''' important : APERTURA_IMPORTANT title j CIERRE_IMPORTANT
        | APERTURA_IMPORTANT j CIERRE_IMPORTANT'''
def p_j(p):
    ''' j : itemlist j
        | important j 
        | para j 
        | spara j 
        | address j
        | mobj j 
        | inftable j 
        | comment j 
        | abstract j
        | itemlist 
        | important 
        | para 
        | spara 
        | address 
        | mobj 
        | inftable 
        | comment 
        | abstract'''
def p_fname(p):
    ''' fname : APERTURA_FIRSTNAME k CIERRE_FIRSTNAME'''
def p_sname(p):
    ''' sname : APERTURA_SURNAME k CIERRE_SURNAME'''
def p_street(p):
    ''' street : APERTURA_STREET k CIERRE_STREET'''
def p_city(p):
    ''' city : APERTURA_CITY k CIERRE_CITY'''
def p_state(p):
    ''' state : APERTURA_STATE k CIERRE_STATE'''
def p_phone(p):
    ''' phone : APERTURA_PHONE k CIERRE_PHONE'''
def p_email(p):
    ''' email : APERTURA_EMAIL k CIERRE_EMAIL'''
def p_date(p):
    ''' date : APERTURA_DATE k CIERRE_DATE'''
def p_year(p):
    ''' year : APERTURA_YEAR k CIERRE_YEAR'''
def p_holder(p):
    ''' holder : APERTURA_HOLDER k CIERRE_HOLDER'''
def p_k(p):
    ''' k : TEXTO k 
        | link k 
        | emphasis k 
        | comment k 
        | TEXTO 
        | link 
        | emphasis 
        | comment'''


#imagenes y multimedia
def p_mobj(p):
    ''' mobj : APERTURA_MEDIAOBJECT info l CIERRE_MEDIAOBJECT
        |APERTURA_MEDIAOBJECT l CIERRE_MEDIAOBJECT'''
def p_l(p):
    ''' l : vobj l 
        | iobj l 
        | vobj 
        | iobj'''
def p_iobj(p):
    ''' iobj : APERTURA_IMAGENOBJECT info idata CIERRE_IMAGENOBJECT 
        | APERTURA_IMAGENOBJECT idata CIERRE_IMAGENOBJECT'''
def p_idata(p):
    ''' idata : APERTURA_IMAGEDATA'''
def p_vobj(p):
    ''' vobj : APERTURA_VIDEOOBJECT info vdata CIERRE_VIDEOOBJECT 
        | APERTURA_VIDEOOBJECT vdata CIERRE_VIDEOOBJECT'''
def p_vdata(p):
    ''' vdata : APERTURA_VIDEODATA'''

#listas
def p_itemlist(p):
    ''' itemlist : APERTURA_ITEMIZEDLIST m CIERRE_ITEMIZEDLIST'''
def p_m(p):
    ''' m : litem m 
        | litem'''
def p_litem(p):
    ''' litem : APERTURA_LISTITEM j CIERRE_LISTITEM'''

#tablas
def p_inftable(p):
    ''' inftable : APERTURA_INFORMALTABLE n CIERRE_INFORMALTABLE'''
def p_n(p):
    ''' n : mobj n 
        | tgroup n 
        | mobj 
        | tgroup'''
def p_tgroup(p):
    ''' tgroup : APERTURA_TGROUP o CIERRE_TGROUP'''
def p_o(p):
    ''' o : thead tfood tbody 
        | tfood tbody 
        | thead tbody'''
def p_thead(p):
    ''' thead : APERTURA_THEAD oo CIERRE_THEAD'''
def p_tfood(p):
    ''' tfood : APERTURA_TFOOT oo CIERRE_TFOOT'''
def p_tbody(p):
    ''' tbody : APERTURA_TBODY oo CIERRE_TBODY'''
def p_oo(p):
    ''' oo : row oo 
        | row'''
def p_row(p):
    ''' row : APERTURA_ROW q CIERRE_ROW'''
def p_q(p):
    ''' q : entry q 
        | entrytbl q 
        | entry 
        | entrytbl'''
def p_entry(p):
    ''' entry : APERTURA_ENTRY r CIERRE_ENTRY'''
def p_r(p):
    ''' r : itemlist r 
        | important r 
        | para r 
        | spara r 
        | TEXTO r 
        | mobj r 
        | comment r 
        | abstract r
        | itemlist 
        | important 
        | para 
        | spara 
        | TEXTO 
        | mobj 
        | comment 
        | abstract'''
def p_entrytbl(p):
    ''' entrytbl : APERTURA_ENTRYTBL t CIERRE_ENTRYTBL'''
def p_t(p):
    ''' t : thead tbody 
        | tbody'''

#error
def p_error(p):
    global check
    check =0
    print (f"Error de sintaxis en linea {p}")

parser2 = yacc.yacc()
check = 1
cadena = input()
lexer.input(cadena)
print(str(lexer.token()))
with open ("prueba/nombreprueba.txt","r",encoding="utf-8") as maestro:
    parser2.parse(maestro.read())

if check == 1:
     print("correcto")