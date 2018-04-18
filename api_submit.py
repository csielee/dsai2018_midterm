
# coding: utf-8

import requests
from config import data
import argparse 

def sendSubmission(answerfile, name='answer.csv', desc=''):
    files={'files': open(answerfile,'rb')}

    data["filename"] = name
    data["description"] = desc

    url = 'https://biendata.com/competition/kdd_2018_submit/'

    response = requests.post(url, files=files, data=data)

    return response.text

if __name__ == '__main__':
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

    print(sendSubmission(args.answer, args.name, args.desc))



