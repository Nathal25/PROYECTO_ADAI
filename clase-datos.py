class Encuesta:
    def __init__(self,temas,nombre):
        self.nombre=nombre
        self.temas=temas
class Tema:
    def __init__(self,preguntas,id):
        self.id=id
        self.preguntas=preguntas

class Encuestado:
    def __init__(self,nombre,experticia,opinion,id):
        self.id=id
        self.nombre=nombre
        self.experticia=experticia
        self.opinion=opinion

class Pregunta:
    def __init__(self,id,encuestados):
        self.id=id
        self.encuestados=encuestados