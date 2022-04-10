<img src="https://marketing.cit.ie/contentfiles/images/MTU/Logos/MTU_Logo_Colour_RGB_300dpi.jpg" alt="MTU" width="25%" />

##### CR106 - BSc Honours Software Development

# SOFT6018 - Programming Fundamentals Project

## Running Race Organiser

Runners like to compete with each other in an attempt to improve their times.

A series of races take place in different venues around Cork and Kerry.

Records are kept of the runners and the races.

**Races.txt holds the venues for the races:**

```
Currabinny
Glengarriff
```

**Runners.txt holds the name and the identification code for each runner registered:**

```
Anna Fox,CK-24
Des Kelly,CK-23
Ann Cahill,KY-43
Joe Flynn,CK-11
Sally Fox,KY-12
```

When a race takes place, a file is created for that race which holds the identification code of each runner and their time in seconds.

**currabinny.txt holds the ids and times (in seconds) for each runner at Currabinny:**

```
CK-24,3040
KY-43,2915
CK-11,3245
CK-23,2900
```

**glengarriff.txt hold the ids and times (in seconds) for each runner at Glengarriff:**

```
CK-24,3245
KY-43,3151
CK-23,3240
KY-12,3199
```

You have been asked to develop an application to help the organisers maintain, view and edit these records.

The application should offer the following menu of items repeatedly until the user chooses to quit the application:

```
1. Show the results for a race
2. Add results for a race
3. Show all competitors by county
4. Show the winner of each race
5. Show all the race times for one competitor
6. Show all competitors who have won a race
7. Quit
```

### 1. Show the results for a race

Show the user the list of races, invite the user to select a race from the list (using a number) and display the runners' identification codes along with their times in minutes and seconds. Display the identification code for the winner of the race.

```
1: Currabinny
2: Glengarriff
Choice > 2

Results for Glengarriff
======================
CK-24   54 min   5 seconds
KY-43   52 min  31 seconds
CK-23   54 min   0 seconds
KY-12   53 min  19 seconds

KY-43 won the race.
```

### 2. Add results for a race

Ask the user for the race's venue and add it to the races file.

Display a list of each competitor's name from the runners' file, ask the user for the time in which they ran the race in seconds (0 if they did not run the race). Store the results (identification code and time ) in a newly created file e.g. fota.txt if the venue was Fota.

### 3. Show all competitors by county

List all the competitors but organise them by county.

```
Cork runners
------------
    Anna Fox    CK-24
    Des Kelly   CK-23
    Joe Flynn   CK-11

Kerry runners
-------------
    Ann Cahill  KY-43
    Sally Fox   KY-12
```

### 4. Show the winner for each race

List the races along with the id of the winner of each race in a nicely formatted table.

```
Venue           Winner
=======================
Currabinny      CK-23
Glengarriff     KY-43
```

### 5. Show all the race times for one competitor

Display a list of people to choose from.

Once the user chooses a person display their name, identification code. For each race that they ran in show their time and their position in the race. The time is shown in minutes and seconds.

```
1: Anna Fox
2: Des Kelly
3: Ann Cahill
4: Joe Flynn
5: Sally Fox
Which runner > 1

Anna Fox (CK-24)

Currabinny      50 mins 40 secs (3 of 4)
Glengarriff     54 mins  5 secs (4 of 4)
```

### 6. Show all competitors who have won a race

List the codes and names of those runners who have won at least one race.

```
The following runners have all won at least one race:
-----------------------------------------------------
Des Kelly (CK-23)
Ann Cahill (KY-43)
```

## Project Development Guidelines

All inputs must be validated but this is not mentioned here.

### **Version 1** - Implement Menu

1. Write a main function that displays the menu.
2. When each menu item is chosen print a message.
3. Create a loop so that the user can repeatedly choose menu items until they choose to quit.

### **Version 2** - Load Data Files

1. Make sure that the data files are in the same directory as your project code file.
    - races.txt
    - people.txt
    - Currabinny.txt
    - Glengarriff.txt
2. Write a function that loads the data from people.txt into lists. The data from the file should be stored in to parallel lists – one list of the competitors name and one for their id – or a list of objects created from a suitable class e.g. Runner class.
3. Write a function that loads the data from races.txt into a list.
4. Write a function that loads the data from a race file given the name of the race. The data from the file should be stored in to parallel lists – one list of the competitors' ids and one for the time – or a list of objects instantiated from a class.
5. Print out these lists in order to test your program is working.

### **Version 3** - Implement Menu Option 1 (Show the results for a race)

1. Display the list of race locations and add a number before each venue.
2. Allow the user choose a location from the list by entering a number
3. Print out the corresponding location.
4. Load the race data for this race and display the competitor ids and their times in a columnar format.
5. Modify the code so that the times are shown in minutes and seconds.
6. Find the fastest time. You might use the `min` function and print this.
7. Print out the id for the winner(s).

### **Version 4** - Implement Menu Option 2 (Add results for a race)

1. This option needs to get the location of a new race and update the list of race locations. (This list can be written back to the places.txt before the program exits )
2. Display the ids for all the competitors one by one so that the user can enter a time for each in seconds. A time of 0 seconds will be used to indicate the runner did not run in that race. Print this data to the screen as it is entered in the following format: `KY-12,319`
3. Create a file with the correct name for storing results. The file name should be made up of the name of the race + “.txt”. Adapt 2. so the information on each competitor is written to the file.
4. When the user chooses to quit add code to make sure that the contents of places.txt is the same as the list of race locations stored in your program. Overwrite the existing file with the current list.

### **Version 5** - Implement Menu Option 3 (Show all competitors by county)

This requires printing the competitors names and the competitors ids in two groups.

1. Print those from Cork – ( if the id starts with “CK”).
2. Print them those from Kerry – ( if the id starts with “KY”).

### **Version 6** - Implement Menu Option 4 (Show the winner for each race)

For each of the race location:

-   Load the competitor ids and race times for a particular race.
-   Identify the fastest time and corresponding competitor id.
-   print the race location and wining competitor id.

### **Version 7** - Implement Menu Option 5 (Show all Race times for one competitor)

1. Present the user with a list of runners.
2. The user selects a runner.
3. The user is shown that runner's race time for each race in which they ran.

### **Version 8** - Implement Menu Option 6 (Show competitors who have won a race)

Add functionality to display the list of those runners who have won at least 1 race.

##### Patrik Richard Szilagyi, 2021
