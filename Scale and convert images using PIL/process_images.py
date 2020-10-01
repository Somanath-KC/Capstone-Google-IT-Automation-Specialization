#!/usr/bin/env python3

from PIL import Image
import os


# Raw Images Folder Location
raw_images_folder = './data/images'

# Destination folder location to save output Images
output_folder = './data/processed-images'

# Traversing the each file in the raw images folder
for file in os.listdir(raw_images_folder):
    image_file_path = os.path.abspath(os.path.join(raw_images_folder, file))
    print(image_file_path)
    output_file_path = os.path.abspath(os.path.join(output_folder, file))

    # Open the image file with Pil Library
    image = Image.open(image_file_path)

    # Process the image matching the requriments
    new_image = image.rotate(90).resize((128, 128))
    new_image.convert('RGB').save(output_file_path, 'jpeg')
