# log.py
# handles writing to the file for logging

import os

# basic set up for log_file, determine folder and file_name, open for write
DATA_DIR = "data"
LOG_FILE_NAME = os.path.join(DATA_DIR, "log.txt")
log_file = open(LOG_FILE_NAME, "w")

# take in content, write it to log_file on a new line
def write_to_log(content):

    log_file.write(content + "\n")

# close log_file
def close_file():

    log_file.close()
