#!/usr/bin/python3

#count number of words in txt file

def count(file):
        dict1={}
        with open(file, 'r+') as f:
                test= f.readlines()
                for line in test:
                        line= line.strip()
                        line= line.split(" ")[2]
                        print (line)
                        for j in range(len(line)):
                            if line[j] not in dict1:
                                dict1[line[j]] = 1
                            else:
                                dict1[line[j]] +=1
        return (sorted(dict1.items()))
               
                            
                        

if __name__ == '__main__':
        filename = 'data1.txt'
        res = count(filename)
        print (res)