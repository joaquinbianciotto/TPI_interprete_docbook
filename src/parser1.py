import ply.yacc as yacc
import os 
import codecs 
import re
from lexer import tokens 
correcto = 0
global i
i = 0
#vi en otros donde cada no terminal q tenia mas de una produccion, por cada produccion hacian una funcion
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
    ''' abstract : APERTURA_ABSTRACT title b CIERRE_ABSTRACT
        | APERTURA_ABSTRACT b CIERRE_ABSTRACT'''
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
        | APERTURA_MEDIAOBJECT l CIERRE_MEDIAOBJECT'''
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
    global correcto
    correcto = 1                           
    print ("Error de sintaxis",p)

parser = yacc.yacc()
