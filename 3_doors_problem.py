# Create an experiment to prove changing door increases your chances of winning.

import random
import matplotlib.pyplot as plt

ntests = 100000  # Number of tests to run
i=0  # For loop count
ChangeWins = 0  # Keep track of outcomes
ChangeLost = 0
StayWins = 0
StayLost = 0
Changes = 0  # Count how many times player decided to change door
while ntests > i:  # Play the game ntests times
    Doors = ["A", "B", "C"]  # Create the 3 doors
    PrizeDoor = random.choice(Doors)  # Select a winning door at random
    #print("Prize door is:", PrizeDoor)
    NoPrizeDoors = [i for i in Doors if i!=PrizeDoor]  # Doors without prize
    PlayerDoor = random.choice(Doors)  # Player selects a door at random
    #print("Player door is:", PlayerDoor)
    HostDoors = [i for i in Doors if i!=PlayerDoor]  # Doors not selected by the player
    #print("Host doors are:", HostDoors)
    NewHostDoors = [PlayerDoor]  # Create the new set of doors which will exclude a no-prize door BUT always
                                 # includes the door selected by the player
    if PrizeDoor in HostDoors:  # New set of doors always needs to also include the winning door
        NewHostDoors.append(PrizeDoor)
    else:  # If the winning door wasn't one of the original 2 host doors, then select a host door at random
        NewHostDoors.append(random.choice(HostDoors))
    #print("New host doors are:", NewHostDoors)
    NewPlayerDoor = random.choice(NewHostDoors)  # Player selects a door at random again from the reduced set of 2 doors
    #print("New player door is:", NewPlayerDoor)
    if NewPlayerDoor != PlayerDoor:  # Account for number of changes
        Changes = Changes+1

    if NewPlayerDoor == PrizeDoor and NewPlayerDoor != PlayerDoor:  # Count all possible outcomes
        #print("You Win")
        ChangeWins = ChangeWins +1
    if NewPlayerDoor == PrizeDoor and NewPlayerDoor == PlayerDoor:
        #print("You Win")
        StayWins = StayWins +1
    if NewPlayerDoor != PrizeDoor and NewPlayerDoor != PlayerDoor:
        #print("You Lost")
        ChangeLost = ChangeLost +1
    if NewPlayerDoor != PrizeDoor and NewPlayerDoor == PlayerDoor:
        #print("You Lost")
        StayLost = StayLost +1

    #else:
        #print("You Lose")
    i = i+1

print("Player changed:",Changes,"\n")
print("Changed and won:", ChangeWins)
print("Changed and lost:", ChangeLost)
print("Player changed and won:", "{:.2%}".format(ChangeWins/Changes))
print("Player changed and lost:", "{:.2%}\n".format(ChangeLost/Changes))

Stayed = ntests - Changes
print("Player stayed:", Stayed,"\n")
print("Stayed and won:", StayWins)
print("Stayed and lost:", StayLost)
print("Player stayed and won:", "{:.2%}".format(StayWins/Stayed))
print("Player stayed and lost:", "{:.2%}\n".format(StayLost/Stayed))
wins = ChangeWins+StayWins
lost = ntests - (ChangeWins+StayWins)
print("Won:", wins)
print("Lost:", lost)
if wins+lost == ntests:
    print("OK")




# Chart creation

fig, ax = plt.subplots()

bar_x = [1.5,3.5]  #Position of bars
bar_height = [StayWins, ChangeWins]  # Bar height
bar_tick_label = ["Player Stayed and Won", "Player Changed and Won"]  # X axis bar names
bar_label = [StayWins, ChangeWins]  # Bar labels
bar_plot = plt.bar(bar_x, bar_height, color=["red", "blue"], tick_label=bar_tick_label)  # Create bars

def autolabel(rects):  # Create and apply bar labels
    for idx, rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1000+height,
                bar_label[idx],
                ha='center', va='bottom', rotation=0)

autolabel(bar_plot)  # Call autolable function

plt.xlim(0,5)  # Width of chart
plt.ylim(0, ntests*0.4)  # Height of chart is set to 40% of total number of tests

plt.title("3 Door Problem Results")  # Chart title
plt.ylabel("Number of Wins")  # Y axis label

plt.show()

