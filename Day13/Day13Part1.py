import re

input = open('day13input.txt','r')
regex = re.compile(r"(.*)\swould\s([a-z]{4}\s\d+)\shappiness\sunits\sby\ssitting\snext\sto\s(.*)\.")
gainregex = re.compile("gain")
data = []

# Extract the data from the text file, build an array with all of the values
for line in input:
    entry = []
    m = re.search(regex,line)
    entry.append(m.group(1))
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