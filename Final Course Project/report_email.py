#!/usr/bin/env python3

import os
import datetime
import getpass
from reports import generate_report
from emails import generate_email, send_email


host_username = getpass.getuser()
description_txt_folder = '/home/{}/supplier-data/descriptions/'.format(host_username)

title = "Processed Update on {}".format(str(datetime.datetime.today().strftime("%B %d, %Y")))
paragraph = []
attachment = "/tmp/processed.pdf"

for file in os.listdir(description_txt_folder):
    with open(description_txt_folder + file) as txt_file:
        name, weight = txt_file.readlines()[:2]
        name = "<br/> name: " + name.strip() + "<br/>"
        weight = "weight: " + weight.strip() + "<br/>"
        paragraph.append(name+weight)

paragraph = ''.join(paragraph)


if __name__ == "__main__":
    generate_report(attachment, title, paragraph)

    #Sending Email
    message = generate_email("automation@example.com",
                             "student-01-f655e6ad970c@example.com",
                             "Upload Completed - Online Fruit Store",
                             "All fruits are uploaded to our website successfully. \
                                A detailed list is attached to this email.",
                             attachment)
    send_email(message)