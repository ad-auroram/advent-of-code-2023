def findProduct(line):
    red = 0
    green = 0
    blue = 0
    cases = line.split(",")
    for case in cases:
        case = case.split(";")
        for i in case:
            i = i.strip()
            i = i.split(" ")
            if "red" == i[1]:
                num = int(i[0])
                if num > red:
                    red = num
            if "green" == i[1]:
                num = int(i[0])
                if num > green:
                    green = num
            if "blue" == i[1]:
                num = int(i[0])
                if num > blue:
                    blue = num
                    
    return red*green*blue
def main():
    games = open("input-day2.txt")
    total = 0
    for line in games:
        line = line.split(":")
        product = findProduct(line[1])
        total += product

    print(total)


main()