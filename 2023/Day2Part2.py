dayNo = 2
with open(f"Inputs\\Day{str(dayNo)}.txt","r") as file:
    fileContents = file.read()

lines = fileContents.split("\n")

red = "red"
green = "green"
blue = "blue"
powers = []

for line in lines:
    redMax = 0
    greenMax = 0
    blueMax = 0
    gameID = line[5:line.find(":")]
    for subset in line[line.find(":")+1:].split(";"):
        for colour in subset.split(","):
            if red in colour:
                redMax = max([redMax,int(colour[1:0-(len(red)+1)])])
            if green in colour:
                greenMax = max([greenMax,int(colour[1:0-(len(green)+1)])])
            if blue in colour:
                blueMax = max([blueMax,int(colour[1:0-(len(blue)+1)])])
    power = redMax * greenMax * blueMax
    powers.append(power)

total = 0
for power in powers:
    total += int(power)
print(total)
                
