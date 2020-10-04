#! /usr/bin/env python3

import os
import requests

feedback_files_location = "/data/feedback"

feedback_list = []

for file in os.listdir(feedback_files_location):
    feedback_file = open(r'{}/{}'.format(feedback_files_location, file))

    title, name, date, feedback = feedback_file.readlines()
    feedback_dict = {'title': title.strip(),
                     'name': name.strip(),
                     'date': date.strip(),
                     'feedback': feedback.strip()
                    }

    api_request = requests.post("http://130.211.210.91/feedback/", data=feedback_dict)
    print(api_request.status_code)