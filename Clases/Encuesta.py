
class Encuesta:
    def __init__(self, temas):
        self.temas = temas
    
    # Pregunta con mayor promedio
    def pregunta_con_mayor_promedio(self):
        mayor = self.temas[0].preguntas[0]
        for tema in self.temas:
            for pregunta in tema.preguntas:
                if pregunta.promedio_opinion() > mayor.promedio_opinion():
                    mayor = pregunta
                    
        print(f"Pregunta con mayor promedio de opiniones: {mayor.num_pregunta} - Promedio: {mayor.promedio_opinion()}")
        return mayor
    
     # Pregunta con menor promedio
    def pregunta_con_menor_promedio(self):
        menor = self.temas[0].preguntas[0]
        for tema in self.temas:
            for pregunta in tema.preguntas:
                if pregunta.promedio_opinion() < menor.promedio_opinion():
                    menor = pregunta
                    
        print(f"Pregunta con menor promedio de opiniones: {menor.num_pregunta} - Promedio:  {menor.promedio_opinion()}")
        return menor
    
    # Pregunta con mayor mediana de opiniones
    def mayor_mediana(self):
        mayor = self.temas[0].preguntas[0]
        for tema in self.temas:
            for pregunta in tema.preguntas:
                mediana_actual = pregunta.mediana_opinion()
                mediana_mayor = mayor.mediana_opinion()

                if mediana_actual > mediana_mayor:
                    mayor = pregunta
                elif mediana_actual == mediana_mayor:
                    # Desempate: elegir la de menor ID
                    if pregunta.num_pregunta < mayor.num_pregunta:
                        mayor = pregunta

        print(f"Pregunta con mayor mediana de opiniones: {mayor.num_pregunta} - Mediana:  {mayor.mediana_opinion()}")
        return mayor

    # Pregunta con menor mediana
    def menor_mediana(self):
        menor = self.temas[0].preguntas[0]
        for tema in self.temas:
            for pregunta in tema.preguntas:
                mediana_actual = pregunta.mediana_opinion()
                mediana_menor = menor.mediana_opinion()

                if mediana_actual < mediana_menor:
                    menor = pregunta
                elif mediana_actual == mediana_menor:
                    # Desempate: elegir la de menor ID
                    if pregunta.num_pregunta < menor.num_pregunta:
                        menor = pregunta

        print(f"Pregunta con menor mediana de opiniones: {menor.num_pregunta} - Mediana: {menor.mediana_opinion()}")
        return menor

    # Pregunta con mayor moda
    def pregunta_mayor_moda(self):
        mejor = None
        mayor_moda = -1

        for tema in self.temas:
            for pregunta in tema.preguntas:
                moda = pregunta.moda_opiniones()
                if moda > mayor_moda:
                    mayor_moda = moda
                    mejor = pregunta
                elif moda == mayor_moda:
                    # Empate: elegir la de menor ID
                    if pregunta.num_pregunta < mejor.num_pregunta:
                        mejor = pregunta

        if mejor:
            print(f"Pregunta con mayor valor de moda: {mejor.num_pregunta} - Moda: {mayor_moda} ")
        return mejor


    # Pregunta con menor moda
    def pregunta_menor_moda(self):
        peor = None
        menor_moda = None  

        for tema in self.temas:
            for pregunta in tema.preguntas:
                moda = pregunta.moda_opiniones()
                if menor_moda is None or moda < menor_moda:
                    menor_moda = moda
                    peor = pregunta
                elif moda == menor_moda:
                    # Empate: elegir la de menor ID
                    if pregunta.num_pregunta < peor.num_pregunta:
                        peor = pregunta

        if peor:
            print(f"Pregunta con menor valor de moda: {peor.num_pregunta} - Moda: {menor_moda}")
        return peor 


    # Pregunta con mayor valor de extremismo 
    def pregunta_mayor_extremismo(self):
        mayor = None
        mayor_extremismo = -1

        for tema in self.temas:
            for pregunta in tema.preguntas:
                valor = pregunta.extremismo_opinion()
                if valor > mayor_extremismo:
                    mayor_extremismo = valor
                    mayor = pregunta
                elif valor == mayor_extremismo:
                    # En caso de empate, elegir la de menor
                    if pregunta.num_pregunta < mayor.num_pregunta:
                        mayor = pregunta

        if mayor:
            porcentaje = round(mayor_extremismo)
            print(f"Pregunta con mayor extremismo: {mayor.num_pregunta} - {porcentaje}%")
        return mayor
    
    # Pregunta con mayor consenso 
    def pregunta_mayor_consenso(self):
        mayor = None
        mayor_consenso = -1
        
        for tema in self.temas:
            for pregunta in tema.preguntas:
                valor = pregunta.consenso_opiniones()
                if valor > mayor_consenso:
                    mayor_consenso = valor
                    mayor = pregunta
                elif valor == mayor_consenso:
                    # En caso de empate, elegir la de menor
                    if pregunta.num_pregunta < mayor.num_pregunta:
                        mayor = pregunta

        if mayor:
            porcentaje = round(mayor_consenso)
            print(f"Pregunta con mayor consenso: {mayor.num_pregunta} - {porcentaje}%")
        return mayor
        
    