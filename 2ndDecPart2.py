from enum import Enum

input = open('2ndDecInput.txt').read()
input = input.split('\n')

opponent = Enum('opponent', ['A', 'B', 'C'])
response = Enum('response', ['X', 'Y', 'Z'])

score = 0


for i in range(len(input)):
    player = input[i][2]
    opp = input[i][0]
    if( player == 'X'):
        score = score + (((opponent[opp].value + 4) % 3)+1)
    elif(player == 'Y'):
        score = score + 3 + opponent[opp].value
    else:
        score = score + 6 + (opponent[opp].value % 3 ) + 1

print(score)
    



#print(response['Z'].value)



