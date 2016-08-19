
currentPattern = '1113222113'
#print(currentPattern)

# Iterate 50 times
for i in range(50):
    # Reset next pattern
    nextPattern = ''
    currentCharacter = currentPattern[0]
    count = 1
    # Iterate through all of the characters in pattern, skipping the first character
    for j in currentPattern[1:]:
        # If currentCharacter matches j, increment counter
        if j == currentCharacter:
            count += 1
        # If currentCharacter does not match
        else:
            # Add to nextPattern
            nextPattern = nextPattern + str(count) + currentCharacter
            # currentCharacter becomes j, count is reset
            currentCharacter = '' + j
            count = 1
    # At the end of the loop, account for the final character group
    nextPattern = nextPattern + str(count) + currentCharacter
    # currentPattern is now nextPattern
    currentPattern = '' + nextPattern
    print(str(i))

print(str(len(currentPattern)))