#!/usr/bin/python3
import os

def recdir(dir, targetf):
    checkdir =[x[0] for x in os.walk(dir)]
    for dirs in checkdir:
        path1 = '{0}/{1}'.format(dirs,targetf)
        #print (path1)
        if os.path.isfile(path1):
            return dirs
    return False

if __name__ == '__main__':
    direc = 'dummydir'
    targetf='target.txt'
    res = recdir(direc, targetf)
    print(res)
