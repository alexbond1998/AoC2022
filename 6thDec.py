input = open('6thDecInput.txt').read()

characters = {}
length = 0

windowsize = 14

def updatewindow(characterlist, start, end):
    characterlist.update({input[end]:characters.get(input[end], 0) + 1})

    if j > 0:                                                                   
        removeindex = start - 1                                                 
        characterlist[input[removeindex]] = characters[input[removeindex]] - 1  #Update character that is no longer in sliding window


for i in range(len(input)):
    j = i - (windowsize - 1)                                                    # windowsize - 1 to be include of the upper bound

    updatewindow(characters, j, i)

    if j >= 0:
        unique = True
        for k in range(j, i+1):
            if characters[input[k]] > 1:                                        #If character value is > 1 then there is more than 1 occurance of the character
                unique = False
                break
                
        if unique == True: 
            length = i
            break

print(length+1)                                                                 #Index starts at 0 so need to offset that
    
