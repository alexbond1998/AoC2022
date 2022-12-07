input = open('1stDecInput.txt').read()
input = input.split('\n')
print(input)

maxCalories = -1
#maxElf = 0
currentCalories = 0
#currentElf = 0


for i in range(len(input)):
    if input[i] == '':
        if currentCalories > maxCalories:
            maxCalories = currentCalories
        
        currentCalories = 0
    else:
        currentCalories = currentCalories + int(input[i])

print(maxCalories)

