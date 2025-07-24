from controller.controller2 import Controller 

string_return=''

controller=Controller(2,2,'tests/inboundtests/Test3.txt')

controller.load_data_and_validate()

info=controller.expected_out()

string_return+=info+'\n\n'

string_return+='Lista de Encuestados:\n'
respondents=controller.get_respondents()
string_return+=respondents + '\n\n'
string_return+='Resultados:\n'


max_opinion_avg=controller.max_opinion_avg_question()
min_opinion_avg=controller.min_opinion_avg_question()
max_median=controller.max_median_question()
min_median=controller.min_median_question()
max_mode=controller.max_mode_question()
min_mode=controller.min_mode_question()
max_extremism=controller.max_opinion_extremism()
max_concesus=controller.max_concensus_question()

string_return+= f'    Pregunta con mayor promedio de opinion:[{max_opinion_avg["attr"]:.2f}] Pregunta: {max_opinion_avg["question"].topic_id}.{max_opinion_avg["question"].id}\n'
string_return+=f'    Pregunta con menor promedio de opinion:[{min_opinion_avg["attr"]:.2f}] Pregunta: {min_opinion_avg["question"].topic_id}.{min_opinion_avg["question"].id}\n'
string_return+=f'    Pregunta con mayor mediana de opinion:[{max_median["attr"]:.2f}] Pregunta: {max_median["question"].topic_id}.{max_median["question"].id}\n'
string_return+=f'    Pregunta con menor mediana de opinion:[{min_median["attr"]:.2f}] Pregunta: {min_median["question"].topic_id}.{min_median["question"].id}\n'
string_return+=f'    Pregunta con mayor valor de moda de opinion:[{max_mode["attr"]:.2f}] Pregunta: {max_mode["question"].topic_id}.{max_mode["question"].id}\n'
string_return+=f'    Pregunta con menor valor de moda de opinion:[{min_mode["attr"]:.2f}] Pregunta: {min_mode["question"].topic_id}.{min_mode["question"].id}\n'
string_return+=f'    Pregunta con mayor valor de extremismo:[{max_extremism["attr"]:.2f}] Pregunta: {max_extremism["question"].topic_id}.{max_extremism["question"].id}\n'
string_return+=f'    Pregunta con mayor valor de concenso:[{max_concesus["attr"]:.2f}] Pregunta: {max_concesus["question"].topic_id}.{max_concesus["question"].id}\n'

f=open("tests/outboundtests/OutTest3.txt","a",encoding='utf-8')
f.write(string_return)
f.close()