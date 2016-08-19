import sys
file = open('day9part1.txt','r')

# Initialize collections/counters
citydata = []
citiesToVisit = set()
distanceTraveled = 0

# Build an array of all possible paths and the length of each
for line in file:
	data = line.strip('\n').split(' ', 4)
	citydata.append([data[0],data[2],int(data[4])])
	citydata.append([data[2],data[0],int(data[4])])
	citiesToVisit.add(data[0])
	citiesToVisit.add(data[2])

# Find the smallest length in city data
shortest = citydata[0]
for entry in citydata:
	if entry[2] < shortest[2]:
		shortest = entry

# Starting city
currentCity = shortest[0]
citiesToVisit.remove(currentCity)
# Traverse the cities according to Dijkstra's algorithm
while(len(citiesToVisit) > 0):
	# Find shortest path beginning with currentCity
	shortestPath = [currentCity,'',sys.maxsize]
	# Look at all of the city data where currentCity is in the first position
	for entry in citydata:
		if shortestPath[0] == entry[0]:
			# Destination must be in the list of citiesToVisit
			if entry[1] in citiesToVisit:
				if entry[2] < shortestPath[2]:
					shortestPath = entry
	# Leave the currentCity and travel to the next one
	# Log the distance traveled
	distanceTraveled += shortestPath[2]
	# currentCity is now city that was just traveled to
	currentCity = shortestPath[1]
	# Remove currentCity from list of places to travel
	citiesToVisit.remove(currentCity)
	# Keep traveling until there are no more cities to visit

print(str(distanceTraveled))