import re
import sys
import json
from pprint import pprint

with open('day12input.txt','r') as file:
    filedata = file.read().replace('\n','')

regex = re.compile(":\"red\"")

def isANumber(c):
    if c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9':
        return True

def findNumbers(data):
    numberMode = False
    currentNumber = ''
    negative = False
    total = 0
    for i in range(len(data)):
        # in number mode
        if numberMode:
            if not isANumber(data[i]):
                # Have reached the end of this number
                # Add current number to the running total
                if negative:
                    total -= int(currentNumber)
                else:
                    total += int(currentNumber)
                # Turn off number mode
                numberMode = False
                # Reset currentNumber
                currentNumber = ''
            else:
                # Continue the current number
                currentNumber = '' + currentNumber + data[i]
        # not in number mode
        else:
            if not isANumber(data[i]):
                continue
            else:
                # Start of a number
                # Add number to currentNumber
                currentNumber = '' + currentNumber + data[i]
                # Turn on number mode
                numberMode = True
                # Check the previous character for a '-' to see if number is negative
                if data[i - 1] == '-':
                    negative = True
                else:
                    negative = False
    return total

# Current search scheme is too aggressive in taking out numbers
# Write a function that finds all the embedded objects within an object
# Examine each of those to see if they match regular expression
def eliminateRedObjects(data):
    newdata = ''
    while('{' in data or '}' in data):
        # Find the right-most left brace in data
        leftBracePos = str.rfind(data,'{',0,len(data))
        # Find the closest right brace to the right of leftBracePos
        rightBracePos = str.find(data,'}',leftBracePos,len(data))
        # Search the slice to see if it contains :"red"
        if re.search(regex, data[leftBracePos:rightBracePos+1]) == None:
            newdata += data[leftBracePos:rightBracePos+1]
            print("Added: " + data[leftBracePos:rightBracePos + 1])
        else:
            print("Deleted: " + data[leftBracePos:rightBracePos + 1])
        data = '' + data[0:leftBracePos] + data[rightBracePos+1:]
    return newdata

def eliminateRedObjects2(data):
    # Turn the string into a JSON object
    jsondata = json.loads(data)
    pprint(jsondata)

# Scan through the characters in the list and look for objects
leftBrackets = 0
leftBraces = 0
objectMode = False
objectStartPos = 0
newdata = ''

# Find objects within big string
for j in range(len(filedata)):
    if objectMode:
        # Looking for the end of the object
        if filedata[j] == '{':
            leftBraces += 1
        if filedata[j] == '}':
            # If leftBraces == 0, end of current object
            if leftBraces == 0:
                objectMode = False
                #print(filedata[objectStartPos:j+1])
                eliminateRedObjects2(filedata[objectStartPos:j+1])
            else:
                leftBraces -= 1
    else:
        # Looking for a left brace to start object mode
        if filedata[j] == '{':
            objectMode = True
            objectStartPos = j
        else:
            newdata += filedata[j]
#print(newdata)
print(str(findNumbers(newdata)))