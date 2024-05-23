#!/usr/bin/python3

def checkdup(nums):

    dict1={}
    for i in nums:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i] += 1 

    for k,v in dict1.items():
        if v == 1:
            return k
    return -1
        
if __name__ == '__main__':
    num = [1,1,2,2,3]
    ans =checkdup(num)
    print (ans)

    
    