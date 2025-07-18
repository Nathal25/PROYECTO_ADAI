from Clases.Encuestado import Encuestado
from Clases.Pregunta import Pregunta
from Clases.Tema import Tema
from Clases.Encuesta import Encuesta
from AlgoritmoOrd.merge_sort import merge_sort
from controller.controlador import leer_encuestados_desde_csv
# Crear encuestados
# (ID ,Nombre, Experticia, Opinion)
from Clases.Encuestado import Encuestado
# Mostrar lista ordenada
def imprimir_encuestados(encuestados):
    for e in encuestados:
        print(f"ID: {e.id}, Nombre: {e.nombre}, Experticia: {e.experticia}, Opinión: {e.opinion}")


ruta_csv = "encuestados.csv"
encuestados = leer_encuestados_desde_csv(ruta_csv)

# Crear temas y preguntas
tema1 = Tema("Tema 1")
tema2 = Tema("Tema 2")
tema3 = Tema("Tema 3")

# Preguntas Tema 1
p1_1 = Pregunta("Pregunta 1.1")
for eid in [2,10]:
    p1_1.agregar_encuestado(encuestados[eid])
    
p1_2 = Pregunta("Pregunta 1.2")
for eid in [1, 9, 12, 6]:
    p1_2.agregar_encuestado(encuestados[eid])

p1_3 = Pregunta("Pregunta 1.3")
for eid in [20, 15, 30, 32]:
    p1_3.agregar_encuestado(encuestados[eid])

p1_4 = Pregunta("Pregunta 1.4")
for eid in [32, 1, 16, 14]:
    p1_4.agregar_encuestado(encuestados[eid])


tema1.agregar_pregunta(p1_1)
tema1.agregar_pregunta(p1_2)
tema1.agregar_pregunta(p1_3)
tema1.agregar_pregunta(p1_4)

# Preguntas Tema 2
p2_1 = Pregunta("Pregunta 2.1")
for eid in [11, 8, 7]:
    p2_1.agregar_encuestado(encuestados[eid])

p2_2 = Pregunta("Pregunta 2.2")
for eid in [3, 4, 5]:
    p2_2.agregar_encuestado(encuestados[eid])

p2_3 = Pregunta("Pregunta 2.3")
for eid in [7, 12, 17, 25]:
    p2_3.agregar_encuestado(encuestados[eid])

p2_4 = Pregunta("Pregunta 2.4")
for eid in [1, 5, 3, 21]:
    p2_4.agregar_encuestado(encuestados[eid])


tema2.agregar_pregunta(p2_1)
tema2.agregar_pregunta(p2_2)
tema2.agregar_pregunta(p2_3)
tema2.agregar_pregunta(p2_4)


# Preguntas Tema 3
p3_1 = Pregunta("Pregunta 3.1")
for eid in [2]:
    p3_1.agregar_encuestado(encuestados[eid])

p3_2 = Pregunta("Pregunta 3.2")
for eid in [3, 5]:
    p3_2.agregar_encuestado(encuestados[eid])

p3_3 = Pregunta("Pregunta 3.3")
for eid in [13, 8, 20, 28]:
    p3_3.agregar_encuestado(encuestados[eid])

p3_4 = Pregunta("Pregunta 3.4")
for eid in [21, 11, 31, 27]:
    p3_4.agregar_encuestado(encuestados[eid])


tema3.agregar_pregunta(p3_1)
tema3.agregar_pregunta(p3_2)
tema3.agregar_pregunta(p3_3)
tema3.agregar_pregunta(p3_4)

# Lista de temas
temas = [tema1, tema2, tema3]
temas = merge_sort(temas, Tema.comparar_temas)
for t in temas:
    t.mostrar_detalle()
    

# Lista de encuestados ordenados por experticia y luego por id
todos_encuestados = list(encuestados.values())
todos_ordenados = merge_sort(todos_encuestados, Encuestado.comparar_por_opinion)

print("Lista de encuestados:")
print("{" + ", ".join(str(e.id) for e in todos_ordenados) + "}")


# Calculos estadisticos:
print("")
encuesta = Encuesta([tema1, tema2, tema3])
encuesta.pregunta_con_mayor_promedio()
encuesta.pregunta_con_menor_promedio()
encuesta.mayor_mediana()
encuesta.menor_mediana()
encuesta.pregunta_mayor_moda()
encuesta.pregunta_menor_moda()
encuesta.pregunta_mayor_extremismo() 
encuesta.pregunta_mayor_consenso()
'''
print("")
print("Pruebas")
print("Mediana")
print("Pregunta 1.1: ",p2_1.mediana_opinion())
print("Pregunta 2.2: ",p2_2.mediana_opinion())
print("Pregunta 2.3: ",p2_3.mediana_opinion())
print("Prueba Moda")
print("Pregunta 1.3:",p1_3.moda_opiniones())
print("Pregunta 2.4:",p2_4.moda_opiniones())
print("Pregunta 1.4:",p1_4.moda_opiniones())
print("")
print("Extremismo de la pregunta 1.4: ",p3_1.extremismo_opinion())
print("Consenso de la pregunta 1.1: ", p1_1.consenso_opiniones())
print("Consenso de la pregunta 1.1: ", p1_1.consenso_opiniones())
print("Consenso de la pregunta 2.1: ", p2_1.consenso_opiniones())
print("Consenso de la pregunta 3.1: ", p3_1.consenso_opiniones())

'''



