class Respondent:
    def __init__(self,name,experience,opinion,id):
        self.id=id
        self.name=name
        self.experience=experience
        self.opinion=opinion

    def print_respondent(self):
        print(f'id:{self.id}\nname:{self.name}\nexperience:{self.experience}\nopinion:{self.opinion}')

