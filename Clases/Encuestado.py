class Encuestado:
    def __init__(self, id, nombre, experticia, opinion):
        self.id = id
        self.nombre = nombre
        self.experticia = experticia
        self.opinion = opinion

    def comparar_por_opinion(e1, e2):
        if e1.opinion > e2.opinion:
            return True
        elif e1.opinion < e2.opinion:
            return False
        elif e1.experticia > e2.experticia:
            return True
        elif e1.experticia < e2.experticia:
            return False
        else:
            return e1.id < e2.id
