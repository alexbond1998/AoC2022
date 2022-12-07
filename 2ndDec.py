from enum import Enum

input = open('2ndDecInput.txt').read()
input = input.split('\n')

opponent = Enum('opponent', ['A', 'B', 'C'])
response = Enum('response', ['X', 'Y', 'Z'])
score = 0


for i in range(len(input)):

    opp = input[i][0]
    player = input[i][2]
    if( response[player].value == (opponent[opp].value % 3 ) + 1):
        score = score + 6 + response[player].value
    elif( response[player].value == opponent[opp].value ):
        score = score + 3 +  response[player].value
    else:
        score = score + response[player].value

print(score)
    



#print(response['Z'].value)



