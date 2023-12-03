dayNo = 1
with open(f"Inputs\\Day{str(dayNo)}.txt","r") as file:
    fileContents = file.read()

digits = ["0","1","2","3","4","5","6","7","8","9"]

lines = fileContents.split("\n")
calibrationVals = []

for line in lines:
    value = ""
    for char in line:
        if char in digits:
            value += char
            break
    for char in line[::-1]:
        if char in digits:
            value += char
            break
    calibrationVals.append(int(value))

total = 0
for value in calibrationVals:
    total += value
print(total)
            
