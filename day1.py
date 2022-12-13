f = open("day1.txt", "r")
cals = []
temp = []
for x in f:
    if(x.strip()):
        temp.append(int(x))
    else:
        cals.append(sum(temp))
        temp = []

print(max(cals))
first = max(cals)
cals.pop(cals.index(max(cals)))

second = max(cals)
print(max(cals))


cals.pop(cals.index(max(cals)))
third = max(cals)
print(max(cals))

print(first + second + third)