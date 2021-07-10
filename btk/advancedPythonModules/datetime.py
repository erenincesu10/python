
from datetime import timedelta
from datetime import datetime
#from datetime import date
#from datetime import time


simdi = datetime.now() #datetime.today() same

result = simdi.year
result = simdi.month

result = datetime.ctime(simdi)
result = datetime.strftime(simdi, '%Y') # year
result = datetime.strftime(simdi, '%X') # hour

t = '21 April 2019 hour 10:12:15'

dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')

#print(dt)

birthday = datetime(1985,4,7,11,35,20)

result = datetime.timestamp(birthday)# second info
result = datetime.fromtimestamp(result) #second to datetime
result = datetime.fromtimestamp(0) #milestones for computers

result = simdi - birthday # timedelta obj

#result = result.days
#result = result.seconds

result = simdi + timedelta(days=10)


print(result)
