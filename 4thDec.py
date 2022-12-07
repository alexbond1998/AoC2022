input = open('4thDecInput.txt').read().split('\n')
sum = 0

for i in range(len(input)):
    sections = input[i].split(',')
    firstelf = sections[0].split('-')
    secondelf = sections[1].split('-')

    #If first section set encapsulates second set
    if(int(firstelf[0]) <= int(secondelf[0]) and int(firstelf[1]) >= int(secondelf[1])):
        sum = sum + 1
    #If second section set encapsulates first set
    elif(int(secondelf[0]) <= int(firstelf[0]) and int(secondelf[1]) >= int(firstelf[1])):
        sum = sum + 1

print(sum)

    
