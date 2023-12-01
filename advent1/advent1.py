
def main():
    #go line by line through file, split into characters, add to a list
    #then find first integer by looping through list from front
    #loop through list from end to find last int
    #if there's only one int it's counted twice
    #stick the strings together then convert to int
    #add to list

    #once we've looped through all the lines, add each int in the list and return

    calibration = open("calibrate.txt")
    numbers = []
    for line in calibration:
        lst = []
        lineNum = []
        for letter in line:
            lst.append(letter)
        for char in lst:
            if char.isnumeric():
                lineNum.append(char)
                break
        lst.reverse()
        for char in lst:
            if char.isnumeric():
                lineNum.append(char)
                break
        cal = lineNum[0]+lineNum[1]
        cal = int(cal)
        numbers.append(cal)

    ele = 0
    total = 0
    while ele < len(numbers):
        total = total + numbers[ele]
        ele += 1

    print(total)






main()