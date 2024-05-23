#!/usr/bin/python3


def happy(path):
    path = path.split('|')
    dict1={}
    for i in path:
        # config length check
        if len(i[4:]) != 10:
            return "Invalid Configuration"      
        # config should be only alphanumeric
        if not (i[4:].isalnum()):
            return "Invalid Configuration"
             
        if i[:4] not in dict1:
            dict1[i[:4]] = i[4:]
        else:
            return "Invalid Configuration"  
    minval= 0000
    arr=[]
    for k,v in sorted(dict1.items()):
        if (int(k)- minval) == 1 and v not in arr :
            minval = int(k)
            arr.append(v)
        else:
            return "Invalid Configuration"
    return arr
           
if __name__ == '__main__':
    path = "0002f7c22e7904|000105d29f4a4c|000305d29f4a4b"
    res = happy(path) 
    print (res)  
