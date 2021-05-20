from datetime import datetime
from threading import Timer
import takepics as tp

x=datetime.today()

#asleep
#y=x.replace(day=x.day+1, hour=4, minute=0, second=0, microsecond=0)

#up
#y=x.replace(day=x.day, hour=6, minute=20, second=0, microsecond=0)

print(y)

delta_t=y-x

secs=delta_t.seconds+1

t = Timer(secs, tp.takepic)
t.start()
