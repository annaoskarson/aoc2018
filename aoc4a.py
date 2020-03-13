fil = open('4a-input.txt', 'r')
lista = list(fil)

#lista=['[1518-11-01 00:00] Guard #10 begins shift\n',
#'[1518-11-01 00:05] falls asleep\n',
#'[1518-11-01 00:25] wakes up\n',
#'[1518-11-01 00:30] falls asleep\n',
#'[1518-11-01 00:55] wakes up\n',
#'[1518-11-01 23:58] Guard #99 begins shift\n',
#'[1518-11-02 00:40] falls asleep\n',
#'[1518-11-02 00:50] wakes up\n',
#'[1518-11-03 00:05] Guard #10 begins shift\n',
#'[1518-11-03 00:24] falls asleep\n',
#'[1518-11-03 00:29] wakes up\n',
#'[1518-11-04 00:02] Guard #99 begins shift\n',
#'[1518-11-04 00:36] falls asleep\n',
#'[1518-11-04 00:46] wakes up\n',
#'[1518-11-05 00:03] Guard #99 begins shift\n',
#'[1518-11-05 00:45] falls asleep\n',
#'[1518-11-05 00:55] wakes up\n']

lista.sort()

#print(lista)

sovlist = []

for x in lista:
    date = x.split()[0][1:]
    time = x.split()[1][:-1]
    text = x.split("]")[1][1:]
#    print("datum:", date)
#    print("tid:", time)
#    print("text:", text)

#    print(text)
    if text[:5] == 'Guard':
        guardno = text.split()[1][1:]
    if text.split()[0] == 'falls':
        somna = time
        print(somna)
    if text.split()[0] == 'wakes':
        vakna = time
        tid = 60*(int(vakna.split(":")[0])-int(somna.split(":")[0])) + int(vakna.split(":")[1])-int(somna.split(":")[1])
#        print("sovtid:", tid)
        sovlist = sovlist + [(guardno, somna, vakna, tid)] 
#        print(guardno, somna, vakna, tid)    

#Make to time stamps ...

sumlist = []

for i in range(len(sovlist)):
    g = sovlist[i][0]
    sov = sovlist[i][3]
#    print(g, sov)
    found = False
    for j in range(len(sumlist)):
        if sumlist[j][0] == g:
            found = True
            sumlist[j][1] = sumlist[j][1] + sov
    if not(found):
        sumlist.append([g, sov])

#print(sumlist)        

def sortSecond(val): 
    return val[1]

sumlist.sort(key = sortSecond, reverse=True)
print(sumlist[0])
guy = sumlist[0][0]

def findminute(a):
    
    return 3


common_minute = findminute(guy)
print(common_minute)

#print(lista)

