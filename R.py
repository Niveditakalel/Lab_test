from datetime import datetime
import pytz
local=datetime.now()
print("Local time is : ",local.strftime("%m/%d/%Y,%H:%M:%S,%p"))
tzNY=pytz.timezone('America/New_York')
x=datetime.now(tzNY)
print("New York Time : ",x.strftime("%m/%d/%Y,%H:%M:%S,%p"))


def Poem():
    print("Hello\nHow are you?")

Poem()
