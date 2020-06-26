weigh = input('你體重多少:')
weigh = float (weigh)
heigh= input('你身高多少')
heigh = float (heigh) / 100
bmi = (weigh) / (heigh **2)
print ('您的bmi為:' , bmi ) 
if bmi < 18.5:
	print ('您的' , bmi , '過輕')
elif bmi >=18.5 and bmi < 24 :
		print ('您的' , bmi , '在正常值')
elif bmi >=24 and bmi < 27 :
		print ('您的' , bmi , '過重')
elif bmi >=27 and bmi <30 :
		print ('您的' , bmi , '輕度肥胖')
elif bmi >=30 and bmi <35 :
		print ('您的' , bmi , '中度肥胖')
else:
	    print ('您的' , bmi , '重度肥胖')









