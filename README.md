# PyLog
My Custom Debugger

### Basic Use:
 ```Py
from PyLog import Logger, Log, Warn, Error
#Default logger level is 5.
# Logger.level = 8

Log("Hello World") #will log at level 0 (will always show)
Log("Hello World", level=3) #Will log at the level 3
Error("Hello World") #Will log at the Error level
Warn("Hello World") #will log at the warning level
 ```
```
[18 Aug 2019] [07:05:55 PM] [0] [<stdin>.<module>:4] >> Hello World
```


### Setting the debug level and custom format:
```Py
from PyLog import Log, Logger

Logger.level = 4 #Anything over level 4 wont be shown in stdout
Logger.error_level = 3 #sets anything between level 3 and the loggers level to be classed as an error.

#The warning level (orange) is (error level + 1) / 2) rounded.

Logger.format = "[(level)] [(date)] [(time)] [(file).(function):(line)] >> (data)" 
#[1] [18 Aug 2019] [06:56:14 PM] [debugger.py.Log:95] >> {'a': 1, 'b': 2, 'c': 3}

Logger.time = "%I:%M:%S %p" #sets the time format
Logger.date = "%d %b %Y" #sets the date format

```
The formula for the format are a combination of any characters and `(<var>)`
where \<var> is one of the following:
* date 
* time
* level
* file
* function
* line
* data


The time and date formats follow the datetime modules format:
        https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior
