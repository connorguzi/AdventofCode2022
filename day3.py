def CtoN(char):
    if(ord(char) >= 65 and ord(char) <= 90):
        return ord(char) - 38
    else:
        return ord(char) - 96


## PART 1

priority = 0
f = open('day3.txt', 'r')
for line in f:
    firstHalfChars = []
    firstHalf = line[0 : int ((len(line)) / 2)]
    secondHalf = line[int ((len(line)) / 2) : ]
    for char in firstHalf:
        if char in secondHalf:
            priority += CtoN(char)
            break
            
print("Part 1 Answer: ", priority)


## PART 2

f.seek(0)

lines = f.readlines()


priority = 0
i =0 
while i  < len(lines):
    elf1 = lines[i]
    elf2 = lines[i + 1]
    elf3 = lines[i + 2]
    for char in elf1:
        if char in elf2 and char in elf3 and ord(char) != 10:
            priority += CtoN(char)
            break
    i+=3

print("Part 2 Answer: ", priority)