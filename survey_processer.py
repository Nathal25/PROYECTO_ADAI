import models.Question as qs
import models.Topic as tp
import models.Respondent as rp
import dataestructure.red_black_tree as rbt


qs_1=qs.Question(0)
qs_2=qs.Question(1)
qs_3=qs.Question(2)

t_1=tp.Topic(0)

resp_1= rp.Respondent('andres',10,2,2)
resp_2= rp.Respondent('juan',9,1,0)
resp_3= rp.Respondent('diana',5,3,1)
resp_4= rp.Respondent('oscar',3,4,4)
resp_5= rp.Respondent('manuel',3,5,5)
resp_6= rp.Respondent('alex',3,6,6)
resp_7= rp.Respondent('andrea',5,0,7)
resp_8= rp.Respondent('marcos',9,2,8)
resp_9= rp.Respondent('dayana',5,1,9)


qs_1.insert_respondent(resp_1)

qs_1.insert_respondent(resp_2)

qs_1.insert_respondent(resp_3)

qs_2.insert_respondent(resp_4)

qs_2.insert_respondent(resp_5)

qs_2.insert_respondent(resp_6)

qs_3.insert_respondent(resp_7)

qs_3.insert_respondent(resp_8)

qs_3.insert_respondent(resp_9)



t_1.insert_question(qs_1)
t_1.insert_question(qs_2)
t_1.insert_question(qs_3)

median_1=qs_1.calculate_opinion_median()

median_2=qs_2.calculate_opinion_median()

median_3=qs_3.calculate_opinion_median()

# print(f'medians are this median_1: {median_1}, median_2: {median_2}, median_3: {median_3}')

# q=t_1.max_median_question()
# id_question=q['question_max'].id
# max_median=q['max_median']

# print(f'question_id:{id_question} and max_median: {max_median}')

# print(getattr(qs_1.respondents.root.object,'name'))

# avg=rbt.TREE_AVERAGE_ATTR(qs_1.respondents,qs_1.respondents.root,'opinion')

# print(avg)

# th_1=rbt.OS_SELECT(qs_1.respondents.root,2)

# print(getattr(th_1.object,'name'))

# median=qs_1.calculate_median()

# print(median)

# median=rbt.OS_SELECT(qs_1.respondents.root,1)

# print(getattr(median.object,'name'))

# m=qs_2.calculate_opinion_median()

# print(m)

t_1.print_questions()

avg_1=rbt.TREE_AVERAGE_ATTR(qs_1.respondents,qs_1.respondents.root,lambda x: getattr(x.object,'opinion'))
avg_2=rbt.TREE_AVERAGE_ATTR(qs_2.respondents,qs_2.respondents.root,lambda x: getattr(x.object,'opinion'))
avg_3=rbt.TREE_AVERAGE_ATTR(qs_3.respondents,qs_3.respondents.root,lambda x: getattr(x.object,'opinion'))

print(avg_1)
print(avg_2)
print(avg_3)