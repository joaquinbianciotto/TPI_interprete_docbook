###### <img src="https://frro.cvg.utn.edu.ar/theme/image.php/snap/theme/1652373334/img/logo"  width="20%" height="20%">

# SINTAXIS Y SEMÁNTICA DE LOS LENGUAJES - TRABAJO PRÁCTICO INTEGRADOR
### Diseño e implementación de Lexer y Parser y Traductor de Lenguaje RSS

  **Grupo:** N.º 4

  **Integrantes:**  
  
   - AGUIRRE, Camilo 
    
   - BIANCIOTTO, Joaquín
    
   - COLOMBO, Matías Julián
    
   - MARAIN, Yoel Mario

  **Carrera:** Ingeniería en Sistemas de Información
  
  **Comisión:** ISI A 
  
  **Primer Cuatrimestre**
  
  **Curso Académico:** 2023
  
  **UNIVERSIDAD TECNOLOGICA NACIONAL**
  
  **FACULTAD REGIONAL RESISTENCIA**
  
  **Fecha y Lugar de presentación:** 04/06/2023. Resistencia, Chaco


# Índice
  + [1. INTRODUCCION](#introduccion)
  + [2. LEXER](#lexer)
    + [2.1 Biblioteca PLY](#ply)
      + [2.1.1 Definición de tokens](#tokens)
      + [2.1.2 Expresiones regulares](#expresiones)
      + [2.1.3 Funciones](#funciones)
    + [2.2 Conversión a HTML](#html)

# 1. INTRODUCCION: <a name="introduccion"></a>
  Un analizador léxico (o *lexer*) es una parte esencial de un compilador o intérprete que se encarga de descomponer el código fuente en una secuencia de elementos más pequeños llamados *tokens*. Estos tokens son unidades léxicas que representan los componentes individuales del lenguaje de programación, como palabras clave, identificadores, operadores, números y símbolos.
  
El lexer toma el código fuente como entrada y realiza un escaneo caracter por caracter, identificando y clasificando los diferentes elementos léxicos. Utiliza reglas definidas previamente para reconocer patrones y formar los tokens correspondientes.

Para la realización de este trabajo, optamos por utilizar **Python** debido a las siguientes razones:

 +	**Sintaxis clara y legible:** Python se destaca por su sintaxis simple y fácil de leer, lo que facilita la comprensión y escritura de código, manteniendo también un código más limpio y organizado.
 +	**Aprendizaje eficiente:** Python tiene una curva de aprendizaje suave y cuenta con una gran comunidad, lo que facilita la obtención de recursos de aprendizaje en línea y documentación clara.
 +	**Amplia disponibilidad de bibliotecas y módulos:** Python cuenta con una gran cantidad de bibliotecas y módulos disponibles que facilitan la tarea de implementar funcionalidades avanzadas.

Llevamos a cabo el proyecto en una plataforma web de desarrollo colaborativo llamada **GitHub**, esta proporciona control automático de versiones, lo que permite realizar un seguimiento de los cambios realizados en el proyecto a lo largo del tiempo, facilita la colaboración en equipo, ofrece herramientas de seguimiento de problemas y solicitudes de extracción.

# 2. LEXER: <a name="lexer"></a>

# 2.1 Biblioteca PLY: <a name="ply"></a>
PLY (Python Lex-Yacc) es una biblioteca de análisis léxico y sintáctico. Proporciona las herramientas necesarias para construir analizadores personalizados basados en las técnicas de análisis léxico y sintáctico LEX y YACC utilizadas tradicionalmente en otros lenguajes. Sin embargo, a diferencia de LEX y YACC, que están escritos en C, PLY está escrito en Python y aprovecha las características del lenguaje y la facilidad de uso que ofrece.

Nosotros utilizaremos el módulo 'ply.lex', el cual proporciona herramientas necesarias para definir y ejecutar reglas de análisis léxico, es decir, para reconocer tokens en un flujo de texto.

Para esto, lo importaremos, de la siguiente forma:

    import ply.lex as lex

Una vez importado el módulo de análisis léxico, debemos definir los tokens, expresiones regulares y las funciones que nuestro Lexer debe tener en cuenta.

# 2.1.1 Definición de tokens: <a name="tokens"></a>

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
          'CIERRE_ENTRY' , 'APERTURA_ENTRYTBL' , 'CIERRE_ENTRYTBL' ]

# 2.1.2 Expresiones regulares: <a name="expresiones"></a>

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
    t_CIERRE_TBODY = r'<tbody>'
    t_APERTURA_ENTRYTBL = r'<entrytbl>'
    t_CIERRE_ENTRYTBL = r'</entrytbl>'

# 2.1.3 Funciones: <a name="funciones"></a>
Definimos una función t_ignore que especifica los caracteres que deben ser ignorados por el lexer, como espacios en blanco o tabulaciones.

    t_ignore = ' \t'

Definimos una función t_error que maneja los errores de caracteres no reconocidos.

    def t_error(t):
      print("caracter ilegal %s" % t.value[0])
      t.lexer.skip(1)
      
Creamos el lexer llamando a la función lex.lex(). Esto inicializa el lexer con las reglas y funciones definidas previamente.

    lexer = lex.lex()
    
# 2.2 Conversión a HTML: (En proceso) <a name="html"></a>
Otra de las funcionalidades que tiene nuestro trabajo es la de traducir el documento, generando un archivo de texto HTML ,transformando algunas etiquetas (XML) en etiquetas HTML.

Funciones de conversión

    def t_DT1(t):
          r'<[!]DOCTYPE\sarticle>'
          arch.write("<!DOCTYPE html>")
    def t_TEXTO (t):
        r'[a-zA-Z][a-zA-Z0-9]*'  #falta ver caracteres especiales
        arch.write(f'{t.value} ')
        return (t)
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
          arch.write('<div style="color:white;background-color:green;font-size:8pts"><p>')
          return(t)
    def t_CIERRE_INFO(t):
          r'</info>'
          arch.write('</p></div>')
          return(t)
    def t_APERTURA_IMPORTANT(t):
          r'<important>'
          arch.write('<div style="background-color:red;color:white">')
          return(t)
    def t_CIERRE_IMPORTANT(t):
          r'</important>'
          arch.write('</div>')
          return(t)
    def t_APERTURA_INFORMALTABLE(t):
          r'<informaltable>'
          arch.write("<table>")
          return (t)
    def t_CIERRE_INFORMALTABLE(t):
          r'</informaltable>'
          arch.write("</table>")
          return (t)
    def t_APERTURA_ROW(t): 
          r'<row>'
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
