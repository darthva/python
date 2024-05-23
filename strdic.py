#!/usr/bin/python3
import json

def jdict(str1):
    
    for k,v in str1.items():
        print (k,v)


    
    return

if __name__ == '__main__':

    str1={"a":"apple","b":{"b":"blueberry","c":"cranberry"}}
    res = jdict(str1)
    print (res)
