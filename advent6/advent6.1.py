
Time = (54, 81, 70, 88)
Distance = (446, 1292, 1035, 1007)

# distance has to be less than the value i find
#find minimum and maximum values for time the button is held?
#time the button is held (in milliseconds) = speed the boat travels (in millimeters/millisecond)

total = []
count = 0
i=0
for time in Time:
    buttonTime = 0
    while buttonTime < time:
        if Distance[i] < buttonTime * (time-buttonTime):
            low = buttonTime
            break
        buttonTime+=1
    buttonTime = time
    while buttonTime > 0:
        if Distance[i] < buttonTime * (time-buttonTime):
            high = buttonTime
            break
        buttonTime-=1

    count = high-low+1
    total.append(count)
    i+=1

print(total[0]*total[1]*total[2]*total[3])

