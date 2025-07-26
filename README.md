
Primera alternativa:
Para esta solución se utilizó programación orientada a objetos. Para ello, se crearon varias carpetas
y archivos organizados de la siguiente forma:

AlgoritmoOrd:
Contiene el archivo con el algoritmo de ordenamiento, que es Merge Sort.

Clases:
Contiene los siguientes archivos:

Encuesta: Funciones para calcular estadísticas de las preguntas, como la que tiene mayor o menor promedio, mediana, moda, extremismo o consenso.

Encuestado: Guarda los datos de cada encuestado y métodos para comparar encuestados por opinión o experticia.

Pregunta: Permite agregar encuestados y contiene funciones para calcular estadísticas de cada pregunta, obtener el total de encuestados y ordenar encuestados.

Tema: Permite agregar preguntas, calcular promedios y promedios de experticia, ordenar preguntas y ordenar temas.

TestFiles:
Contiene los 3 archivos de prueba.

Controller:

controlador: Lee un archivo de texto, arma las preguntas y agrupa todo en temas. Además, devuelve una lista de encuestados y temas listos para usarse.

output: Imprime la salida en un archivo de texto.

Archivo main:
Este archivo se encarga de juntar todo lo realizado en el proyecto. 
Lee la información de un archivo .txt donde están los encuestados y las preguntas, 
luego ordena los datos y calcula resultados como cuál pregunta tuvo mayor promedio,
mediana, moda, etc. Después muestra todo eso en pantalla y también lo guarda en un archivo
de texto para poder revisarlo después.

---- Instrucciones ----

Para ejecutar el programa:
1) Abre el archivo main.py
2) Localiza la variable

archivo_txt = "TestFiles/Test2.txt"   <- Cambias solo el nombre al archivo que quiera ejecutar 

3) Guarda el archivo y ejecutalo

4) Una vez que se termine de ejecutar, abres el archivo resultados_encuesta.txt, alli
encontraras los resultados del archivo ejecutado.