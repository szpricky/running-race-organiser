# Name: runner.py
# Author: Patrik Richard Szilagyi
# Description: Runner class


class Runner:

    # Initialization method
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no

    # __str__ method
    def __str__(self):
        return f"Runner: {self.name}\n\tID: {self.id_no}."

# End of Runner class
