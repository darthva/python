#!/usr/bin/python3
import json
def parse(deploy):
    deploy =json.dumps(deploy)
    y = json.loads(deploy)
    errors =0
    failed =0
    success =0
    for i in y:
        try:
            if len(i["deployment_id"]) !=12 or i["deployment_id"][:2] != 'd-' or not i["deployment_id"][2:].isalnum():
                errors +=1
                continue
            if i["status"] == "Success":
                success +=1
            elif i["status"] == "Fail":
                failed +=1
            else:
                errors +=1
        except (KeyError,TypeError):
            errors +=1
    return [success, failed, errors]
        
    
if __name__ == '__main__':

    deploy=[
    {"deployment_id": "d-123456abcd", "status": "Success"},
    {"deployment_id": "d-098765efgh", "status": "Fail"},
    ]
    res = parse(deploy)
    print (res)