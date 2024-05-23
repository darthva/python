#!/usr/bin/python3
import json
import re
def repjson(data):
    for key, value in data['user'].items():
        value  =re.sub("\d", "x", value)
        data['user'][key] = value
    print (data)
        
if __name__ == '__main__':
    data = {"user": {"age": "16 years", "name": "Bill Gates", "weight": "200 lbs", "height": "72 in"} }
    res = repjson(data)