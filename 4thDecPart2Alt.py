input = open('4thDecInput.txt').read().split('\n')
sum = 0

for i in range(len(input)):
    sections = input[i].split(',')
    firstelf = sections[0].split('-')
    secondelf = sections[1].split('-')

    #If first set's lower bound is inside the second set's bounds
    if(int(firstelf[0]) >= int(secondelf[0]) and int(firstelf[0]) <= int(secondelf[1])):
        sum = sum + 1
    #If first set's upper bound is inside the second set's bounds
    elif(int(firstelf[1]) >= int(secondelf[0]) and int(firstelf[1]) <= int(secondelf[1])):
        sum = sum + 1
    #If first set's bounds encapsulate the second set's bounds
    elif(int(firstelf[0]) <= int(secondelf[0]) and int(firstelf[1]) >= int(secondelf[1])):
        sum = sum + 1

print(sum)

    
