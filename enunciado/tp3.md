---
title: |
  Algoritmos y Programación I (75.40) \
  Trabajo práctico n.º 3
date: Primer cuatrimeste 2015
lang: spanish
fontsize: 12pt
linkcolor: black
links-as-notes: true
header-includes:
  - \usepackage[marginal,bottom,splitrule,stable]{footmisc}
  - \urlstyle{tt}
...

1. Introducción
============

En la Universidad de Alfarería de la ciudad de Buenos Aires el querido docente
 Toban Lajp ha desaparecido sin dejar rastros.
 
 Aunque algunos afirman que ha ido de vacaciones a una pomposa isla del Caribe 
 habiendo apagado su celular, la idea que recorre los pasillos es 
 más sombría: los rumores cuentan que alguno de sus allegados se ha encargado de él 
 para siempre; con el objetivo de conseguir algún beneficio.
 
Un plantel de selectos decidió que los sospechosos a investigar son:

   - Coronel D. Bárbara: al haber desaparecido Toban Lajp, es quien queda a cargo
   de su materia. Este ascenso inmediato lo convierte ciertamente en el más beneficiado.
   - Christian Grace: el extravagante joven millonario que tiene locos a alumnos y a
   alumnas, y que se sospecha que hace tiempo está planeando maniobras para obtener 
   protagonismo.
   - Haskell Martinez: siendo que se encuentra queriendo ejercer una carrera
   docente, esta desaparición puede catapultarlo hasta la cima.
   - Ing. Alan Información: la nueva personalidad extranjera que fue recibido con
   fiesta y panqueques, traida para jerarquizar la currícula. Sin embargo parecería 
   querer escalar rápidamente hasta hacerse cargo del curso. ¿Vale?
   - Jesús: el gurú del grupo, y quien lo provee de vino y asados. Nadie
   desconfiaría de él, pero nunca se sabe...
   - Lic. Pólez: el único sospechoso no allegado a la víctima. Se sospecha que la 
   desaparición del Ing. Lajp y la consecuente debilitación de la materia puede 
   tener intereses políticos para perpetuarlo en su rol de no hacer nada.
   
Se decidió que la situación es una excelente oportunidad para ser modelada como
una versión del famoso juego Clue [^1].

Previendo que nadie va a tener dinero como para comprar la versión de mesa, 
se le solicitó a un grupo muy prestigioso de programadores que realicen el diseño y 
la implementación de una versión digital. 

Lamentablemente la implementación se dejó a medio terminar. El grupo de desarrollo
resultó ser muy conflictivo y se desató una discusión que atentaba con una 
segunda desaparición. Por lo tanto, la tarea de concluirlo le fue encomendada a 
programadores novatos de gran potencial.

Como estos no estuvieron disponibles, no quedó alternativa más que pedirle a 
los alumnos del curso de Algoritmos y Programación 1. Por suerte, el código que se pudo 
recuperar está completamente documentado, inclusive las partes faltantes, por lo que 
finalizarlo no debería ser una tarea tan laboriosa.

 [^1]: http://en.wikipedia.org/wiki/Cluedo#Games


2. Consigna
========

El Clue o Cluedo es un juego de mesa cuyas reglas se encuentran disponibles en Internet [^2]. 
Se pide desarrollar una simplificación del juego, con las siguientes variaciones:

- El tablero es más sencillo que en la versión original. Aquí 
tiene forma circular y el jugador a moverse podrá seleccionar el sentido del movimiento.

- Los jugadores no representan a ningún personaje del juego. El único movimiento
que tienen las piezas del tablero serán en los sentidos horario y antihorario 
definido luego de lanzar los dados.

- Dado que el Ing. Lajp tenía la tendencia a jugar con dados cargados, en esta
versión se permite especificar las cantidades de dados, la cantidad de caras de cada
uno y la probabilidad de ocurrencia de cada cara.

Se entrega ya desarrollada e implementada parte de la funcionalidad
básica del programa. Esto incluye una interfaz gráfica, las funciones principales 
del ciclo principal y una especificación de la interfaz de comunicación
entre los objetos del juego.

Para ejecutar la interfaz gráfica, se deberá tener instalado el paquete
PyGame:

- En sistemas operativos Linux, ejecutar: `sudo apt-get install python-pygame`
- En sistemas operativos Windows, descargar el instalador desde el sitio web
de PyGame [^3].


El alumno deberá completar las clases faltantes 
(`Tablero`, `Jugador`, `Dados` (los cuatro tipos) y `ListadoCartas`), respetando 
las especificaciones que se encuentran en el código fuente.


Adicionalmente se deberán programar pruebas para las clases
`Tablero`, `Dados` y `ListadoCartas` siguiendo el ejemplo provisto y usando
la herramienta de pruebas automatizadas de Python: unittest [^4].

Para correr las pruebas simplemente se debe ejecutar el archivo de pruebas:

    python pruebas_tp3.py


[^2]: http://www.hasbro.com/common/instruct/Clue_in_Spanish_%282002%29.pdf
[^3]: http://www.pygame.org/download.shtml
[^4]: https://docs.python.org/2/library/unittest.html


3. Criterios de aprobación
=======================

A continuación se describen los criterios y lineamientos que deben respetarse
en el desarrollo del trabajo.

3.1. Grupos
-------

El trabajo práctico debe realizarse en grupo de dos personas.


3.2. Informe
-------

El informe deberá consistir de las siguientes partes, según fueron explicadas en clase:

- Diseño: diseño del programa y de las clases, atributos y métodos a desarrollar.

- Implementación: Incluir aquí todo el código fuente utilizado, imprimiéndolo en tipo 
de letra `monoespaciado`, para facilitar su lectura.

- Pruebas: Incluir todas las funciones desarrolladas que permitan verificar el 
correcto funcionamiento de las operaciones definidas para cada clase. No incluir 
capturas de pantalla.

- Mantenimiento (opcional): posibles cambios a realizar en el trabajo, para mejorarlo.

- También opcionalmente, toda explicación adicional que consideren necesaria, 
referencias utilizadas, dificultades encontradas y conclusiones.

El informe debe estar lo más completo posible, con presentación y formato
adecuados. Por ejemplo, este enunciado cumple con los requerimientos de un
informe bien presentado.

3.3. Código
------

Además de satisfacer las especificaciones de la consigna, el código entregado
debe cumplir los siguientes requerimientos:

  - El código debe ser claro y legible.

  - Todas las clases y funciones deben estar adecuadamente documentadas, y 
  donde sea necesario el código debe estar acompañado de comentarios.
  
  - Además, claro, debe satisfacer la especificación de la interfaz y ninguna
  prueba puede fallar.


4. Entrega
=======

La entrega del trabajo consiste en:


  - El informe y código fuente impresos. Para el código fuente utilizar una
    tipografía `monoespacio`.

  - El informe digital, en formato _PDF_.

  - Una versión digital de todos archivos `.py` de código, separados del
    informe. Al ser más de un archivo, se pide que estén comprimidos en un fichero
    `.zip`.

El informe impreso debe entregarse en clase. Los dos últimos (PDF y código
fuente) deben enviarse a la dirección electrónica `tps.7540rw@gmail.com` con el
asunto _“TP3 - \<PADRÓN 1\> - \<PADRÓN 2\>”_.

El plazo de entrega vence el **viernes 29 de mayo de 2015**.