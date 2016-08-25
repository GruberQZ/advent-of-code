import re

regex = re.compile(r"(.*)\scan\sfly\s(\d+)\skm\/s\sfor\s(\d+)\sseconds,\sbut\sthen\smust\srest\sfor\s(\d+)\sseconds\.")
input = open('day14input.txt','r')
data = []
distanceTraveled = {}
points = {}
flyingSpeed = {}
flyingTime = {}
restingTime = {}

for line in input:
    entry = []
    m = re.search(regex,line)
    # Add reindeer to the points and distanceTraveled dicts
    distanceTraveled[m.group(1)] = 0
    points[m.group(1)] = 0
    # Speed in km/s
    flyingSpeed[m.group(1)] = m.group(2)
    entry.append(int(m.group(2)))
    # Length of time reindeer can travel in seconds
    entry.append(int(m.group(3)))
    # Resting time needed in seconds
    entry.append(int(m.group(4)))
    data.append(entry)

# Reindeer need to run together
#for time in range(1,2504,1):
