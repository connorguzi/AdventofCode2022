## PART 1 ##

def DuplicateCheck(list):
    for elem in list:
        if list.count(elem) > 1:
            return True
    return False


f = open('day6.txt', 'r')
characters = []
data = f.readline()
count = 0
for char in data:
    count += 1
    if len(characters) < 4:
        characters.append(char)

    else:
        characters.pop(0)
        characters.append(char)
        if DuplicateCheck(characters):
            pass
        else:
            break
print(count)


count = 0
for char in data:
    count += 1
    if len(characters) < 14:
        characters.append(char)

    else:
        characters.pop(0)
        characters.append(char)
        if DuplicateCheck(characters):
            pass
        else:
            break
print(count)
