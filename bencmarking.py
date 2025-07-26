import models.Question as qs
import models.Respondent as rp
import dataestructure.red_black_tree as rbt
import models.Topic as tp
import models.Survey as sv
import random
import time
import matplotlib.pyplot as plt

"""
qs_1 = qs.Question(1)
qs_2 = qs.Question(2)
qs_3 = qs.Question(3)
qs_4 = qs.Question(4)
qs_5 = qs.Question(5)
qs_6 = qs.Question(6)


t_1 = tp.Topic(1)
t_2 = tp.Topic(2)

survey_1 = sv.Survey(1)


questions = [qs_1, qs_2, qs_3, qs_4, qs_5, qs_6]

# Número total de respondents
n = 100000

# Crear y distribuir respondents
for i in range(n):
    r = rp.Respondent(f'nombre_{i}', random.randint(0, 10), random.randint(0, 10), i)
    idx = i % 6  # Distribuye cíclicamente entre 6 preguntas
    #idx = 0
    questions[idx].insert_respondent(r)

t_1.insert_question(qs_1)
t_1.insert_question(qs_2)
t_1.insert_question(qs_3)
t_2.insert_question(qs_4)
t_2.insert_question(qs_5)
t_2.insert_question(qs_6)

t_1.insert_question(qs_1)
t_1.insert_question(qs_2)
t_1.insert_question(qs_3)
t_1.insert_question(qs_4)
t_1.insert_question(qs_5)
t_1.insert_question(qs_6)

survey_1.insert_topic(t_1)
survey_1.insert_topic(t_2)

#print(f"Total respondents {qs_1.respondents.root.size}")
print(f"total respondents = {qs_6.respondents.root.size+qs_1.respondents.root.size+qs_2.respondents.root.size+qs_3.respondents.root.size+qs_4.respondents.root.size+qs_5.respondents.root.size}")

def auxFunc(node):
    return node.object.calculate_opinion_mode_consensus('mode')

def benchmark_func():
    start = time.time()
    resultado = rbt.MAX_GENERIC_QUESTION_ATTR(t_1.questions,auxFunc)
    end = time.time()
    print(f"Tiempo de ejecucion {end-start:.6f} segundos")
    return resultado

print(benchmark_func())

"""
n_values = [10, 100, 1000, 10000, 100000]


times = [0.000047,0.000094,0.000590,0.006104,0.076168]

plt.figure(figsize=(8,5))
plt.plot(n_values, times, marker='o', linestyle='-', color='blue', label='Tiempo real')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tamaño de entrada vs Tiempo de ejecución')
plt.grid(True)
plt.legend()
plt.show()


