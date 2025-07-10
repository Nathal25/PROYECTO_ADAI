import models.Question as qs
import models.Respondent as rp
import dataestructure.red_black_three as rbt


qs_1=qs.Question(0)

resp_1= rp.Respondent('andres',0,2,2)
resp_2= rp.Respondent('juan',2,1,0)
resp_3= rp.Respondent('diana',3,1,1)


qs_1.insert_respondent(resp_1)

qs_1.insert_respondent(resp_2)

qs_1.insert_respondent(resp_3)

# print(getattr(qs_1.respondents.root.object,'name'))

avg=qs_1.calculate_opinion_average()

print(avg)

# th_1=rbt.OS_SELECT(qs_1.respondents.root,3)

# print(getattr(th_1.object,'name'))