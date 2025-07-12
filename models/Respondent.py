
# Clase encuestados

class Respondent:
    def __init__(self,id,name,expertise,opinion):
        self.id = id
        self.name = name
        self.expertise = expertise
        self.opinion = opinion

    def print_respondent(self):
        print(f'id:{self.id}\nname:{self.name}\nexperience:{self.expertise}\nopinion:{self.opinion}')
