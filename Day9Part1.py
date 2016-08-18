
file = open('day9part1.txt','r')

for line in file:
	data = file.readline()
	splitdata = data.split(' ', 5)
	print(splitdata[0] + splitdata[2] + str(splitdata[4]))