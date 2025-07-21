from controller.controlador import leer_desde_txt
from AlgoritmoOrd.merge_sort import merge_sort
from Clases.Tema import Tema
from Clases.Encuesta import Encuesta
from Clases.Encuestado import Encuestado
from controller.output import RedireccionarSalida 

# Leer datos desde archivo txt
encuestados, temas = leer_desde_txt("TestFiles/Test1.txt")

# Redirigir salida al archivo
with RedireccionarSalida("salida.txt"):
    # Ordenar temas
    temas = merge_sort(temas, lambda t1, t2: Tema.comparar_temas(t1, t2))

    for t in temas:
        t.mostrar_detalle()

    # Lista de encuestados ordenados por opinión
    todos_encuestados = list(encuestados.values())
    todos_ordenados = merge_sort(todos_encuestados, Encuestado.comparar_por_opinion)

    print("\nLista de encuestados ordenados por opinión:")
    print("{" + ", ".join(str(e.id) for e in todos_ordenados) + "}")

    print("\n--- Estadísticas ---")
    encuesta = Encuesta(temas)
    encuesta.pregunta_con_mayor_promedio()
    encuesta.pregunta_con_menor_promedio()
    encuesta.mayor_mediana()
    encuesta.menor_mediana()
    encuesta.pregunta_mayor_moda()
    encuesta.pregunta_menor_moda()
    encuesta.pregunta_mayor_extremismo()
    encuesta.pregunta_mayor_consenso()