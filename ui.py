# restaurant api caller
# ui.py

import log

# main menu display
def display_menu():

    log.write_to_log("Display menu shown.")
    # Display choices for user, return users selection
    print('''
        1. Pick a place to eat
        2. Pick a movie
        q. Quit
    ''')

    choice = input("Enter your selection: ")
    return choice

# prompts user for y or n, returns choice
def prompt_for_more():
    choice = input("Want info on another restaurant? (y/n) ")
    return choice

def print_to_user(content):
    # get message from somewhere else in project, print to user
    log.write_to_log("Content printed to user.")
    print(content)
