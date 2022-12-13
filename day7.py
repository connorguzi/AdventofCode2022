totalscore = 0
closest = 30000000
totalspace = 0
class File:
    def __init__(self, size=0, name=None):
        self.name = name
        self.size = size

class Directory:

    def __init__ (self, parent=None, name=None):
        self.size = 0
        self.children = []
        self.files = []
        self.parent = parent
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __str__(self, level=0):
        ret = '|' + "-"*level+self.name+":\n"
        for file in self.files:
            ret += ('|' + ' ' * (level + 2)) +'File ' + file.name + ': ' + str(file.size)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def AddDir(self, name=None):
        NewDir = Directory(parent=self, name=name)
        self.children.append(NewDir)
        return NewDir
        
    def AddFile(self, size=0, name=None):
        global totalspace
        self.size+= size
        totalspace += size
        NewFile = File(size=size, name=name)
        self.files.append(NewFile)

    ## ONLY USE ONCE ##
    def CalcSize(self):
        global totalscore
        if self.children:
            for child in self.children:
                self.size += child.CalcSize()
        if self.size <= 100000:
            totalscore += self.size
        return self.size

    def FindHead(self):
        head = self
        while head.parent:
            head = head.parent
        return head
    
    def GetNode(self, name):
        correctchild = None
        if self.name == name:
            return self
        for child in self.children:
            if child.name == name:
                return child
            else:
                correctchild = child.GetNode(name)
        return correctchild

    def CD(self, name):

        for child in self.children:
            if child.name == name:
                return child
        if self.name == name:
            return self
    def ChildExists(self, name):
        for child in self.children:
            if child.name == name:
                return True
        return False 

    def FileExists(self, name):  
        for file in self.files:
            if file.name == name:
                return True
        return False

    def FindClosest(self, size):
        closest = self
        for child in self.children:
            if(child.FindClosest(child.size).size < closest.size and child.FindClosest(child.size).size >= 2677139):
                closest = child.FindClosest(child.size)

        return closest

root = Directory(name='/')
current = root

f = open('day7.txt', 'r')

for x in f:
    words = x.split()

    if(words[1] == 'cd'):
        if(words[2] == '..'):
            current = current.parent
        else:
            current = current.CD(words[2])
    elif(words[0] == 'dir'):
        if current.ChildExists(words[1]):
            pass
        else:
            current.AddDir(words[1])
    elif(words[0].isnumeric()):
        if current.FileExists(words[1]):
            pass
        else:
            current.AddFile(int(words[0]),words[1])

# print(root)
    
root.CalcSize()  

print('Part1: ' + str(totalscore))

##Needed space:
2677139

print('Part2: ' + str(root.FindClosest(root.size).size))



















# current = root.AddDir(name='a')
# current.AddFile(10, '123')
# current = root.AddDir(name='b')
# current.AddFile(20, '456')
# current = current.AddDir(name='c')
# current.AddFile(50, '789')
# # print(current.name)
# current = root

# # current.PrintDir()
# # print(current.CalcSize())
# # print(root)

# current = root.GetNode('c')
# current.AddFile(60, 'bruh')

# # print(root)

# current = root.GetNode('b')
# current = current.AddDir(name='b')
# current.AddFile(1000, 'shid')
# current = current.AddDir(name = 'e')
# current.AddFile(300, 'nad')


# # print(root.CalcSize())
# print(root)
