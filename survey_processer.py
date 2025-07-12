# Main
from dataestructure.list_structure import ListStructure
from models.Respondent import Respondent
from models.Question import Question

# Lista Ordenada
list_respondent = ListStructure()

# Encuestados
# Ojo (ID ,Nombre, Experticia, Opinion)
r1 = Respondent(1, "Sara", 8, 1)
r2 = Respondent(2, "Diego", 6, 8)
r3 = Respondent(3, "Juan", 9, 7)
r4 = Respondent(4, "Mari", 3, 10)
r5 = Respondent(5, "Alex", 3, 8)

q1 = Question("Q1")
q1.add_respondent(r1)
q1.add_respondent(r2)
q1.add_respondent(r3)
q1.add_respondent(r4)
q1.add_respondent(r5)

print(f"Promedio de opiniones: {q1.average_opinion():.2f}")
print(f"Promedio de experticia: {q1.average_expertise():.2f}")
print("Mediana de opinion:", q1.median_opiniones())
print("Moda de opiniones: ", q1.moda_opiniones())
print("Porcentaje extremismo de opiniones: ", q1.extremism_opinion())
print("Consenso de opiniones: ", q1.consenso_opiniones())