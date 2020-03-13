fil = open('3a-input.txt', 'r')
claims = list(fil)

#claims =['#1 @ 1,3: 4x4\n', '#2 @ 3,1: 4x4\n', '#3 @ 5,5: 2x2\n']
#print(claims)

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
#print("storlek:", x,y)
fabric = [[0 for i in range(2*x)] for i in range(2*y)]
#print(fabric)

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
#            print("j,k",j, k)
            jx = x+j
            ky = y+k
#            print("x, y", jx, ky)
            antal = fabric[ky][jx]
            fabric[ky][jx] = antal + 1

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
        print(idnum)
        
