import models.Question as qs
import models.Respondent as rp
import dataestructure.red_black_tree as rbt


qs_1=qs.Question(0)

resp_1= rp.Respondent('andres',2,2,2)
resp_2= rp.Respondent('juan',2,1,0)
resp_3= rp.Respondent('diana',3,3,1)
resp_4= rp.Respondent('oscar',3,4,1)
resp_5= rp.Respondent('manuel',3,5,1)
resp_6= rp.Respondent('alex',2,6,1)


qs_1.insert_respondent(resp_1)

qs_1.insert_respondent(resp_2)

qs_1.insert_respondent(resp_3)

qs_1.insert_respondent(resp_4)

qs_1.insert_respondent(resp_5)
 
qs_1.insert_respondent(resp_6)


#--------------PRUEBAS DE MODA------------------------
moda = qs_1.calculate_opinion_mode()
print(moda)


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


