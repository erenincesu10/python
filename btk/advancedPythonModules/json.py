

import json

person_string = '{"name" : "Ali", "languages" : ["python","C#"]}'

#JSON str to dict
#result = json.loads(person_string)
#result = result["name"]
#result = result["languages"]

#with open("person.json") as f:
#    data = json.load(f)
#    print(data)
#    print(data["name"])
#    print(data["languages"])

person_dict = {
    "name" : "Ali",
    "languages" : ["Python","C#"]
}
"""
result = json.dumps(person_dict) #dict to JSON str
print(result)
print(type(result))
"""

#write to file
#with open("person.json","w") as f:
#    json.dump(person_dict,f)

person_dict = json.loads(person_string)

#ways of writing
result = json.dumps(person_dict, indent=4, sort_keys=True)
print(person_dict)
print(result)
