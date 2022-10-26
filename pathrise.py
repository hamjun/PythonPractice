#https://storage.googleapis.com/pathrise-app/hiring/availability_10mentors.json
#json

from collections import defaultdict
import requests

response = requests.get('https://storage.googleapis.com/pathrise-app/hiring/availability_10mentors.json')
decoded_responses = response.json()
d = dict()

for item in decoded_responses:
    d[item["email"]] = item["availability"]


#iterate through every 30 45 minte start times
def avail(start, end):  #assume this is given also as strings (same input type as t)
    
    availD = defaultdict(lambda: [])
    for e, a in d.items():
        for times in a.values():
            for t in times:
                if t in [start, end]:
                    availD[e].append(t)
    
    return availD

#test cases
print(avail("2022-03-10T13:00:00-08:00","2022-03-11T13:00:00-08:00"))
print(avail("2022-03-28T13:00:00-07:00","2022-03-29T14:30:00-07:00"))
print(avail("2023-03-10T13:00:00-08:00","2023-03-11T13:00:00-08:00"))
