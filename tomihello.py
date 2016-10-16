def hello():
    if len(sys.argv)<2:
        world()
    else:
        name()

def world():
    print("Hello World!")

def name():
    print("Hello "+sys.argv[1]+"!")

import sys
hello()