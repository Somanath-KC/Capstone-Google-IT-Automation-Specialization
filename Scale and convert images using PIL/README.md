# Project Problem Statement

Your company is in the process of updating its website, and they've hired a design contractor to create some new icon graphics for the site. But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large. Oof! You're not able to get in contact with the designers and your own deadline is approaching fast. You'll need to use Python to get these images ready for launch.


## What you'll do

Use the Python Imaging Library to do the following to a batch of images:

* Open an image
* Rotate an image
* Resize an image
* Save an image in a specific format in a separate directory

The images required for the launch should be in this format:
* .jpeg format
* Image resolution 128x128 pixel
* Should be straight


## Development

Downloaing the Data
```
   mkdir data && cd data
   
   curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie

   unzip images.zip
```

Install Dependencies
```
pip3 install pillow
```

Create Script File and Grant Executable Permissions
```
touch process_images.py && sudo chmod +x process_images.py
```

Running the Script
```
    ./process_images.py
```