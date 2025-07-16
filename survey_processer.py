import models.Question as qs
import models.Respondent as rp
import dataestructure.red_black_tree as rbt
import models.Topic as tp
import models.Survey as sv

qs_1=qs.Question(1)
qs_2=qs.Question(2)
qs_3=qs.Question(3)
qs_4 = qs.Question(4)
qs_5 = qs.Question(5)
qs_6 = qs.Question(6)

t_1 = tp.Topic(1)
t_2 = tp.Topic(2)

survey_1 = sv.Survey(1)

resp_1= rp.Respondent('andres',10,2,2)
resp_2= rp.Respondent('juan',9,1,0)
resp_3= rp.Respondent('diana',5,3,1)
resp_4= rp.Respondent('oscar',3,4,4)
resp_5= rp.Respondent('manuel',2,5,5)
resp_6= rp.Respondent('alex',3,6,6)
resp_7= rp.Respondent('andrea',4,0,7)
resp_8= rp.Respondent('marcos',9,2,8)
resp_9= rp.Respondent('dayana',9,1,9)
resp_10 = rp.Respondent('carlos', 6, 3, 0)
resp_11 = rp.Respondent('luisa', 8, 2, 1)
resp_12 = rp.Respondent('valentina', 4, 1, 2)
resp_13 = rp.Respondent('sebastian', 7, 5, 3)
resp_14 = rp.Respondent('camilo', 2, 4, 4)
resp_15 = rp.Respondent('juliana', 9, 0, 5)
resp_16 = rp.Respondent('esteban', 3, 2, 6)
resp_17 = rp.Respondent('laura', 10, 3, 7)
resp_18 = rp.Respondent('santiago', 1, 1, 8)


qs_1.insert_respondent(resp_1) 

qs_1.insert_respondent(resp_2)

qs_1.insert_respondent(resp_3)

qs_2.insert_respondent(resp_4)  

qs_2.insert_respondent(resp_5)

qs_2.insert_respondent(resp_6)

qs_3.insert_respondent(resp_7) 

qs_3.insert_respondent(resp_8)

qs_3.insert_respondent(resp_9)

qs_4.insert_respondent(resp_10)

qs_4.insert_respondent(resp_11)

qs_4.insert_respondent(resp_12)

qs_5.insert_respondent(resp_13)

qs_5.insert_respondent(resp_14)

qs_5.insert_respondent(resp_15)

qs_6.insert_respondent(resp_16)

qs_6.insert_respondent(resp_17)

qs_6.insert_respondent(resp_18)

t_1.insert_question(qs_1)
t_1.insert_question(qs_2)
t_1.insert_question(qs_3)

t_2.insert_question(qs_4)
t_2.insert_question(qs_5)
t_2.insert_question(qs_6)

survey_1.insert_topic(t_1)
survey_1.insert_topic(t_2)

avg_1 = rbt.TREE_AVERAGE_ATTR(t_1.questions,t_1.questions.root,
                              lambda question : rbt.TREE_AVERAGE_ATTR(question.object.respondents,question.object.respondents.root,lambda x : getattr(x.object,'opinion')))

avg_2 = rbt.TREE_AVERAGE_ATTR(t_2.questions,t_2.questions.root,
                              lambda question : rbt.TREE_AVERAGE_ATTR(question.object.respondents,question.object.respondents.root,lambda x : getattr(x.object,'opinion')))

#print(f"Promedio del topic 1 es {avg_1}")
#print(f"Promedio del topic 2 es {avg_2}")

#survey_1.print_topics()

median_qs_1 = qs_1.calculate_opinion_median()
median_qs_2 = qs_2.calculate_opinion_median()
median_qs_3 = qs_3.calculate_opinion_median()

print(f"Median opinions question 1 {median_qs_1}")
print(f"Median opinions question 2 {median_qs_2}")
print(f"Median opinions question 3 {median_qs_3}")

max_media_question = survey_1.max_median_question()
print(f"valor de la maxima mediana es: {max_media_question['max_attr']}")
print(f"La pregunta con mayor mediana es la que tiene id: {max_media_question['question_max'].id}")


mode_qs_1 = qs_1.calculate_opinion_mode_consensus('mode')
mode_qs_2 = qs_2.calculate_opinion_mode_consensus('mode')
mode_qs_3 = qs_3.calculate_opinion_mode_consensus('mode')

print(f"Mode opinions question 1 {mode_qs_1}")
print(f"Mode opinions question 2 {mode_qs_2}")
print(f"Mode opinions question 3 {mode_qs_3}")

max_mode_question = survey_1.max_mode_question()
max_mode_question_topic_1=t_1.max_mode_question()
max_mode_question_topic_2=t_2.max_mode_question()
print(f"valor de la maxima mode es: {max_mode_question['max_attr']}")
print(f"La pregunta con mayor mode es la que tiene id: {max_mode_question['question_max'].id}")
print(f"La pregunta con mayor mode desde topic es la que tiene id:{max_mode_question_topic_1['question_max'].id}")
print(f"La pregunta con mayor mode desde topic es la que tiene id:{max_mode_question_topic_2['question_max'].id}")



# max_consensus_q = survey_1.max_consensus_question()
# print(max_consensus_q)
# print(max_consensus_q['question_max'].id)
# print(getattr(qs_1.respondents.root.object,'name'))

# avg=qs_1.calculate_opinion_average()

# print(avg)

# th_1=rbt.OS_SELECT(qs_1.respondents.root,5)

# print(getattr(th_1.object,'name'))

# median=qs_1.calculate_median()

# print(median)

# median=rbt.OS_SELECT(qs_1.respondents.root,1)

# print(getattr(median.object,'name'))

#m=qs_1.calculate_opinion_median()

#print(m)





