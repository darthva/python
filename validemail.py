#!/usr/bin/python3
import re

def validemail(email):
    error = 0
    ok = 0
    for valid in email:
        try:
            user, rem = valid.split('@')
            web, ext = rem.split('.')
            if not re.match('^[a-zA-Z0-9_-]+$',user):
                error +=1
            elif not re.match('^[a-zA-Z0-9]+$', web):
                error +=1
            elif not re.match('^[a-zA-Z]+$', ext):
                error +=1
            elif len(ext) !=3:
                error +=1
            else:
                ok +=1
        except ValueError:
            error +=1
    return [ok,error]

if __name__ == '__main__':
    arr1=['ani@abc.com', 'shard@gmail.com', 'ab@abc']
    res= validemail(arr1)
    print (res)

