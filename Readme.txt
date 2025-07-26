Archivos Fuente:
Solucion Arboles Rojo y negros:

Controller: Esta carpeta contiene 2 archivos Controller lo usamos para hacer pruebas de nuestras funciones, y Controller2 es el que usamos en el main para imprimir las soluciones 
como pide el enunciado, Controller2 tiene las funciones que llaman a survey para obtener las respuestas y carga los datos

dataStructure: Continene la definicion de la clase de arbol Rojo y negro (rbt) con la definicion de todos sus metoso, los vistos en clases y algunos adicionales

models: Esta carpeta contiene los modelos de todos los objectos que usamos en la estructura de datos, como Survey, Topic, Question, Respondents, con sus respectivos metodos

tets: esta carpeta contiene los test propuestos por el proyecto, inboundtests contiene los datos de entrada de cada test, y outboundtests contiene los datos de salida de cada test

main: aqui es donde se ejecutas las funciones del proyecto y se escriben los datos de salida de cada test

Insctrucciones de uso:
En el main encontraran la incializacion del controller y los llamados a cada funcion, para probar cada test solo se debe cambiar 2 cosas.
Primero: En la linea 5 se cargan los datos para hacer las operaciones "controller=Controller(2,2,'tests/inboundtests/Test3.txt')"
cambie la ruta de los datos en 'tests/inboundtests/Test3.txt' a 'tests/inboundtests/Test2.txt' o 'tests/inboundtests/Test1.txt' para probar los diferentes test, 
en caso de querer probar con otros datos debera crear un txt en la carpeta tests y poner los datos ahi, luego cambiar la ruta mencionada anteriormente para cargas esos datos

Segundo:Para visualizar los datos de los diferentes test debe cambiar la linea 37 f=open("tests/outboundtests/OutTest3.txt","a",encoding='utf-8')
Esta linea abre un archivo txt y luego se escribe los resultados en ese archivo, cambie la ruta para guardar los resultados en sus txt correspondiente,
cambie f=open("tests/outboundtests/OutTest3.txt","a",encoding='utf-8') a f=open("tests/outboundtests/OutTest2.txt","a",encoding='utf-8') o
f=open("tests/outboundtests/OutTest1.txt","a",encoding='utf-8') para visualizar los otros test en sus respectivas carpetas en tests, si introdujo nuevos datos cree otro txt 
en la carpeta tests/outboundtests para guardar los nuevos resultados y cambie la ruta mencionada antes para guardarlos

Finalmente Correr el archivo main.py
