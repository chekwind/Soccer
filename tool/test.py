import json
import random

base={}
for i in range(1,21):
	base[i]=int(3000*(1+random.randrange(0,100,2)*0.01))
print base