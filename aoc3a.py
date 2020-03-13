fil = open('3a-input.txt', 'r')

claims = list(fil)

#claims =['#1 @ 1,3: 4x4\n', '#2 @ 3,1: 4x4\n', '#3 @ 5,5: 2x2\n']

#print(claims)

fabric = []


def findpatch(a,b):
    if len(fabric) == 0:
#        print("tomt tyg")
        return -1
    for apa in fabric:
#        print("tyget:", fabric)
#        print("x-koord",apa[0], "y-koord", apa[1])
#        print(apa, a, b)
        if apa[0] == a and apa[1] == b:
#            print("finns på tyg:", "(", a, ",", b, ")")
            return fabric.index(apa)
        
#    print("finns inte på tyg")
    return -1    

for i in claims:
    claim = i.split()
    idnum = claim[0]
#    print(len(fabric), idnum, "of", len(claims))
#    print(fabric)
#    print(idnum, "of", len(claims), "fabric size", len(fabric))
    x = int(claim[2].split(",")[0])
    y = int(claim[2].split(",")[1].split(":")[0])
    width = claim[3].split("x")[0]
    height = claim[3].split("x")[1]
#    print(claim)
#    print("x, y, width, height", x,y, width, height)
    for j in range(int(width)):
#        print(j, width)
        for k in range(int(height)):
#            print(x,y,j,k)
            jx = x+j
            ky = y+k
#            print("koord:", jx, ky)
            patch = findpatch(jx,ky)
            if patch < 0:
                fabric = fabric + [(jx, ky, 1)]
            else:
                antal = fabric[patch][2]
#                print("X")
#                print("antal:", antal)
                fabric[patch] = (jx, ky, antal + 1)
    print(idnum)

svar = 0
for x in fabric:
    if x[2] > 1:
        svar = svar + 1
print("svaret är:", svar)
#        print(len(fabric))
#print(fabric)
                
#            fabric = fabric + [(jx, ky, antal)]
