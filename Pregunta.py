from merge_sort import merge_sort
# Pregunta

class Pregunta:
    def __init__(self, numero_pregunta):
        self.num_pregunta = numero_pregunta
        self.encuestados = []
        

def agregar_encuestado(self, encuestado):
        self.encestados.append(encuestado)
        
# Preguntas - promedio del valor de opinion

def promedio_opinion(self):
    total = 0
    contador = 0
    for encuestados in self.encuestados:
        total +=encuestados.opinion
        contador += 1
    if contador == 0:
        return 0
    return total / contador 


# Preguntas - Experticia

def promedio_experticia(self):
    total = 0
    contador = 0
    for encuestados in self.encuestados:
        total +=encuestados.experticia
        contador += 1
    if contador == 0:
        return 0
    return total / contador 

# Preguntas - Mediana de opiniones
def mediana_opinion(self):
    return self.encuestados // 2
# Preguntas - Moda de opiniones 

# Ordena los encuestados por opinion
def ordenar_encuestados(self):
    def comparar(a, b):
        if a.opinion > b.opinion:
             return True
        elif a.opinion < b.opinion:
            return False
        else:
            if a.experticia > b.experticia:
                return True
            else:
                return False
    self.encuestados = merge_sort(self.encuestados, comparar)











