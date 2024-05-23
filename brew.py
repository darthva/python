#!/usr/bin/python3

import requests
import json

def req(url):
    re = requests.get(url)
    return re

filename = 'hwrite.json'
dict1={}
r = req('https://formulae.brew.sh/api/formula.json')
json_res = r.json()
for i in range(len(json_res)):
    try:
        name = json_res[i]['name']
    #json_str = json.dumps(json_res[0], indent=2)
        p = req(f'https://formulae.brew.sh/api/formula/{name}.json')
        parse_json= p.json()
        print(parse_json['analytics']['install']['30d'][name])
        dict1[name] = parse_json['analytics']['install']['30d'][name]
    except KeyError:
        print ('KeyError, please check')
        continue
js= json.dumps(dict1, indent=4)
with open (filename, 'w+') as w:
    print(js, file=w)
        


#https://formulae.brew.sh/api/formula/a2ps.json