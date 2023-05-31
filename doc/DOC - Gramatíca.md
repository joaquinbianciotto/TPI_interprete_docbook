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
  + [2. GRAMÁTICA](#gramatica)
    + [2.1 Símbolos de la gramática](#gramatica1)
    + [2.2 Producciones](#gramatica2)
  + [3. WEBGRAFIA](#webgrafia)

# 1. INTRODUCCION: <a name="introduccion"></a>
  En esta primera entrega del Trabajo Practico Integrador se presenta la gramática del software desarrollada. 

  El objetivo de este trabajo es construir un analizador léxico y sintáctico que permita analizar, validar y transformar un subconjunto de etiquetas de la especificación DocBook/XML para la descripción de artículos. La utilidad construida recibe un archivo en formato XML y contenido Docbook y deberá indicar si está bien construido (adecuado al estándar, sin errores) de otra manera indicar los errores; adicionalmente a medida que analiza el documento deberá transformar el contenido en un documento HTML.

  Para poder llevar a cabo el trabajo, primero que nada, debemos entender que es Docbook y que características posee.

  DocBook es un lenguaje de marcado semántico para documentación técnica. Originalmente estaba destinado a escribir documentos técnicos relacionados con el hardware y el software de la computadora, pero puede usarse para cualquier otro tipo de documentación.
  Como lenguaje semántico, DocBook permite a sus usuarios crear contenido de documentos en una forma de presentación neutral que captura la estructura lógica del contenido; ese contenido se puede publicar en una variedad de formatos, incluidos HTML, XHTML, EPUB, PDF, páginas de manual, ayuda web y ayuda HTML, sin necesidad de que los usuarios realicen ningún cambio en la fuente. En otras palabras, cuando un documento se escribe en formato DocBook, se puede transferir fácilmente a otros formatos, en lugar de tener que volver a escribirlo.

  Algunos de los principales usos de Docbook son:

   •	Libros para publicación impresa
   
   •	Mantenimiento de sitios web
   
   •	Sitios web de preguntas frecuentes
   
   •	Documentación informática
   
   •	Producción de diapositivas de presentación
   
   •	Producir documentación generada a partir de comentarios de código 

# 2. GRAMÁTICA: <a name="gramatica"></a>

# 2.1 Símbolos de la gramática: <a name="gramatica1"></a>

    Símbolo sentencia = S

    No terminales = {SEC, SSEC, INFO, ABSTRACT ADRESS, AUTHOR, COPY, TITLE, SPARA, EMPHASIS, COMMENT, LINK, EMAIL, MOBJ, FIRSTNAME, SURNAME, STREET, CITY, STATE, PHONE, DATE, YEAR, HOLDER, IOBJ, IDATA, VOBJ, VDATA, ITEMLIST, LITEM, INFTABLE, TGROUP, THEAD, TFOOD, TBODY, ROW, ENTRY, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, T, U, V, X, Y, Z }

    Terminales= {#texto, #url, <, >, /, =, ", !DOCTYPE, article, section, simplesec, info, abstract, address, author, copyright, title, simpara, emphasis, comment, link, xlink:href, para, important, firstname, surname, street, city, state, phone, email, date, year, holder, mediaobject, imageobject, imagedata, fileref, videoobject, videodata, itemizedlist, listitem, informaltable, tgroup, thead, tfood, tbody, row, entry, entrybl}
  
# 2.2 Producciones: <a name="gramatica2"></a>

  Etiquetas estructurales del documento
  
    S → <!DOCTYPE article><article> Y X Z </article>
    S → <!DOCTYPE article><article> Y X </article>
    S → <!DOCTYPE article><article>  X Z </article>
    S → <!DOCTYPE article><article>  X </article> 
    Y → INFO TITLE | INFO | TITLE
    X → ITEMLIST X | IMPORTANT X | PARA X | SPARA X | ADDRESS X | MOBJ X | INFTABLE X | COMMENT X | ABSTRACT X  
    X → ITEMLIST | IMPORTANT | PARA | SPARA | ADDRESS | MOBJ | INFTABLE | COMMENT | ABSTRACT 
    Z → SEC Z | SSEC Z 
    Z → SEC|SSEC
    SEC → <section>Y X Z</section> | <section>Y X</section> | <section>X Z</section> | <section>X </section>
    SSEC → <simplesec>Y X</simplesec> | <simplesec>X</simplesec>
    
  Etiquetas básicas de párrafo
  
    INFO → <info>A</info>
    A → MOBJ A | ABSTRACT A | ADDRESS A | AUTHOR A | DATE A | COPY A | TITLE A | 
    A → MOBJ | ABSTRACT | ADDRESS | AUTHOR | DATE | COPY | TITLE
    ABSTRACT →<abstract>TITLE B</abstract> | <abstract> B</abstract>
    B → PARA B | SPARA B 
    B → PARA | SPARA
    ADDRESS →  <address>C</address>
    C → #texto C | STREET C | CITY C | STATE C | PHONE C | EMAIL C 
    C → #texto | STREET | CITY | STATE | PHONE | EMAIL
    AUTHOR→ <author>D</author>
    D → FNAME D| SNAME D 
    D → FNAME | SNAME
    COPY → <copyright>EF</copyright>| <copyright>E</copyright>
    E → YEAR E | YEAR
    F → HOLDER F | HOLDER
    TITLE→ <title>G</title>
    G → #texto G | EMPHASIS G | LINK G | EMAIL G
    G → #texto | EMPHASIS | LINK | EMAIL | 
    SPARA → <simpara > H </simpara>
    EMPHASIS → < emphasis> H </emphasis> 
    COMMENT → <comment> H </comment>
    LINK → <link U> H </link>
    U → xlink:href=”#url”
    H → #texto H | EMPHASIS H | LINK H | EMAIL H | AUTHOR H | COMMENT H
    H → #texto | EMPHASIS | LINK | EMAIL | AUTHOR | COMMENT 
    PARA → <para>I</para>
    I → #texto I | EMPHASIS I | LINK I | EMAIL I | AUTHOR I | COMMENT I | ITEMLIST I | IMPORTANT I | ADDRESS I | MOBJ I | INFTABLE I |
    I → #texto |EMPHASIS | LINK | EMAIL | AUTHOR | COMMENT | ITEMLIST | IMPORTANT| ADDRESS | MOB | INFTABLE
    IMPORTANT → <important>TITLE J </important>| <important> J </important>
    J → ITEMLIST J | IMPORTANT J | PARA J | SPARA J | ADDRESS J | MOBJ J | INFTABLE J | COMMENT J | ABSTRACT J | 
    J → ITEMLIST  | IMPORTANT   | PARA   | SPARA  | ADDRESS  | MOBJ  | INFTABLE  | COMMENT  | ABSTRACT  |
    FIRSTNAME → <firstname> K </firstname>
    SURNAME → <surname> K </surname>
    STREET → <street> K </street>
    CITY → <city> K </city>
    STATE → <state> K </state>
    PHONE → <phone> K </phone>
    EMAIL → <email> K </email>
    DATE → <date> K </date>
    YEAR → <year> K </year>
    HOLDER → <holder> K </holder>
    K → #texto K | LINK K | EMPHASIS K | COMMENT K 
    K → #texto | LINK | EMPHASIS | COMMENT

  Imágenes y multimedia
  
    MOBJ → <mediaobject> INFO L </mediaobject> | <mediaobject> L </mediaobject>
    L → VOBJ L | IOBJ L
    L → VOBJ | IOBJ
    IOBJ → <imageobject> INFO IDATA </imageobject>
    IOBJ → <imageobject> IDATA </imageobject> 
    IDATA → <imagedata fileref=”#url”/>
    VOBJ → <videoobject> INFO VDATA </videoobject> 
    VOBJ → <videoobject> VDATA </videoobject>
    VDATA → <videodata fileref=”#url”/>

  Listas
  
    ITEMLIST → <itemizedlist> M </itemizedlist>
    M → LITEM M | LITEM
    LITEM → <listitem> J </listitem>

  Tablas
  
    INFTABLE → <informaltable> N </informaltable>
    N → MOBJ N | TGROUP N
    N → MOBJ | TGROUP 
    TGROUP → <tgroup> O </tgroup>
    O → THEAD TFOOD TBODY | TFOOD TBODY | THEAD TBODY
    THEAD → <thead> P </thead>
    TFOOD → <tfood> P </tfood>
    TBODY → <tbody> P </tbody>
    P → ROW P | ROW
    ROW → <row>  Q </row>
    Q → ENTRY Q | ENTRYTBL Q
    Q → ENTRY | ENTRYTBL 
    ENTRY → <entry>  R </entry>
    R → ITEMLIST R | IMPORTANT R | PARA R | SPARA R | #texto R | MOBJ R | COMMENT R | ABSTRACT R 
    R → ITEMLIST | IMPORTANT| PARA| SPARA | #texto| MOBJ| COMMENT | ABSTRACT 
    ENTRYTBL → <entrytbl> T </entrytbl>
    T → THEAD TBODY | TBODY

# 3. WEBGRAFIA: <a name="webgrafia"></a>
  •	https://wiki.archlinux.org/title/DocBook
  
  •	https://web.archive.org/web/20120123183312/http://www.dpawson.co.uk/docbook/reference.html
