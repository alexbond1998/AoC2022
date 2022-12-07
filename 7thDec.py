class Node:
    def __init__(self, name, size, filetype, parent):
        self.children = []
        self.name = name
        self.size = size
        self.filetype = filetype
        self.parent = parent

def Traverse(treenode, directory):

    if(directory == '..'):
        return treenode.parent
    else:
        for i in range(len(treenode.children)):
            if(treenode.children[i].name == directory):
                return treenode.children[i]
        
        print("No child found.. wtf?")
        exit()

def loadFileSystem(input):
    root = Node("/", 0,"dir", None)

    input = open('7thDecInput.txt').read().split('\n')

    currentNode = root

    for i in range(1, len(input)):
        cmd = input[i].split(' ')
        if(cmd[0] == '$'):
            if(cmd[1] == "cd"):
                currentNode = Traverse(currentNode, cmd[2])
                continue
            else:
                continue

        elif(cmd[0] == "dir"):
            currentNode.children.append(Node(cmd[1], 0, "dir", currentNode))
        else:
            currentNode.children.append(Node(cmd[1], int(cmd[0]), "file", currentNode))
    
    return root

def UpdateSizes(itr, dir_sizes): #Post-Order Traversal
    if(itr == None):
        return dir_sizes

    for i in range(len(itr.children)):
        dir_sizes = UpdateSizes(itr.children[i], dir_sizes)
    
    size = 0

    for i in range(len(itr.children)):
        size = size + itr.children[i].size

    if(itr.filetype == 'dir'):
        itr.size = size
        
        if(size <= 100000):
            dir_sizes.append(size)    
    

    return dir_sizes

def FindSmallestRequiredDirectory(itr, dir_sizes, minimum_size): #Pre-Order Traversal
    if(itr == None):
        return dir_sizes

    if(itr.filetype == 'dir' and itr.size >= minimum_size):
        dir_sizes.append(itr.size)
    
    # Loop for printing t a value of character
    for i in range(len(itr.children)):
        dir_sizes = FindSmallestRequiredDirectory(itr.children[i], dir_sizes, minimum_size)

    return dir_sizes   



storage_size = 70000000
filesystem_min = 30000000    

root = loadFileSystem(input)


#Part 1
sums = []
sums = UpdateSizes(root, sums)
sorted_sums = sorted(sums)
print("Part 1 Solution: " + str(sum(sorted_sums)))


#Part 2
space_required = filesystem_min - (storage_size - root.size)

minimumSizes = []
minimumSizes = FindSmallestRequiredDirectory(root, minimumSizes, space_required)
minimumSizes = sorted(minimumSizes)
print("Part 2 Solution: " + str(minimumSizes[0]))
 






    
    

    


