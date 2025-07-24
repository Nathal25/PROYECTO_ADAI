class Respondent:
    def __init__(self,name,opinion,experience,id):
        self.id=id
        self.name=name
        self.experience=experience
        self.opinion=opinion

    def get_info(self):
        return f'   {self.id}, Nombre:{self.name}, Experticia:{self.experience}, Opinión:{self.opinion}\n'

