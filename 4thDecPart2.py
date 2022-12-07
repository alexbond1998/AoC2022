input = open('Dec4thInput.txt').read().split('\n')
sum = 0

for i in range(len(input)):
    sections = input[i].split(',')
    firstelf = sections[0].split('-')
    secondelf = sections[1].split('-')

    #Lazy approach: Makes array list of all sections within first and second sets of bounds
    firstelfsections = range(int(firstelf[0]), int(firstelf[1])+1)
    secondelfsections = range(int(secondelf[0]), int(secondelf[1])+1)

    #Loop through first section set, if any section in the first set is within the second set, an overlap has occurred
    for j in range(len(firstelfsections)):
        if firstelfsections[j] in secondelfsections:
            sum = sum + 1
            break
        

print(sum)

    
