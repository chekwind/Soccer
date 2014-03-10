import json
import random
import math
import datetime
import time

startTime=datetime.datetime.now()
finishTime=startTime+datetime.timedelta(seconds=7200)
startTime=int(time.mktime(startTime.timetuple()))
finishTime=int(time.mktime(finishTime.timetuple()))

print finishTime-startTime