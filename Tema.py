from merge_sort import merge_sort
 class Tema:
    def __init__(self, nombre):
        self.nombre = nombre  # nombre del tema
        self.preguntas = []  # lista de preguntas

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
    #Temas - promedio de opiniones
    def promedio_tema(self):
        suma = 0
        for p in self.preguntas:
            suma += p.promedio_opinion()
        
        if self.preguntas:
            return suma / len(self.preguntas) 
        else: 
           return 0

    #Temas - promedio de experticia
    def promedio_experticia_tema(self):
        suma = 0
        for p in self.preguntas:
            suma += p.promedio_experticia()
        if self.preguntas: 
            return suma / len(self.preguntas) 
        else:
            return 0
    #Temas - total de encuestados por tema   
    def total_encuestados_tema(self):
        total = 0
        for p in self.preguntas:
            total += p.total_encuestados()
        return total
    #Temas - ordenar preguntas
    def ordenar_preguntas(self):
        for p in self.preguntas:
            p.ordenar_encuestados()

        def comparar(p1, p2):
            if p1.promedio_opinion() > p2.promedio_opinion():
                return True
            if p1.promedio_opinion() == p2.promedio_opinion():
                if p1.promedio_experticia() > p2.promedio_experticia():
                    return True
                if p1.promedio_experticia() == p2.promedio_experticia():
                    return p1.total_encuestados() > p2.total_encuestados()
            return False

        self.preguntas = merge_sort(self.preguntas, comparar)
