
file = open('day9part1.txt','r')

for line in file:
	data = line.split(' ', 4)
	print(data[0] + data[2] + str(data[4]))