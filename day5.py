## PART 1 ##

f = open('day5.txt', 'r')
## letter is (col * 4) - 3
colvals = [[] for x in range(9)]
x = f.readlines()
row = 0

# Getting the initial state of the columns
while x[row][1].isnumeric() == False:
    for col in range(1, 10):
        if x[row][(col*4) - 3] != ' ':
            colvals[col-1].append(x[row][(col*4) - 3])
    row+=1
# Reversing to make popping and appending easier
for vals in colvals:
    vals.reverse()

row = 10
# Looping through and carrying out the instructions
while row <= 514:
    moveAmount = int(x[row].split()[1])
    startCol = int(x[row].split()[3]) - 1
    endCol = int(x[row].split()[5]) - 1
    for i in range(moveAmount):
        colvals[endCol].append(colvals[startCol].pop())
        # print(i)
    row+=1

answer = ''
for i in range(1, 10):
    answer+=colvals[i-1][-1]
print("Part 1: ", answer)

## PART 2 ##
row = 0
colvals = [[] for x in range(9)]

while x[row][1].isnumeric() == False:
    for col in range(1, 10):
        if x[row][(col*4) - 3] != ' ':
            colvals[col-1].append(x[row][(col*4) - 3])
    row+=1

for vals in colvals:
    vals.reverse()

row = 10

while row <= 514:
    moveAmount = int(x[row].split()[1])
    startCol = int(x[row].split()[3]) - 1
    endCol = int(x[row].split()[5]) - 1
    for i in range(moveAmount):
        colvals[endCol].append(colvals[startCol].pop(len(colvals[startCol]) - (moveAmount - (i))))
        # print(i)
    row+=1

answer = ''
for i in range(1, 10):
    answer+=colvals[i-1][-1]

print("Part 2: ", answer)

