from functools import *

def union(*ar):
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList