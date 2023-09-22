import requests
import json
import os

url = 'http://worldtimeapi.org/api/ip'
response = requests.request(method='GET', url=url)

x = json.loads(response.text)

f=open('file.out','w')
f.write(os.environ['SECRET1'])
json.dump(x, f)
f.close()

f=open('test.json','w')
f.write(os.environ['SECRET1'])
json.dump(x, f)
f.close()
