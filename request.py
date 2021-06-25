import requests
import json
from requests.api import options, request
result=requests.get('https://saral.navgurukul.org/api/courses')
data=result.json()
with open("availableCourses.json","w")as f:
    json.dump(data,f,indent=4)
def course():
    index=0
    for i in data["availableCourses"]:
        print(index+1,"...",i["name"],"...",i["id"])
        index+=1
course()