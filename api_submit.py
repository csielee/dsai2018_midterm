
# coding: utf-8

import requests
from config import data 

filename = 'answer.csv'

files={'files': open(filename,'rb')}

data["filename"] = filename
data["description"] = 'this is my answer'

url = 'https://biendata.com/competition/kdd_2018_submit/'

response = requests.post(url, files=files, data=data)

print(response.text)


