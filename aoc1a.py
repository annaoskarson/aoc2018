fil = open('1a-input.txt', 'r')

digits = list(fil)
a = 0

for x in (digits):
    a = a + int(x)

print(a)
