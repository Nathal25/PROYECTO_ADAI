
# Clase pregunta

# Ojo cada pregunta guarda su propio grupo de encuestados
from dataestructure.list_structure import ListStructure

class Question:
    def __init__(self,id):
        self.id = id
        self.respondents = []
        
    # Agregar un encuestado a una pregunta especifca
    def add_respondent(self, respondent):
        self.respondents.append(respondent)


    # Ordenar a través de opinion y en caso de empate mayor nivel de experticia
    def ordenar_respondents(self):
        lista = ListStructure(self.respondents)
    
        def compare(a, b):
            if a.opinion > b.opinion:
                return True
            elif a.opinion == b.opinion:
                return a.expertise > b.expertise
            return False

        self.respondents = lista.mergeSort(lista.list, compare)
        
        
    def imprimir_respondents(self):
        print(f"Encuestados de {self.id}:")
        for r in self.respondents:
            print(f"ID: {r.id}, Nombre: {r.name}, Opinion: {r.opinion}, Experticia: {r.expertise}")
    
    # Calcula el promedio de opiniones
    def average_opinion(self):
        total = 0
        contador = 0
        for respondent in self.respondents:
            total +=respondent.opinion
            contador += 1
        if contador == 0:
            return 0
        return total / contador
    
    # Calcula el promedio de experticia
    def average_expertise(self):
        total = 0
        contador = 0
        for respondent in self.respondents:
            total +=respondent.expertise
            contador += 1
        if contador == 0:
            return 0
        return total / contador
    
    # Calcula la mediana de opiniones
    def median_opiniones(self):
        opiniones = [r.opinion for r in self.respondents]
        lista = ListStructure(opiniones)
        lista.mergeSort(lista.list)
        
        medianaOrdenada = lista.get()[::-1] # lo ordena ascendentemente xd
      
        n = len(medianaOrdenada)
        if n % 2 == 0:
            return (medianaOrdenada[n//2-1] + medianaOrdenada[n//2] )/2
        else:
            return medianaOrdenada[n//2]
        
    # Calcula la moda de opiniones
    # Puede llegar a tres casos xd:
    # Un valor tiene la frecuencia mas alta
    # Si dos valores tienen la misma frecuencia, por ahora estan almacenados como lista :( 
    # los valores aparecen la misma cantidad de veces -> 0 (duda?)
    
    def moda_opiniones(self):
    # Revisar
    # Lista de opiniones
        listaOpiniones = [q.opinion for q in self.respondents]
        
        # Calcula la frecuencia maxima
        frecuencia_maxima = 0
        for numero in listaOpiniones:
            cantidad = listaOpiniones.count(numero)
            if cantidad > frecuencia_maxima:
                frecuencia_maxima = cantidad
                
        # Si todas aparecen una sola vez 
        if frecuencia_maxima == 1:
            return 0
    
        modas = []
        for numero in listaOpiniones:
            if listaOpiniones.count(numero) == frecuencia_maxima and numero not in modas:
                modas.append(numero)
        
        if len(modas) == 1:
            return modas[0]
        
        return modas
            
    # Calcula el extremismo de opiniones 
    def extremism_opinion(self):
        extrem = 0
        total = len(self.respondents)
        
        if total == 0:
            return 0
        
        for q in self.respondents:
            if q.opinion == 0 or q.opinion == 10:
                extrem += 1
                
        porcentaje = (extrem / total) * 100
                
        return porcentaje
    
    # Calculo de consenso de opiniones    (Similar a moda pero con porcentaje)
    def consenso_opiniones(self):
  
        listaOpiniones = [q.opinion for q in self.respondents]
        
        # Calcular la frecuencia máxima
        frecuencia_maxima = 0
        for numero in listaOpiniones:
            cantidad = listaOpiniones.count(numero)
            if cantidad > frecuencia_maxima:
                frecuencia_maxima = cantidad

        total = len(listaOpiniones)
       
        if frecuencia_maxima == 1:
            return 0
    
        porcentaje = (frecuencia_maxima / total) * 100
        return porcentaje
