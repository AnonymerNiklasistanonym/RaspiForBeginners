import os
import datetime

# this get's us the path of the PI's home directory
# this is important, because every cron job script will be
# run from the home directory - even when it's not there
PATH_HOME_DIR = os.path.expanduser('~')

# Directory where we want to create the log
PATH_FILE_DIR = os.path.join(PATH_HOME_DIR, 'Documents/CronDemoLog')

# Path of the log file
PATH_FILE = os.path.join(PATH_FILE_DIR, 'log.txt')

# Check if the directory exists, if not create it
if not os.path.exists(PATH_FILE_DIR):
    os.makedirs(PATH_FILE_DIR)

# get the current time
date_time = datetime.datetime.now()

date = date_time.date()  # gives date
time = date_time.time()  # gives time

date_string = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
time_string = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)

# create a file and add the current time or if it exists just add the current time
file = open(PATH_FILE, "a+")
file.write("The script was executed at " + time_string + " on " + date_string)
file.write("\n") # write newline
file.close()

# read file to the console (https://stackoverflow.com/a/43625375/7827128)
with open(PATH_FILE) as file:
     my_list = file.readlines()
my_list = [x.strip() for x in my_list]
for rows in my_list:
    print(rows)