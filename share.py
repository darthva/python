#!/usr/bin/python3
import math
def shares(arr, cap):
    
    minn =  10000
    maxn =  -10000
    for i in range(len(arr)):
        minn = min(arr[i], minn)
        sh= cap//minn
        maxn = max((arr[i]*sh) - (minn*sh), maxn)
    return maxn

if __name__ == '__main__':
    arr = [2,7,1,5,3]
    cap = 10
    res = shares(arr,cap)
    print (res)