from PyLog import *
from PyLog import Logger


testdict = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}


print(Logger.format)
Logger.level = 8

for i in range(0, 100):
    Log("test at level ", i, level=i)

Log("-"*20)
Logger.level = 3
for i in range(0, 100):
    Log("level ", i, level=i)


Log("-"*20)

Log(testdict)

def out():
    Error("This is an Error")
    Warn("This is a warning")
    Log("Everything's a'ok")


out()