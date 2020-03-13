fil = open('2a-input.txt', 'r')

boxes = list(fil)

res = ""

for x in (boxes):
    for y in (boxes):
        res = ""
        for i in range(len(y)):
            if x[i] == y[i]:
                res = res + x[i]
        if len(res) + 1 == len(y):
            print(res)

