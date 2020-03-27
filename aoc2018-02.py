fil = open('aoc2018-02-input.txt', 'r')

boxes = list(fil)

def partone():
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
    print('Part one:', two, "*", three, "=", two * three)

def parttwo():
    res = ""

    for x in (boxes):
        for y in (boxes):
            res = ""
            for i in range(len(y)):
                if x[i] == y[i]:
                    res = res + x[i]
            if len(res) + 1 == len(y):
                print('Part two:', res)
                break

partone()
parttwo()