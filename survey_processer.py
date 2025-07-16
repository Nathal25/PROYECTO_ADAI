# Main
from dataestructure.list_structure import ListStructure
from models.Respondent import Respondent
from models.Question import Question
from models.Survey import Survey
from models.Topic import Topic

# Lista Ordenada
list_respondent = ListStructure()

# Encuestados
# Ojo (ID ,Nombre, Experticia, Opinion)
r1 = Respondent(1, "Sara", 8, 1)
r2 = Respondent(2, "Diego", 6, 3)
r3 = Respondent(3, "Juan", 9, 7)
r4 = Respondent(4, "Mari", 3, 10)
r5 = Respondent(5, "Alex", 3, 5)
r6 = Respondent(6, "Anna", 4, 8)
r7 = Respondent(7, "Nathalia", 4, 10)
r8 = Respondent(8, "Santiago", 4, 2)
r9 = Respondent(9, "Nicole", 4,5)
r10 = Respondent(10, "Pedro", 4,1)
r11 = Respondent(11, "Yineth", 8, 5)
r12 = Respondent(12, "Leonardo", 6, 9)
r13 = Respondent(13, "Amariles", 9, 7)
r14 = Respondent(14, "Ortiz", 3, 10)
r15 = Respondent(15, "Reyes", 3, 4)
r16 = Respondent(16, "Carlos", 4, 6)
r17 = Respondent(17, "Oscar", 4, 3)
r18 = Respondent(18, "Narvaez", 4, 2)
r19 = Respondent(19, "Sam", 4,5)
r20 = Respondent(20, "Juanita", 4,1)

# Preguntas

q1 = Question("Pregunta 1")  # Experticia / Opinion
q1.add_respondent(r1) # 8 / 1
q1.add_respondent(r2) # 6 / 3 
q1.add_respondent(r3) # 9 / 7 
q1.add_respondent(r4) # 3 / 10
q1.add_respondent(r5) # 3 / 5
q1.add_respondent(r17) # 4 / 3
q1.add_respondent(r20) # 4 / 1 
# Promedio = 4.285
# Mediana = 3
# Moda = 1 y 3

q2 = Question("Pregunta 2") # Experticia / Opinion
q2.add_respondent(r6) # 4 / 8
q2.add_respondent(r7) # 4 / 10
q2.add_respondent(r8) #  4 / 2
q2.add_respondent(r9) # 4 / 5
q2.add_respondent(r10) # 4 / 1
q1.add_respondent(r18) # 4 / 2
# Promedio =  4.666
# Mediana = 3.5
# Moda = 2


q3 = Question("Pregunta 3") # Experticia / Opinion
q3.add_respondent(r11) # 8 / 5
q3.add_respondent(r12) # 6 / 9
q3.add_respondent(r14) # 3 / 10
q3.add_respondent(r15) # 3 / 4
q3.add_respondent(r16) # 4 / 6
q1.add_respondent(r19) # 4 /  5
# Promedio = 6.5
# Mediana = 5.5
# Moda = 5 


print("")
print("------- Lista de encuestados por pregunta  -------")
print("")
q1.ordenar_respondents()
q1.imprimir_respondents()
print("")
q2.ordenar_respondents()
q2.imprimir_respondents()
print("")
q3.ordenar_respondents()
q3.imprimir_respondents()
print("")


# Tema

t1 = Topic("T1")
t1.add_question(q1)
t1.add_question(q2)
t1.add_question(q3)

surveys = Survey([t1])


surveys.pregunta_con_mayor_promedio()
surveys.pregunta_con_menor_promedio()
print("")
surveys.mayor_mediana()
surveys.menor_mediana()
print("")
#surveys.pregunta_mayor_moda()
#surveys.pregunta_menor_moda()
