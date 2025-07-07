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
    
# Preguntas - Moda de opiniones 
def moda_opinion(self):










