import re

input = open('5thDecInput.txt').read().split('\n')

stackarray = [[], [], [], [], [], [], [], [], []]

for i in range(8):
    a = [(m.start()) for m in re.finditer(r"\[[A-Z]\]", input[i])]
    for j in range(len(a)):
        stack_num = int((a[j]/4))
        stackarray[stack_num].insert(0, input[i][a[j]+1])

for i in range(10, len(input)):
    values = re.findall(r"[0-9]+", input[i])
    cratestack = []
    for j in range(int(values[0])):
        crate = stackarray[int(values[1]) - 1].pop()
        cratestack.insert(0, crate)
        
    stackarray[int(values[2]) - 1] = stackarray[int(values[2]) - 1] + cratestack

for i in range(len(stackarray)):
    print("Stack: " + str(i + 1) + " Top Crate: " + stackarray[i][-1])




