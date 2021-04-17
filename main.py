# Name: main.py
# Author: Patrik Richard Szilagyi
# Description: SOFT6017 Project 2021 - Race Organiser Application

# Import modules
from module import *
from race import *


# Function for printing the main menu
# Returns the menu selection
def menu():
    print(f"Select from the following options:\n"
          f"1. Show the results for a race\n"
          f"2. Add results for a race\n"
          f"3. Show all competitors by county\n"
          f"4. Show the winner of each race\n"
          f"5. Show all the race times for one competitor\n"
          f"6. Show all competitors who have won a race\n"
          f"7. Quit")
    selection = read_menu_selection("==> ")
    return selection
# End of menu function


# Function to ask the user to select an option and validate selection
# No return value
def select_option():
    while True:
        # Call the menu function and store the returned value in menu_selection
        menu_selection = menu()

        # If statements to validate user selection
        # Code to execute if 1st option is selected
        if menu_selection == 1:
            show_results()

        # Code to execute if 2nd option is selected
        if menu_selection == 2:
            add_results()

        # Code to execute if 3rd option is selected
        if menu_selection == 3:
            show_competitors_by_county()

        # Code to execute if 4th option is selected
        if menu_selection == 4:
            show_winners()

        # Code to execute if 5th option is selected
        if menu_selection == 5:
            show_race_times()

        # Code to execute if 6th option is selected
        if menu_selection == 6:
            show_winning_competitors()

        # Code to execute if 7th option is selected (Quit program)
        if menu_selection == 7:
            print(f"Bye bye!")
            break

    # End of while loop
# End of select_option function


# Main function
def main():
    # Call the banner function
    print_banner()

    # Call the select_option function
    select_option()
# End of main function


if __name__ == "__main__":
    # Call the main function
    main()

# END OF FILE
