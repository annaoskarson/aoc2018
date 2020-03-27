fil = open('aoc2018-03-input.txt', 'r')
claims = list(fil)

#claims =['#1 @ 1,3: 4x4\n', '#2 @ 3,1: 4x4\n', '#3 @ 5,5: 2x2\n']

fabric = [[]]

def size(indata):
    maxx = 0
    maxy = 0

    for i in claims:
        claim = i.split()
        idnum = claim[0]
        x = int(claim[2].split(",")[0])
        y = int(claim[2].split(",")[1].split(":")[0])
        width = int(claim[3].split("x")[0])
        height = int(claim[3].split("x")[1])
        if x+width > maxx:
            maxx = x+width
        if y+height > maxy:
            maxy = y+height
        return(maxx, maxy)

(x,y)=size(claims)
fabric = [[0 for i in range(2*x)] for i in range(2*y)]

antal = 0

for i in claims:
    claim = i.split()
    idnum = claim[0]
    x = int(claim[2].split(",")[0])
    y = int(claim[2].split(",")[1].split(":")[0])
    width = int(claim[3].split("x")[0])
    height = int(claim[3].split("x")[1])

    for j in range(int(width)):
        for k in range(int(height)):
            jx = x+j
            ky = y+k
            antal = fabric[ky][jx]
            fabric[ky][jx] = antal + 1

svar = 0
for x in fabric:
    for p in x:
        if p > 1:
            svar = svar + 1
print("Part one:", svar)   

def isOK(x,y,width,height):
    for j in range(int(width)):
        for k in range(int(height)):
            jx = x+j
            ky = k+y
            if fabric[ky][jx] != 1:
                return False
    return True

for i in claims:
    claim = i.split()
    idnum = claim[0]
    x = int(claim[2].split(",")[0])
    y = int(claim[2].split(",")[1].split(":")[0])
    width = int(claim[3].split("x")[0])
    height = int(claim[3].split("x")[1])
    if isOK(x,y,width,height):
        print('Part two:', idnum)

