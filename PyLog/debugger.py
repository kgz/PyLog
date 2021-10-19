#!/usr/bin/env python
"""."""
import datetime
from os import environ
import sys
import inspect
import subprocess
import json

subprocess.call('', shell=True)

__colours__ = {
    "reset":'\033[0m',
    "red": '\033[38;2;247;0;0m',
    "green": "\033[38;2;32;247;0m",
    "orange": "\033[38;2;255;165;0m"
}

class jsonSettings:
    def __init__(self, *args, **kwargs):
        """."""
        self.skipkeys=True
        self.ensure_ascii=True
        self.check_circular=True
        self.allow_nan=True
        self.cls=None
        self.indent="\t"
        self.separators=None
        self.default=None
        self.sort_keys=True

class Logger:
    """\n
        A Logging module used to easily control logging.

    This is automatically called when importing the module:

    .. code-block:: python
        from PythonDebugger import Logger, Log
        Logger.level = 3
        Log("test", level=2)
    
    Attributes
    -----------
    format : string format to use:
        ..code-block:: python
            Logger.format = "[(date)] [(time)] [(level)] [(file).(function):(line)] >> (data)"
            Log("Test")
            output > [05 Oct 2018] [09:55:57 PM] [1] [test.py.main:7] >> test
    time : The time format to use see:
        https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior
    date : The date format to use see:
        https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior


    """

    def __init__(self, *args, **kwargs):
        """."""
        self.format = "[(date)] [(time)] [(level)] [(file).(function):(line)] >> (data)"
        self.time = "%I:%M:%S %p"
        self.date = "%d %b %Y"
        self._level = kwargs.get("level", 0)
        self.error_level = round(kwargs.get("error_level", self.level/3 * 2))
        self.json = jsonSettings         
  
    @property
    def warning_level(self):
        """."""
        return round((self.error_level + 1) / 2)

    @property
    def level(self):
        """."""
        return self._level

    @level.setter
    def level(self, level):
        """Set The logging Level."""
        try:
            self._level = int(level)
            self.error_level = round((self.level+1)/3 * 2)
            self.Warn("Debug level set to:", self.level)
            self.Warn("Error level set to:", self.error_level)

        except ValueError:
            raise ValueError("Value {} is not an int.".format(level))

    def Error(self, *args, **kwargs):
        """Outputs an error."""
        kwargs['level'] = self.error_level
        self.Log(*args, **kwargs)

    def Warn(self, *args, **kwargs):
        """Outputs a Warning."""
        kwargs['level'] = self.warning_level
        self.Log(*args, **kwargs)

    def Log(self, *args, **kwargs):
        """Outputs a Log."""
        return Log(self, *args, **kwargs)

    def __exit__(self, exc_type, exc_value, traceback):
        self.Warn("Exiting.")


class Log:
    def __init__(self, logger, *args, **kwargs):
        """
        Debugs at diffrent levels.
        """
        self.logger = logger
        lvl = self.logger._level
        if  lvl >= kwargs.get("level", kwargs.get("lvl", 1)) or lvl == 0:
            time = datetime.datetime.now().strftime(self.logger.time)
            date = datetime.datetime.now().strftime(self.logger.date)
            level = kwargs.get('level', 1)
            file = kwargs.get("file", sys.stdout)
            curframe = inspect.currentframe()
            ins = inspect.getouterframes(curframe, 2)
            # print(ins[2])
            filename = ins[2][1].split("\\")[-1]
            caller = ins[2][3]
            line = ins[2][2]

            color = __colours__.get("green") 
            if self.logger.warning_level <= level < self.logger.error_level:
                color = __colours__.get("orange")
            elif level >= self.logger.error_level:
                color = __colours__.get("red")

            def yellow(string):
                return __colours__.get("orange") + str(string) + __colours__.get("reset")

            replacements = {
                "date": yellow(date),
                "time": yellow(time),
                "level": color +str(level) + __colours__.get("reset") ,
                "file": yellow(filename),
                "function": yellow(caller),
                "line": yellow(line),
                "data": color + ' '.join(str(i) for i in args) +  __colours__.get("reset")
            }
            string = self.logger.format
            for x in replacements:
                if(type(x) == dict):
                    string = json.dumps(x, *vars(self.logger.json))

                try:
                    string = string.replace("({})".format(x), str(replacements[x]))
                except Exception as exc:
                    print(exc)
            
            print(string,  end=__colours__.get("reset") + "\n\r")
            #return f"<Log output={string}{__colours__.get('reset')}\\n\\r level={lvl}>"


