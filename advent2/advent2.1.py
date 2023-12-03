#read through line by line
# for each line, split the line on the :
# split the last part along commas
# each time a number of cubes is specified, check if the number with it is larger than the number given.
#do this by splitting along spaces


def checkCase(line):

    cases = line[1].split(",")
    for case in cases:
        case = case.split(";")
        for i in case:
            i = i.strip()
            i = i.split(" ")
            if "red" == i[1]:
                num = int(i[0])
                if num > 12:
                    return False
            if "green" == i[1]:
                num = int(i[0])
                if num > 13:
                    return False
            if "blue" == i[1]:
                num = int(i[0])
                if num > 14:
                    return False
    return True
def main():
    games = open("input-day2.txt")
    total = []
    for line in games:
        line = line.split(":")
        gameNum = int(line[0].strip("Game "))
        verify = checkCase(line)
        if not verify:
            continue
        else:
            total.append(gameNum)

    ele = 0
    ans = 0
    while ele < len(total):
        ans = ans + total[ele]
        ele += 1

    print(ans)




main()