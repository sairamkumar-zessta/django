import requests 
import json
URL =""
data = {
    'name' : 'sai',
    'roll' : 101,
    'city' : 'Ranchi'
} 
json_data = json.dump(data) 
r = requests.post(url = URL , data = json_data) 
data = r.json() 
print(data)