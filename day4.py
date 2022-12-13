
## PART 1
f = open('day4.txt', 'r')
count = 0
for x in f:
    range1,range2 = x.split(',')
    
    low1, high1 = range1.split('-')
    low2, high2 = range2.split('-')
    low1 = int(low1)
    low2 = int(low2)
    high1 = int(high1)
    high2 = int(high2)

    if(low1 >= low2 and high1 <= high2):
        count+=1

    elif ((low1 <= low2 and high1 >= high2)):
        count+=1

print("Part1: ", count)


## PART 2

f.seek(0)
count = 0

for x in f:
    range1,range2 = x.split(',')
    
    low1, high1 = range1.split('-')
    low2, high2 = range2.split('-')
    low1 = int(low1)
    low2 = int(low2)
    high1 = int(high1)
    high2 = int(high2)

    if(low1 >= low2 and low1 <= high2):
        count+=1

    elif ((high1 >= low2 and high1 <= high2)):
        count+=1

    elif ((low2 >= low1 and low2 <= high1)):
        count+=1
    elif ((high2 >= low1 and high2 <= high1)):
        count+=1

print("Part2: ", count)
