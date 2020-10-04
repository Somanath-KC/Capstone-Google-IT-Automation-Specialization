#!/usr/bin/env python3

import os
import requests
import getpass


url = "http://localhost/upload/"

images_directory = "/home/{}/supplier-data/images".format(getpass.getuser())

for file in os.listdir(images_directory):
    if '.jpeg' in file:
      with open('{}/{}'.format(images_directory,file), 'rb') as opened:
          req = requests.post(url, files={'file': opened})
