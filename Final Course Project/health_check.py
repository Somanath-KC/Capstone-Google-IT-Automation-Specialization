#!/usr/bin/env python3

import shutil
import psutil
from emails import generate_email, send_email
import socket


email_to = "student-01-f655e6ad970c@example.com"
email_from = "automation@example.com"
body = "Please check your system and resolve the issue as soon as possible."


def check_cpu_usage():
    """
       Sends an Email if CPU Usage is greater than 80%
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    #print(cpu_usage)
    if cpu_usage > 80:
        message = generate_email(email_from,
                                 email_to,
                                 "Error - CPU usage is over 80%",
                                 body)
        send_email(message)


def check_disk_space():
    """
       Sends an Email if Disk Space is less than 20%
    """

    hd_stats = shutil.disk_usage("/")

    if (hd_stats.free/hd_stats.total)*100 < 20:
        message = generate_email(email_from,
                                 email_to,
                                 "Error - Available disk space is less than 20%",
                                 body)
        send_email(message)


def check_memory_usage():
    """
       Send an Email if Memory is less than 500MB
    """

    free_mem = psutil.virtual_memory().available // (1024*1024)
    if free_mem < 500:
        message = generate_email(email_from,
                                 email_to,
                                 "Error - Available memory is less than 500MB",
                                 body)
        send_email(message)


def check_localhost():
    try:
        addr = socket.gethostbyname("localhost")
        if addr == "127.0.0.1":
          return True
        else:
          return False
    except socket.error:
        return False

def check_network():
    """
       Checks if localhost is being resoled
       Sends an email in case of failure
    """

    if not check_localhost():
        message = generate_email(email_from,
                                 email_to,
                                 "Error - localhost cannot be resolved to 127.0.0.1",
                                 body)
        send_email(message)

def run():
    check_cpu_usage()
    check_disk_space()
    check_memory_usage()
    check_network()


if __name__ == "__main__":
    run()