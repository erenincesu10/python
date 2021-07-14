
import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
#"Response [200] " means that the successful message has arrived.

result = json.loads(result.text)

#print(result[0]["title"])
#print(result[0])

for i in result:
    if i["userId"] == 1:
        print(i["title"])


#print(type(result))
