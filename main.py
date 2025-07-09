from encuestado import Encuestado
from pregunta import Pregunta
from tema import Tema
from merge_sort import merge_sort

# Crear encuestados
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
    12: Encuestado(12, "Lucas Vásquez", 6, 8)
}

# Crear temas y preguntas
tema1 = Tema("Tema 1")
tema2 = Tema("Tema 2")

# Preguntas Tema 1
p1_1 = Pregunta("Pregunta 1.1")
p1_1.agregar_encuestado(encuestados[10])
p1_1.agregar_encuestado(encuestados[2])

p1_2 = Pregunta("Pregunta 1.2")
for eid in [1, 9, 12, 6]:
    p1_2.agregar_encuestado(encuestados[eid])

tema1.agregar_pregunta(p1_1)
tema1.agregar_pregunta(p1_2)

# Preguntas Tema 2
p2_1 = Pregunta("Pregunta 2.1")
for eid in [11, 8, 7]:
    p2_1.agregar_encuestado(encuestados[eid])

p2_2 = Pregunta("Pregunta 2.2")
for eid in [3, 4, 5]:
    p2_2.agregar_encuestado(encuestados[eid])

tema2.agregar_pregunta(p2_1)
tema2.agregar_pregunta(p2_2)

# Lista de temas
temas = [tema1, tema2]

# Ordenar preguntas de cada tema
for t in temas:
    t.ordenar_preguntas()

# Ordenar temas con merge_sort
def comparar_temas(t1, t2):
    if t1.promedio_tema() > t2.promedio_tema():
        return True
    elif t1.promedio_tema() < t2.promedio_tema():
        return False
    else:
        if t1.promedio_experticia_tema() > t2.promedio_experticia_tema():
            return True
        elif t1.promedio_experticia_tema() < t2.promedio_experticia_tema():
            return False
        else:
            return t1.total_encuestados_tema() > t2.total_encuestados_tema()

temas = merge_sort(temas, comparar_temas)

# Mostrar resultados
for t in temas:
    print(f"[{round(t.promedio_tema(), 2)}] {t.nombre}:")
    for p in t.preguntas:
        enc_ids = ', '.join(str(e.id) for e in p.encuestados)
        print(f"[{round(p.promedio_opinion(), 2)}] {p.num_pregunta}: ({enc_ids})")

# Lista de encuestados ordenados por experticia y luego por id
todos_encuestados = list(encuestados.values())

def comparar_encuestados(e1, e2):
    if e1.experticia > e2.experticia:
        return True
    elif e1.experticia < e2.experticia:
        return False
    else:
        return e1.id > e2.id  # el de mayor ID va primero si empate en experticia

todos_ordenados = merge_sort(todos_encuestados, comparar_encuestados)

print("Lista de encuestados:")
print("{" + ", ".join(str(e.id) for e in todos_ordenados) + "}")
