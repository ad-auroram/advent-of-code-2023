# split lines into two on the |
# myNums = first part split on spaces
# winningNums = last part split on spaces
# loop through myNums, for each one matching in winnindNums, count +=1
# points = 1 if only one match, 2**count-1 otherwise
# total += points
# print total

def matching(myNums, winningNums):
    count = 0
    for num in myNums:
        for i in winningNums:
            if num == i:
                count += 1

    return count

def main():
    file = open("input4.txt")
    total = 0
    for line in file:
        points = 0
        noCard = line.split(":")
        nums = noCard[1].strip().split("|")
        myNums = nums[0].strip().replace("  ", " ").split(" ")
        winningNums = nums[1].strip().replace("  ", " ").split(" ")

        count = matching(myNums, winningNums)

        if count == 1:
            points += 1
        elif count >1:
            points += 2**(count-1)
        else:
            points+=0

        total+= points

    print(total)



main()