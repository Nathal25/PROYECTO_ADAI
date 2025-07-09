from merge_sort import merge_sort

class Pregunta:
    def __init__(self, numero_pregunta):
        self.num_pregunta = numero_pregunta
        self.encuestados = []

    def agregar_encuestado(self, encuestado):
        self.encuestados.append(encuestado)

    def promedio_opinion(self):
        total = 0
        for e in self.encuestados:
            total += e.opinion
        return total / len(self.encuestados) if self.encuestados else 0

    def promedio_experticia(self):
        total = 0
        for e in self.encuestados:
            total += e.experticia
        return total / len(self.encuestados) if self.encuestados else 0

    def total_encuestados(self):
        return len(self.encuestados)

    def ordenar_encuestados(self):
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


        self.encuestados = merge_sort(self.encuestados, comparar)

  
