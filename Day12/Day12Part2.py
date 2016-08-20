
def isANumber(c):
    if c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9':
        return True

with open('day12input.txt','r') as file:
    data = file.read().replace('\n','')

currentNumber = ''
negative = False
numberMode = False
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
            if data[i-1] == '-':
                negative = True
            else:
                negative = False

print(str(total))