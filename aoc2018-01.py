fil = open('aoc2018-01-input.txt', 'r')

digits = list(fil)

def partone():
	a = 0
	for x in (digits):
	    a = a + int(x)
	print('Part one:', a)

def parttwo():
	a = 0
	result = []
	done = False

	while done != True:
	    for x in (digits):
	        a = a + int(x)
	        if a in result:
	            done = True
	            print('Part two:', a)
	            break
	        result.append(a)

partone()
parttwo()