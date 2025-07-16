
# Clase Encuesta

# Ojo guarda todos los temas
class Survey:
    def __init__(self,topics):
        self.topics = topics
      
    # Calculos de estadisticas
    
    # Menor promedio
    def pregunta_con_mayor_promedio(self):
        
        mayor = self.topics[0].questions[0]
        for topic in self.topics:
            for q in topic.questions:
                if q.average_opinion() > mayor.average_opinion(): 
                    mayor = q
            print(f"Pregunta con mayor promedio de opiniones: {mayor.id}")
            
        return 
    
    
    def pregunta_con_menor_promedio(self):
        menor = self.topics[0].questions[0]
        
        for topic in self.topics:
            for q in topic.questions:
                if q.average_opinion() < menor.average_opinion(): 
                    menor = q
                    
            print(f"Pregunta con menor promedio de opiniones: {menor.id}")
    
        return
    
    
    # Mayor mediana 
    def mayor_mediana(self):
        mayor = self.topics[0].questions[0]
        for topic in self.topics:
            for q in topic.questions:
                if q.median_opiniones() > mayor.median_opiniones():
                    mayor = q
        
        print(f"Pregunta con mayor mediana de opiniones: {mayor.id}")
                
        return 
    
    # menor mediana 
    def menor_mediana(self):
            menor = self.topics[0].questions[0]
            for topic in self.topics:
                for q in topic.questions:
                    if q.median_opiniones() < menor.median_opiniones():
                        menor = q
            
            print(f"Pregunta con menor mediana de opiniones: {menor.id}")
                    
            return 
    
"""
    # mayor moda - Falta mayor moda iguales 
    def pregunta_mayor_moda(self):
        mejor = None
        mayor_moda = -1
        
        for topic in self.topics:
            for q in topic.questions:
                moda = q.moda_opiniones()
                
                if moda > mayor_moda:
                    mayor_moda = moda
                    mejor = q
        
        print(f"Pregunta con mayor valor de moda: {mejor.id}")
        return
            
    # menor moda - Falta menor moda iguales
    def pregunta_menor_moda(self):
        mejor = None
        menor_moda = None
        
        for topic in self.topics:
            for q in topic.questions:
                moda = q.moda_opiniones()
                
                if menor_moda is None or moda < menor_moda:
                    menor_moda = moda
                    mejor = q
        
        print(f"Pregunta con menor valor de moda: {mejor.id}")
        return
  """  
    # Mayor extremismo
    
    # Consenso