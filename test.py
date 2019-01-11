from PyDebug import Log
from PyDebug import Logger


testdict = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}


Logger.level = 8
print(Logger.format)

for i in range(0, 100):
    Log("test at level ", i, level=i)

Log("-"*20)
Logger.level = 3
print(Logger.format)
for i in range(0, 100):
    Log("level ", i, level=i)


Log("-"*20)

Log(testdict)
