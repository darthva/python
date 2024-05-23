#!/usr/bin/python3



def valid(str1,str2,r):
    str1 = str1 + str2
    if r == str1:
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':

    str1 = "SAM"
    str2 = "JOHN"
    r = "SAMLJOHN"
    res= valid(str1,str2,r)
    print (res)