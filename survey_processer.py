import models.Question as qs
import models.Respondent as rp
import dataestructure.red_black_three as rbt


qs_1=qs.Question(0)

resp_1= rp.Respondent('andres',1,3,2)
resp_2= rp.Respondent('juan',1,3,0)
resp_3= rp.Respondent('diana',1,3,1)


qs_1.insert_respondent(resp_1)

qs_1.insert_respondent(resp_2)

qs_1.insert_respondent(resp_3)

qs_1.print_info('name')