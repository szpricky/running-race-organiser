# Name: module_race.py
# Author: Patrik Richard Szilagyi
# Description: Script including functions for the race that gets called when an option is selected

from module_main import *
from files import *


# Option 1 - Show the results for a race
def show_results():
    print("\nSelect a race:")
    # Load list of race objects
    races = read_venues_from_file()
    # Count the number of races
    races_no = 1
    # Loop over list of race objects
    for race in races:
        # Print the races
        print(f"{races_no}. {race.venue}")
        # Iterate the count of number of races
        races_no += 1
    # End of for loop

    while True:
        try:
            # Ask user to select a race from options
            selection = read_menu_selection("==> ", races_no)
            # Store the selected race in variable
            selected_race = races[selection - 1]

            # Print option header
            print(f"\nResults for {selected_race.venue}\n"
                  f"====================")

            # Load results from file and create lists for runners' IDs and times
            race_results = read_race_results_from_file(selected_race)
            runner_ids_list = []
            runner_times_list = []
            # Loop over the race results
            for runner_result in race_results:
                # Store results data for each runner in variables
                runner_id = runner_result[0]
                runner_time = runner_result[1]
                # Add runner's ID and time to list
                runner_ids_list.append(runner_id)
                runner_times_list.append(runner_time)
                # Print results for each runner
                print(f"{runner_id}\t{convert_time_to_min(runner_time)}")
            # End of for loop

            # Look for the winner
            winner_time = min(runner_times_list)
            winner = runner_ids_list[runner_times_list.index(winner_time)]
            print(f"\n{winner} won the race.\n")
            break
        except ValueError:
            pass
        except IndexError:
            pass
    # End of while loop
# End of show_results function


# Option 2 - Add results for a race
def add_results():
    print(f"\nAdd results for a race")
    # Store the venue in a variable
    venue = read_string("Enter venue for the race: \n==> ")

    # Open the races.txt file and check if the venue already exists
    with open("races.txt") as races_file:
        venue_list = races_file.read().splitlines()
        # If the venue does not exist then it gets added to the races.txt file
        if venue not in venue_list:
            venues_file = open("races.txt", "a")
            print(venue, file=venues_file)
            venues_file.close()

    # Load the list of Runner objects
    runners = read_runners_from_file()
    # Create a new file with the venue name
    results_file = open(f"{venue.lower()}.txt", "w")
    # Loop over runners
    for runner in runners:
        while True:
            try:
                # Ask the user for each runner's time
                runner_time = read_time_value(f"\n{runner.id_no}'s time: \n==> ")
                # Store the ID and time for each runner in runner_data
                runner_data = f"{runner.id_no},{runner_time}"
                print(runner_data)
                # If runner's time is more than 0 their result gets added to the file
                if runner_time > 0:
                    print(f"{runner_data}", file=results_file)
                break
            except ValueError:
                pass

    # Close the file
    results_file.close()

    print(f"\nRace results for {venue} added.\n")
# End of add_results function


# Option 3 - Show all competitors by county
def show_competitors_by_county():
    # Load the list of Runner objects
    runners = read_runners_from_file()

    print("\nCork runners\n"
          "------------")
    # Loop over runners
    for runner in runners:
        # If the id_no includes "CK" then the runners are from Cork
        if "CK" in runner.id_no:
            print(f"{runner.name}\t{runner.id_no}")

    print("\nKerry runners\n"
          "-------------")
    # Loop over runners
    for runner in runners:
        # If the id_no includes "KY" then the runners are from Kerry
        if "KY" in runner.id_no:
            print(f"{runner.name}\t{runner.id_no}")
    print()
# End of show_competitors_by_county function


# Option 4 - Show the winner of each race
def show_winners():
    table_header1 = "Venue"
    table_header2 = "Winner"
    print(f"\n{table_header1:18}{table_header2:6}\n"
          f"========================")

    # Load list of race objects
    races = read_venues_from_file()
    for race in races:
        # Load results from file and create lists for runners' IDs and times
        race_results = read_race_results_from_file(race)
        runner_ids_list = []
        runner_times_list = []
        for runner_result in race_results:
            # Store results data for each runner in variables
            runner_id = runner_result[0]
            runner_time = runner_result[1]
            # Add runner's ID and time to list
            runner_ids_list.append(runner_id)
            runner_times_list.append(runner_time)
        # Look for the winner
        winner_time = min(runner_times_list)
        winner = runner_ids_list[runner_times_list.index(winner_time)]
        print(f"{race.venue:18}{winner:^6}")
    print()
# End of show_winners function


# Option 5 - Show all the race times for one competitor
def show_race_times():
    # Load the list of Runner objects
    runners = read_runners_from_file()
    # Count the number of races
    runner_no = 1
    for runner in runners:
        print(f"{runner_no}. {runner.name}")
        runner_no += 1

    while True:
        try:
            # Ask user to select a runner from options
            selection = read_menu_selection("==> ", runner_no)
            # Store the selected runner in variable
            selected_runner = runners[selection - 1]

            print(f"\n{selected_runner.name} ({selected_runner.id_no})")
            print("-" * 36)

            # Load list of race objects
            races = read_venues_from_file()
            # Loop over list of race objects
            for race in races:
                # Load results from file
                race_results = read_race_results_from_file(race)
                # Loop over race_results
                for runner_result in race_results:
                    # Store results data for each runner in variables
                    runner_id = runner_result[0]
                    runner_time = runner_result[1]
                    # If the runner_id is the same as the selected runner's ID then print out the venue and their time
                    if selected_runner.id_no == runner_id:
                        print(f"{race.venue:18}{convert_time_to_min(runner_time):>18}")
            print()
            break
        except ValueError:
            pass
        except IndexError:
            pass
# End of show_race_times function


# Option 6 - Show all competitors who have won a race
def show_winning_competitors():
    print(f"\nThe following runners have won at least one race:\n"
          f"--------------------------------------------------")

    races = read_venues_from_file()
    winners = []
    for race in races:
        # Load results from file and create lists for runners' IDs and times and winners of the race
        race_results = read_race_results_from_file(race)
        runner_ids_list = []
        runner_times_list = []
        for runner_result in race_results:
            # Store results data for each runner in variables
            runner_id = runner_result[0]
            runner_time = runner_result[1]
            # Add runner's ID and time to list
            runner_ids_list.append(runner_id)
            runner_times_list.append(runner_time)
        # Look for the winner
        winner_time = min(runner_times_list)
        winner = runner_ids_list[runner_times_list.index(winner_time)]
        # Add winner to winners list
        if winner not in winners:
            winners.append(winner)

    # Load the list of Runner objects
    runners = read_runners_from_file()
    # Loop over runners
    for runner in runners:
        # If the runner has the same ID as the winner print out their name and ID number.
        if runner.id_no in winners:
            print(f"\t{runner.name} ({runner.id_no})")
    print()
# End of show_winning_competitors function


def main():
    show_results()
    add_results()
    show_competitors_by_county()
    show_winners()
    show_race_times()
    show_winning_competitors()


if __name__ == '__main__':
    main()

# END OF FILE
