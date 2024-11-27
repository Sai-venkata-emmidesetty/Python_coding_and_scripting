#in the link,you need to print the people who boarded ISS and Tiangong

import json
import requests
IFSS=[]
Tiangong=[]
def extractions(url):
    data=requests.get(url)
    # this will get only the output- <Response [200]>, In orger to get api data/api response we stored all data in dump varibale
    print(requests.get(url)) 
    #This method is used to convert the response from an API 
    # (usually obtained using libraries like requests in Python) into a Python dictionary or list. 
    # When you send an HTTP request, you often get data back in JSON format, 
    # and json() parses that JSON into a native Python data structure.
    dump=data.json() 
    original=dump['people']
    for peoples in original:
        if peoples['craft']=='ISS':
            IFSS.append(peoples['name'])
        else:
            Tiangong.append(peoples['name'])
    return IFSS,Tiangong
names_of_people=extractions("http://api.open-notify.org/astros.json")
print(f"people borded the IFSS : {names_of_people[0]}")
print(f"people borded the Tiangong : {names_of_people[1]}")