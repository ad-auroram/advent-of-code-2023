Time = 54817088
Distance = 446129210351007

# same code but I shmushed the numbers together


count = 0
i=0

buttonTime = 0
while buttonTime < Time:
    if Distance < buttonTime * (Time-buttonTime):
        low = buttonTime
        break
    buttonTime+=1
buttonTime = Time
while buttonTime > 0:
    if Distance < buttonTime * (Time-buttonTime):
        high = buttonTime
        break
    buttonTime-=1

count = high-low+1

i+=1

print(count)