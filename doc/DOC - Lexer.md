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
