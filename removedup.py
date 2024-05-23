#!/usr/bin/python3
import json

def removedup(data):
    list1= data.splitlines()
    set1 =set(list1)
    print (set1)
    dict1={}
    list2=[]
    for i,j in enumerate(list1):
        if j not in dict1.values():
            dict1[i] = j
    for k,v in dict1.items():
        list2.append(v)
    return list2

if __name__ == '__main__':
    filename = 'data.txt'
    with open(filename, "r+") as f:
        data = f.read()
        ans= removedup (data)
        print ('\n'.join(ans))
        #print (ans)
