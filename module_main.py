# Name: module_main.py
# Author: Patrik Richard Szilagyi
# Description: Module file for Race Organiser Application (SOFT6017 Project)

# Print the banner of the application
def print_banner():
    print(f"---------------\n"
          f"RACE ORGANISER\n"
          f"---------------")
# End of print_banner function


# Read a string from the user
def read_string(prompt):
    result = input(prompt)
    return result
# End of read_string function


# Read a positive number from the user
def read_positive_integer_number(prompt):
    while True:
        n = int(input(prompt))
        if n > 0:
            return n
    # End of while loop
# End of read_positive_integer_number function


# Read the selected menu option from the user
def read_menu_selection(prompt):
    while True:
        n = int(input(prompt))
        if 1 <= n <= 7:
            return n
    # End of while loop
# End of read_menu_selection function

# END OF FILE
