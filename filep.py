#!/usr/bin/python3
import re

def parse(files):

    for file in files:
        with open(file, 'r') as f:
            lines= f.readlines()
            for line in lines:
                if 'error' in line:
                    print (line)
                line.replace("key", "vaalue")

    return 
if __name__ == '__main__':
    filename = ['file1.txt', 'file2.txt']
    res = parse(filename)
