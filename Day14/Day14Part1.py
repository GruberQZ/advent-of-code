import re

regex = re.compile(r"(.*)\scan\sfly\s(\d+)\skm\/s\sfor\s(\d+)\sseconds,\sbut\sthen\smust\srest\sfor\s(\d+)\sseconds\.")
input = open('day14input.txt','r')
data = []
maximumDistance = 0

for line in input:
    entry = []
    m = re.search(regex,line)
    # Speed in km/s
    entry.append(int(m.group(2)))
    # Length of time reindeer can travel in seconds
    entry.append(int(m.group(3)))
    # Resting time needed in seconds
    entry.append(int(m.group(4)))
    data.append(entry)

# Run the race for each reindeer
for entry in data:
    # Initialize reindeer's run
    distanceTraveled = 0
    timeRemaining = 2503
    flyingMode = True
    restingMode = False
    flyingSpeed = entry[0]
    flyingTime = entry[1]
    restingTime = entry[2]
    while(True):
        if flyingMode:
            if timeRemaining - flyingTime >= 0:
                timeRemaining -= flyingTime
                distanceTraveled += flyingSpeed*flyingTime
                flyingMode = False
                restingMode = True
            else:
                break
        elif restingMode:
            if timeRemaining - restingTime >= 0:
                timeRemaining -= restingTime
                flyingMode = True
                restingMode = False
            else:
                break
    # If still in flying mode close to time limit, fly until time limit
    if flyingMode:
        distanceTraveled += flyingSpeed*timeRemaining
    if distanceTraveled > maximumDistance:
        maximumDistance = distanceTraveled

print(str(maximumDistance))