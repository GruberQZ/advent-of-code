pattern = 'hxbxwxba'

def IncrementPattern(pattern):
    # Find the right-most position in pattern that is not a 'z'
    for j in range(len(pattern)-1,-1,-1):
        if pattern[j] == 'z':
            continue
        else:
            break
    # Increment the character in the j position
    newpattern = '' + pattern[0:j]
    newpattern = newpattern + chr(ord(pattern[j])+1)
    filler = ''
    charsToAdd = (len(pattern) - 1) - j
    for k in range(0,charsToAdd,1):
        filler = filler + 'a'
    newpattern = newpattern + filler
    return newpattern

# Main function
while(True):
    # Need to check and see if all conditions are met
    criteria1 = False
    # First condition: contains one "straight" of 3 letters
    # Ex: 'abc' or 'fgh'
    for i in range(len(pattern)-2):
        firsttwo = ord(pattern[i+1]) - ord(pattern[i])
        secondtwo = ord(pattern[i+2]) - ord(pattern[i+1])
        if firsttwo == 1 and secondtwo == 1:
            criteria1 = True
    # Check criteria1 - if False, increment pattern and return to beginning of loop
    if criteria1 == False:
        pattern = IncrementPattern(pattern)
        continue

    # Second condition: does not contain the letters i, o, or l
    if 'i' in pattern or 'o' in pattern or 'l' in pattern:
        pattern = IncrementPattern(pattern)
        continue

    repeatedChar = ''
    countRepeated = 0
    # Third condition: Two different, non-overlapping pairs of letters - 'aa' and 'ee'
    for m in range(len(pattern)-1):
        if pattern[m] == pattern[m+1]:
            if repeatedChar != '' and repeatedChar != pattern[m]:
                countRepeated += 1
            elif repeatedChar == '':
                countRepeated += 1
                repeatedChar = pattern[m]
    if countRepeated < 2:
        pattern = IncrementPattern(pattern)
        continue

    # Passed all 3 criteria, break
    break

print(pattern)