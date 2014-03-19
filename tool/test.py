import json
import random
import math
import datetime
import time
# win=0
# lose=0
# o=0
# for i in range(1,1000):
# 	s1=int(random.uniform(0,1.09)*100)
# 	s2=int(random.uniform(0,1)*100)
# 	if s1>s2:
# 		win+=1
# 	elif s1<s2:
# 		lose+=1
# 	else:
# 		o+=1

# print win,lose,o
# if (s1>s2):

# if i<133:
# 	zhu=random.randint(0,6)
# 	ke=random.randint(0,6)
# 	if zhu<ke:
# 		zhu,ke=ke,zhu
# 	if zhu==ke:
# 		zhu=zhu+1
# 	print zhu,":",ke
# else:
# 	zhu=random.randint(0,6)
# 	ke=random.randint(0,6)
# 	if zhu>ke:
# 		zhu,ke=ke,zhu
# 	print zhu,":",ke
goal,lose,goal1,lose1,offscore,defscore=0,0,0,0,0,0

for i in range(20):
	s1=random.randint(0,1000)
	s2=random.randint(0,1000)
	s3=random.randint(0,1000)
	s4=random.randint(0,1000)
	if s1<=343:
		goal+=1
	if s2<=36:
		lose+=1
	if s3<=36:
		goal1+=1
	if s4<=343:
		lose1+=1
	
if(goal-lose)/2<0:
	defscore-=(goal-lose)/2
elif(goal1-lose1)/2<0:
	offscore-=(goal1-lose1)/2
else:
	offscore=(goal-lose)/2
	defscore=(goal1-lose1)/2

print offscore,defscore
