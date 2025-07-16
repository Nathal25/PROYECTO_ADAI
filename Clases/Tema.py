from AlgoritmoOrd.merge_sort import merge_sort

class Tema:
    def __init__(self, nombre):
        self.nombre = nombre  # nombre del tema
        self.preguntas = []   # lista de preguntas
  
    # Agregar pregunta
    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
    
    # Promedio tema
    def promedio_tema(self):
        suma = 0
        for p in self.preguntas:
            suma += p.promedio_opinion()
        return suma / len(self.preguntas) if self.preguntas else 0
    
    # Promedio de experticia tema
    def promedio_experticia_tema(self):
        suma = 0
        for p in self.preguntas:
            suma += p.promedio_experticia()
        return suma / len(self.preguntas) if self.preguntas else 0

    # Total de encuestados
    def total_encuestados_tema(self):
        return sum(p.total_encuestados() for p in self.preguntas)

    # Ordenar preguntas
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

    # Mostrar resultados
    def mostrar_detalle(self):
        self.ordenar_preguntas() 
        print(f"[{round(self.promedio_tema(), 2)}] {self.nombre}:")
        for p in self.preguntas:
            enc_ids = ', '.join(str(e.id) for e in p.encuestados)
            print(f"[{round(p.promedio_opinion(), 2)}] {p.num_pregunta}: ({enc_ids})")
