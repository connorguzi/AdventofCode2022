# 1 point for Rock, 2 paper, 3 scissors
# 0 for loss, 2 for paper, 3 for scissors
#
f = open("day2.txt", "r")

# PART 1

score = 0
for x in f:
    if(x[2] == 'X'):
        score+=1
        if(x[0] == 'A'):
            score+=3
        elif((x[0] == 'C')):
            score+=6

    elif(x[2] == 'Y'):
        score+=2
        if(x[0] == 'B'):
            score+=3
        elif((x[0] == 'A')):
            score+=6
    elif(x[2] == 'Z'):
        if(x[0] == 'C'):
            score+=3
        elif((x[0] == 'B')):
            score+=6
        score+=3

print(f'Part 1: {score}')

# PART 2
score = 0
f.seek(0)
for x in f:
    if(x[2] == 'X'):
        if(x[0] == 'A'):
            score+=3
        elif((x[0] == 'B')):
            score+=1
        else:
            score+= 2

    elif(x[2] == 'Y'):
        score+=3
        if(x[0] == 'A'):
            score+=1
        elif((x[0] == 'B')):
            score+=2
        else:
            score+= 3

    elif(x[2] == 'Z'):
        score+=6
        if(x[0] == 'A'):
            score+=2
        elif((x[0] == 'B')):
            score+=3
        else:
            score+= 1
        
print(f'Part 2: {score}')