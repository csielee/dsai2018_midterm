
# coding: utf-8

import requests
from config import data
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--answer',
                       default='answer.csv',
                       help='answer csv file')
parser.add_argument('--name',
                        default='answer.csv',
                        help='upload file name')
parser.add_argument('--desc',
                        default='this is my answer',
                        help='description on web')
args = parser.parse_args()

filename = 'answer.csv'

files={'files': open(args.answer,'rb')}

data["filename"] = args.name
data["description"] = args.desc

url = 'https://biendata.com/competition/kdd_2018_submit/'

response = requests.post(url, files=files, data=data)

print(response.text)


