import sys
file = open('day9part1.txt','r')

# Initialize collections/counters
citydata = []
cities = set()
citiesToVisit = set()
citiesToVisitBackup = set()
distanceTraveled = 0
longestDistance = 0

# Build an array of all possible paths and the length of each
for line in file:
    data = line.strip('\n').split(' ', 4)
    citydata.append([data[0],data[2],int(data[4])])
    citydata.append([data[2],data[0],int(data[4])])
    cities.add(data[0])
    cities.add(data[2])
    citiesToVisit.add(data[0])
    citiesToVisit.add(data[2])
    citiesToVisitBackup.add(data[0])
    citiesToVisitBackup.add(data[2])

# Find the longest length in city data
# longest = citydata[0]
# for entry in citydata:
# 	if entry[2] > longest[2]:
# 		longest = entry

# Try starting in each city and find the longest path
for city in cities:
    currentCity = city
    citiesToVisit.remove(currentCity)
    # Traverse the cities according to the inverse of Dijkstra's algorithm
    while(len(citiesToVisit) > 0):
        # Find longest path beginning with currentCity
        longestPath = [currentCity,'',0]
        # Look at all of the city data where currentCity is in the first position
        for entry in citydata:
            if longestPath[0] == entry[0]:
                # Destination must be in the list of citiesToVisit
                if entry[1] in citiesToVisit:
                    if entry[2] > longestPath[2]:
                        longestPath = entry
        # Leave the currentCity and travel to the next one
        # Log the distance traveled
        distanceTraveled += longestPath[2]
        # currentCity is now city that was just traveled to
        currentCity = longestPath[1]
        # Remove currentCity from list of places to travel
        citiesToVisit.remove(currentCity)
        # Keep traveling until there are no more cities to visit
    # Update longest distance if applicable
    if distanceTraveled > longestDistance:
        longestDistance = distanceTraveled
    # Reset test
    distanceTraveled = 0
    for i in citiesToVisitBackup:
        citiesToVisit.add(i)

print(str(longestDistance))