# Name: runner.py
# Author: Patrik Richard Szilagyi
# Description: Race class


class Race:
    runner_id = None
    runner_time = None

    # Initialization method
    def __init__(self, venue):
        self.venue = venue

    # __str__ method
    def __str__(self):
        return f"Race venue is {self.venue}."

    # add_result method
    def add_result(self, runner_id, runner_time):
        self.runner_id = runner_id
        self.runner_time = runner_time

    # show_result method
    def show_result(self):
        return self.runner_id, self.runner_time

# End of Race class
