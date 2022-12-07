input = open('3rdDecInput.txt').read().split('\n')

Alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
            'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

sum = 0

for i in range(0, len(input), 3):
    #print(i)
    elf1 = {}
    elf2 = {}
    #halfpoint = round(len(input[i])/2)

    elf1_container = input[i]
    elf2_container = input[i+1]
    elf3_container = input[i+2]
    
    for j in range(len(elf1_container)):
        elf1.update({elf1_container[j]: elf1.get(elf1_container[j], 0) + 1})
        
    for j in range(len(elf2_container)):
        elf2.update({elf2_container[j]: elf2.get(elf2_container[j], 0) + 1})
    
    for j in range(len(elf3_container)):
        if(elf1.get(elf3_container[j], None ) is not None and elf2.get(elf3_container[j], None ) is not None ):
            sum = sum + Alphabet.get(elf3_container[j])
            #print(elf3_container[j] + ' Sum: ' + str(sum))
            break

print(sum)


