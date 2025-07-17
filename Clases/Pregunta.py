from AlgoritmoOrd.merge_sort import merge_sort

def comparar_ascendente(x, y):
        return x < y

class Pregunta:
    def __init__(self, numero_pregunta):
        self.num_pregunta = numero_pregunta
        self.encuestados = []
        
    # Agregar encuestados
    def agregar_encuestado(self, encuestado):
        self.encuestados.append(encuestado)
 
    # Promedio de opinion
    def promedio_opinion(self):
        total = 0
        for e in self.encuestados:
            total += e.opinion
        return total / len(self.encuestados) if self.encuestados else 0

    # Promedio experticia
    def promedio_experticia(self):
        total = 0
        for e in self.encuestados:
            total += e.experticia
        return total / len(self.encuestados) if self.encuestados else 0
    

    # Mediana de opiniones
    def mediana_opinion(self):
        opiniones = [e.opinion for e in self.encuestados]
        opiniones_ordenadas = merge_sort(opiniones, comparar_ascendente)
        
        n = len(opiniones_ordenadas)
        if n == 0:
            return 0
        
        if n % 2 == 0:
            return opiniones_ordenadas[n//2 - 1] 
        else:
            return opiniones_ordenadas[n//2]
    
    # Modaq de opiniones
    def moda_opiniones(self):
        
        lista_opiniones = [e.opinion for e in self.encuestados]
        
        frecuencia_maxima = 0
        for numero in lista_opiniones:
            cantidad = lista_opiniones.count(numero)
            if cantidad > frecuencia_maxima:
                frecuencia_maxima = cantidad
                
        menor_moda = None
        for numero in lista_opiniones:
                if lista_opiniones.count(numero) == frecuencia_maxima:
                    if menor_moda is None or numero < menor_moda:
                        menor_moda = numero

        return menor_moda
    
    # Extremismo de opinion
    def extremismo_opinion(self):
        extremos = 0
        total = len(self.encuestados)

        if total == 0:
            return 0

        for e in self.encuestados:
            if e.opinion == 0 or e.opinion == 10:
                extremos += 1
                
        porcentaje = (extremos / total) * 100

        return porcentaje
    
    # Consenso de opiniones
    def consenso_opiniones(self):
        listaOpiniones = [q.opinion for q in self.encuestados]
        total = len(listaOpiniones)
        
        frecuencia_maxima = 0
        
        for numero in listaOpiniones:
            cantidad = 0
            for n in listaOpiniones:
                if n == numero:
                    cantidad += 1
            if cantidad > frecuencia_maxima:
                frecuencia_maxima = cantidad

        total = len(listaOpiniones)
       
        porcentaje = (frecuencia_maxima / total) * 100
        return porcentaje

    # Total de encuestados
    def total_encuestados(self):
        return len(self.encuestados)

    # Ordenar encuestados 
    def ordenar_encuestados(self):
        def comparar(e1, e2):
            if e1.opinion > e2.opinion:
                return True
            elif e1.opinion < e2.opinion:
                return False
            else:
                if e1.experticia > e2.experticia:
                    return True
                elif e1.experticia < e2.experticia:
                    return False
                else:
                    return False  # En caso de empate total, no se cambia el orden

        self.encuestados = merge_sort(self.encuestados, comparar)


  
