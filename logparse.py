#!/usr/bin/python3

import datetime
import json

def logfun(logs):
    dict1={}
    error = 0
    list1 = []
    counter = 0
    list2=[]
    with open (logs, 'r+') as r:
        try:
            lines = r.readlines()
            for line in lines:
                line = line.split(' ')
                if line[2] == '[ERROR]':
                    error +=1
                    nw = line[3:5]
                    nw= " ".join(nw)
                    if nw not in dict1:
                        dict1[nw] = 1
                    else:
                        dict1[nw] += 1
                if line[2] == '[CRITICAL]':
                    list1.append(line)
        except (TypeError,ValueError):
            return "ERROR PARSING JSON"
        
        dict2={} 
        dict2['timestamp'] = '2024-05-24 19:09'
        dict2['0523']["error"] = error
            
        while (counter < 5):
            for k,v in sorted(dict1.items(), key=lambda item : item[1], reverse= True):
                dict2['0523'][k] = v
                counter +=1
    writef='write_dict.json'
    js= json.dumps(dict2, indent=4)
    with open (writef, 'w') as w:
        print (js, file=w)
    return dict2

if __name__ == '__main__':
    filen='demo.log'
    res = logfun(filen)
    print (res)