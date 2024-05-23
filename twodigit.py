#!/usr/bin/python3

def twodigit(num1, num2):

    prod = num1* num2
    if prod < 10 :
        return prod
    
    count =0
    list1=[]
    twodig =0
    while (count < 2):
        p1=prod%10
        prod= prod/10
        #print (prod)
        twodig = (count * 10 * p1) + twodig
        count +=1
    return round(twodig)

if __name__ == '__main__':

    num1 = 123
    num2 = 12
    res= twodigit (num1, num2)
    print (res)