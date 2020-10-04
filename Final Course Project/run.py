#! /usr/bin/env python3

import os
import requests
import getpass


host_username = getpass.getuser()
description_txt_folder = '/home/{}/supplier-data/descriptions/'.format(host_username)

endpoint_url = 'http://34.69.88.113/fruits/'

for file in os.listdir(description_txt_folder):
    with open(description_txt_folder+file) as txt_file:
       name, weight, desc = txt_file.readlines()[:3]
       weight = int(weight.split(' ')[0])
       img = file.split('.')[0]+'.jpeg'
       #print(name, weight, desc, img)

       data = {'name': name.strip(),
               'weight': weight,
               'description': desc.strip(),
               'image_name': img.strip()
              }

       #print(data)
       resp = requests.post(endpoint_url, data=data)
       print(resp.status_code)