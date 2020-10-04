#!/usr/bin/env python3

from PIL import Image
import os
import getpass


raw_images_folder = '/home/{}/supplier-data/images'.format(getpass.getuser())

# Traversing through each file in the raw images folder
for file in os.listdir(raw_images_folder):
    if '.tiff' in file:
      image_file_path = os.path.abspath(os.path.join(raw_images_folder, file))

      image = Image.open(image_file_path).resize((600,400))
      image.convert('RGB').save(image_file_path[:-4]+'jpeg', 'jpeg')