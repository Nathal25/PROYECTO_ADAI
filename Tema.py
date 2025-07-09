from merge_sort import merge_sort

class Tema:
    def __init__(self, nombre):
        self.nombre = nombre  # nombre del tema
        self.preguntas = []   # lista de preguntas

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def promedio_tema(self):
        suma = 0
        for p in self.preguntas:
            suma += p.promedio_opinion()
        return suma / len(self.preguntas) if self.preguntas else 0

    def promedio_experticia_tema(self):
        suma = 0
        for p in self.preguntas:
            suma += p.promedio_experticia()
        return suma / len(self.preguntas) if self.preguntas else 0

    def total_encuestados_tema(self):
        return sum(p.total_encuestados() for p in self.preguntas)

    def ordenar_preguntas(self):
        def comparar(p1, p2):
            if p1.promedio_opinion() > p2.promedio_opinion():
                return True
            elif p1.promedio_opinion() < p2.promedio_opinion():
                return False
            else:
        # Empate en promedio de opiniones
                if p1.promedio_experticia() > p2.promedio_experticia():
                    return True
                elif p1.promedio_experticia() < p2.promedio_experticia():
                    return False
                else:
            # Empate en experticia también
                    if p1.total_encuestados() > p2.total_encuestados():
                        return True
                    else:
                        return False
        self.preguntas = merge_sort(self.preguntas, comparar)
