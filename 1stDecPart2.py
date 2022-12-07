input = open('1stDecInput.txt').read()
input = input.split('\n')

top3 = [0,0,0]
currentCalories = 0

for i in range(len(input)):
    if input[i] == '':
        for j in range(3):
            if currentCalories > top3[j]:
                top3.insert(j, currentCalories)
                top3.pop(3)
                break
        currentCalories = 0
    else:
        currentCalories = currentCalories + int(input[i])

print("Sum: " + str(sum(top3)))

