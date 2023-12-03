dayNo = 1
with open(f"Inputs\\Day{str(dayNo)}.txt","r") as file:
    fileContents = file.read()

digits = [("zero",0),
          ("one",1),
          ("two",2),
          ("three",3),
          ("four",4),
          ("five",5),
          ("six",6),
          ("seven",7),
          ("eight",8),
          ("nine",9)]

lines = fileContents.split("\n")
calibrationVals = []

for line in lines:
    value = ""
    places = {}
    for digit in digits:
        for form in digit:
            if str(form) in line:
                places[line.find(str(form))] = digit[1]
    value += str(places[min(place for place in places)])

    places = {}
    for digit in digits:
        for form in digit:
            if str(form) in line:
                places[line.rfind(str(form))] = digit[1]
    value += str(places[max(place for place in places)])
    
    calibrationVals.append(value)

total = 0
for value in calibrationVals:
    total += int(value)
print(total)
    
    
