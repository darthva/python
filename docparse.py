#!/usr/bin/python3
import json 
def docparse(doc, query):
    for i in doc['details']:
        for j in (i['field5']['nested']['other']):
            print (j)

if __name__ == '__main__':
    f = open('doc.json')
    data= json.load(f)
    #print (data)
    query = 'field1'
    res = docparse(data, query)

    