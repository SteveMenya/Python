import os, sys  # not on one line
import os  # this is better
import sys

from datetime import datetime

if datetime.now().isoweekday() == 5:
    print('Thank God Its Friday')  # stick to indention with 4 spaces not tabs

greet, Greet, GREET = 'hello', 'howdy', 'hola'  # identifiers are case sensitive

say_hello = 'hi'  # use underscores to separate identifier words


def my_func():
    print(say_hello)


my_func()  # usind functions

days = [
    1, 2, 3  # preffered closing bracket alignment, same for parentheses and curlies
]

days1 = [
    1, 2, 3  # this is also ok
]


class SomeFuncClass(object):  # use CapWords notation for class names
    pass


def my_func2(arg1, arg2,  # start argumrnts beneath other arguments
             arg3):
    pass
