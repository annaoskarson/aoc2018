fil = open('1a-input.txt', 'r')

digits = list(fil)
a = 0
result = []
done = False

while done != True:
    for x in (digits):
        a = a + int(x)
        if a in result:
            done = True
            print(a)
            break
        result.append(a)
