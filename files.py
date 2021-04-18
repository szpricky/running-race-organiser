# Name: files.py
# Author: Patrik Richard Szilagyi
# Description: Script for handling the .txt files

# Import modules
from runner import Runner
from race import Race


# Function to read the runners from text file
# Returns a list of objects from Runner class
def read_runners_from_file():
    # List to store the objects of the Runner class
    runners_list = []

    # Open file
    file = open("runners.txt")
    while True:
        line = file.readline().strip()
        if line == "":
            break
        data = line.split(",")

        # Variables to store data from file
        name = data[0]
        id_no = data[1]
        # Create a new Runner object
        runner = Runner(name, id_no)
        # Add runner object to list
        runners_list.append(runner)
    # End of while loop
    # Close file
    file.close()

    return runners_list
# End of read_runners_from_file function


# Function to read the venues from text file
# Returns a list with the venues
def read_venues_from_file():
    # List to store the venues
    venues_list = []

    # Open file
    file = open("races.txt")
    while True:
        line = file.readline().strip()
        if line == "":
            break

        # Create a new Race object
        venue = Race(line)
        # Add venue object to list
        venues_list.append(venue)
    # End of while loop
    # Close file
    file.close()

    return venues_list
# End of read_venues_from_file function


# Function to read the race results from a file
# Takes an object as parameter
# Returns a list of the results from Race class
def read_race_results_from_file(race):
    # List to store the objects of the Race class
    results_list = []

    # Execute code when file exists
    try:
        # Open file
        file = open(f"{race.venue.lower()}.txt")
        while True:
            line = file.readline().strip()
            if line == "":
                break
            data = line.split(",")

            # Variables to store data from file
            runner_id = data[0]
            runner_time = data[1]
            # Add results to race object
            race.add_result(runner_id, runner_time)
            # Store the race results in result variable
            result = race.show_result()
            # Add result variable to list
            results_list.append(result)
        # End of while loop
        # Close file
        file.close()
    # Execute code when file doesn't exist
    except OSError:
        print(f"No such race exists: {race.venue}")

    return results_list
# End of read_race_results_from_file function


# Main function
def main():
    print("Runners:")
    # Store runners_list in runners variable
    runners = read_runners_from_file()
    # Loop over runners
    for runner in runners:
        # Print name and id
        print(f"{runner.name}\t{runner.id_no}")
    # End of for loop

    print("\nVenues:")
    # Store venues_list in races variable
    races = read_venues_from_file()
    # Loop over races
    for race in races:
        # Print venue
        print(f"- {race.venue}")

        print("\tRace results:")
        # Store results_list in race_results variable
        race_results = read_race_results_from_file(race)
        # Loop over race_results
        for results in race_results:
            try:
                # Variables to store results data
                runner_id = results[0]
                runner_time = results[1]

                # Loop over runners
                for runner in runners:
                    # Match the IDs
                    if runner.id_no == runner_id:
                        # Print runner name, runner ID and runner time
                        print(f"\t {runner.name}\t{runner_id}\t{runner_time}")
                # End of for loop
            except IndexError as err:
                print(err)
        # End of for loop
    # End of for loop
# End of main function


# Call the main function
if __name__ == '__main__':
    main()
