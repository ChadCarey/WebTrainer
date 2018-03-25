import json

def ToJson(data):
    if type(data) == list:
        outJsonArray = []
        for d in data:
            outJsonArray.append(d.dict)
        return json.dumps(outJsonArray)

