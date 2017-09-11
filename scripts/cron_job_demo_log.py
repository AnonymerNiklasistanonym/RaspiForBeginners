# -*- coding: utf-8 -*-

"""Python script for a cron job function demo."""

import datetime
import os

# this get's us the path of the PI's home directory
# this is important, because every cron job script will be
# run from the home directory - even when it's not there
PATH_HOME_DIR = os.path.expanduser('~')

# Directory where we want to create the log
PATH_FILE_DIR = os.path.join(
    PATH_HOME_DIR, 'Documents/GitHubBeta/RaspiForBeginners/scripts')

# Path of the log file
PATH_FILE = os.path.join(PATH_FILE_DIR, 'log.txt')

# Check if the directory exists, if not create it
if not os.path.exists(PATH_FILE_DIR):
    os.makedirs(PATH_FILE_DIR)

# get the current time
DATE_TIME = datetime.datetime.now()
DATE = DATE_TIME.date()  # gives date
TIME = DATE_TIME.time()  # gives time
DATE_STRING = str(DATE.year) + "-" + \
    str(DATE.month).zfill(2) + "-" + str(DATE.day).zfill(2)
TIME_STRING = str(TIME.hour).zfill(2) + ":" + \
    str(TIME.minute).zfill(2) + ":" + str(TIME.second).zfill(2)

# create a file and add the current time or if it exists just add the current time
with open(PATH_FILE, "a+") as text_file:
    text_file.write("The script was executed at " +
                    TIME_STRING + " on " + DATE_STRING + "\n")

# read file to the console (https://stackoverflow.com/a/5214587/7827128)
with open(PATH_FILE) as file:
    COMPLETE_FILE = file.readlines()

# strip every entry and print it to the console (remove '\n')
for rows in COMPLETE_FILE:
    print(rows.strip())
