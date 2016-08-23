import re
import itertools

input = open('day13input2.txt','r')
regex = re.compile(r"(.*)\swould\s([a-z]{4}\s\d+)\shappiness\sunits\sby\ssitting\snext\sto\s(.*)\.")
gainregex = re.compile("gain")
data = []
people = []
maximumHappiness = 0

def happinessValue(person,neighbor):
    # Iterate through data and find the correct record
    for entry in data:
        if person == entry[0] and neighbor == entry[1]:
            return entry[2]

# Extract the data from the text file, build an array with all of the values
for line in input:
    entry = []
    m = re.search(regex,line)
    entry.append(m.group(1))
    if m.group(1) not in people:
        people.append(m.group(1))
    entry.append(m.group(3))
    value = m.group(2)
    valuearray = value.split(' ')
    if valuearray[0] == 'gain':
        entry.append(int(valuearray[1]))
    elif valuearray[0] == 'lose':
        entry.append(int(valuearray[1])*-1)
    else:
        print("Invalid amount")
    data.append(entry)

# Iterate through every possible seating arrangement
for arrangement in itertools.permutations(people):
    # Calculate happiness points for each arrangement, keep the highest value
    happiness = 0
    lastIndex = len(arrangement)-1
    for position in range(len(arrangement)):
        # Special case for beginning of list
        if position == 0:
            # Person to the left (wrap around to end of list)
            happiness += happinessValue(arrangement[position], arrangement[lastIndex])
            # Person to the right
            happiness += happinessValue(arrangement[position], arrangement[position+1])
        # Special case for end of list
        elif position == lastIndex:
            # Person to the left
            happiness += happinessValue(arrangement[position], arrangement[position-1])
            # Person to the right (wrap around to beginning of list)
            happiness += happinessValue(arrangement[position], arrangement[0])
        else:
            # Person to the left
            happiness += happinessValue(arrangement[position], arrangement[position-1])
            # Person to the right
            happiness += happinessValue(arrangement[position], arrangement[position+1])
    # Save maximum happiness value
    if happiness > maximumHappiness:
        maximumHappiness = happiness

print(str(maximumHappiness))