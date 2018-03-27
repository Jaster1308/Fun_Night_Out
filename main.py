# main.py

import restaurants, DBmovie, ui

# handle choice for main menu display
def handle_choice(choice):

    if choice == "1":
        restaurants.food_start()

    elif choice == "2":
        DBmovie.movie_start()

    elif choice == "q" or choice == "Q":
        ui.print_to_user("\nGoodbye!\n")
        exit(0)

    else:
        ui.print_to_user("Please enter a valid selection")

# main function
def main():
    ui.print_to_user("\nWelcome to Fun Night Out!")

    quit = "q"
    choice = None

    # main menu display loop
    while choice != quit:
        choice = ui.display_menu()
        handle_choice(choice)
    # close log file    
    log.close_file()


main()
