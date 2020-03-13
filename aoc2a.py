fil = open('2a-input.txt', 'r')

boxes = list(fil)
two = 0
three = 0

def countiftwo(box):
    for a in box:
        count = box.count(a)
        if count == 2:
            return 1
    return 0

def countifthree(box):
    for b in box:
        count = box.count(b)
        if count == 3:
            return 1
    return 0


for x in (boxes):
    two = two + countiftwo(x)
    three = three + countifthree(x)

print(two, "*", three, "=", two * three)
