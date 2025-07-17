from Clases.Encuestado import Encuestado
from Clases.Pregunta import Pregunta
from Clases.Tema import Tema
from Clases.Encuesta import Encuesta
from AlgoritmoOrd.merge_sort import merge_sort

# Crear encuestados
 # Ojo (ID ,Nombre, Experticia, Opinion)

encuestados = {
    1: Encuestado(1, "Sofia García", 1, 6),
    2: Encuestado(2, "Alejandro Torres", 7, 10),
    3: Encuestado(3, "Valentina Rodriguez", 9, 0),
    4: Encuestado(4, "Juan López", 10, 1),
    5: Encuestado(5, "Martina Martinez", 7, 0),
    6: Encuestado(6, "Sebastián Pérez", 8, 9),
    7: Encuestado(7, "Camila Fernández", 2, 7),
    8: Encuestado(8, "Mateo González", 4, 7),
    9: Encuestado(9, "Isabella Díaz", 7, 5),
    10: Encuestado(10, "Daniel Ruiz", 2, 9),
    11: Encuestado(11, "Luciana Sánchez", 1, 7),
    12: Encuestado(12, "Lucas Vásquez", 6, 8),
    13: Encuestado(13, "Sara", 8, 1),
    14: Encuestado(14, "Diego", 6, 3),
    15: Encuestado(15, "Juan", 9, 7),
    16: Encuestado(16, "Mari", 3, 10),
    17: Encuestado(17, "Alex", 3, 5),
    18: Encuestado(18, "Anna", 4, 8),
    19: Encuestado(19, "Nathalia", 4, 10),
    20: Encuestado(20, "Santiago", 4, 2),
    21: Encuestado(21, "Nicole", 4,5),
    22: Encuestado(22, "Pedro", 4,1),
    23: Encuestado(23, "Yineth", 8, 5),
    24: Encuestado(24, "Leonardo", 6, 9),
    25: Encuestado(25, "Amariles", 9, 7),
    26: Encuestado(26, "Ortiz", 3, 10),
    27: Encuestado(27, "Reyes", 3, 4),
    28: Encuestado(28, "Carlos", 4, 6),
    29: Encuestado(29, "Oscar", 4, 3),
    30: Encuestado(30, "Narvaez", 4, 2),
    31: Encuestado(19, "Sam", 4,5),
    32: Encuestado(20, "Juanita", 4,1)
}

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



