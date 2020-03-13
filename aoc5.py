fil = open('5-input.txt', 'r')
indata = fil.read()
indata = indata.replace('\n', '')
fil.close()

#code = 'dabAcCaCBAcCcaDA'

def shorten(kod):
    i = 0
    while i+1 < len(kod):
        [a,b] = kod[i:i+2]
        if a.lower() == b.lower() and (a.islower() != b.islower()):
            kod = kod[:i] + kod[i+2:]
            if i != 0:
                i = i - 1
        else:
            i = i + 1
    return(kod)

def partone(code):
    print("Advent of code 2018, day 5, part 1")
    kort = shorten(code)
    print(len(kort))

def parttwo(code):
    print("Advent of code 2018, day 5, part 2")
    res = []
    for x in 'abcdefghijklmnopqrstuvwxyz':
        newcode = code.replace(x, '').replace(x.upper(), '')
        kort = shorten(newcode)
        res = res + [len(kort)]
    print(min(res))        

partone(indata)
parttwo(indata)
