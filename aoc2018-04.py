from collections import Counter
from operator import itemgetter

with open('aoc2018-04-input.txt') as file:
    text = file.readlines()

#test=['[1518-11-01 00:00] Guard #10 begins shift\n','[1518-11-01 00:05] falls asleep\n','[1518-11-01 00:25] wakes up\n','[1518-11-01 00:30] falls asleep\n','[1518-11-01 00:55] wakes up\n','[1518-11-01 23:58] Guard #99 begins shift\n','[1518-11-02 00:40] falls asleep\n','[1518-11-02 00:50] wakes up\n','[1518-11-03 00:05] Guard #10 begins shift\n','[1518-11-03 00:24] falls asleep\n','[1518-11-03 00:29] wakes up\n','[1518-11-04 00:02] Guard #99 begins shift\n','[1518-11-04 00:36] falls asleep\n','[1518-11-04 00:46] wakes up\n''[1518-11-05 00:03] Guard #99 begins shift\n','[1518-11-05 00:45] falls asleep\n','[1518-11-05 00:55] wakes up\n']
#text = test

lista = [line.strip() for line in text]
lista.sort()

guards = {}

#Strategy 1: Find the guard that has the most minutes asleep.
#What minute does that guard spend asleep the most?
#What is the ID of the guard you chose multiplied by the minute you chose?

for x in lista:
    [date, time] = x.split(']',1)[0].strip('[').split(' ')
    sleeptime = 0
    if x.split(' ')[2] == 'Guard':
        guardno = x.split(' ')[3][1:]
        if int(time.split(':')[0]) != 0:
            wake = 0
        else:
            wake = int(time.split(':')[1])
        if (guardno not in guards):
            guards.update({guardno : []})
    else:
        text = ' '.join(x.split(' ',4)[-2:])
        if text == 'falls asleep':
            sleep = int(time.split(':')[1])
        elif text == 'wakes up':
            wake = int(time.split(':')[1])
            for t in range(sleep, wake):
                guards.update({guardno : guards[guardno] + [t]})

results = []
for g in guards:
    occurence_count = Counter(guards[g]) 
    num_minutes = len(guards[g])
    if len(guards[g]) > 0: [(minute, times)] = occurence_count.most_common(1)
    results = results + [(g, num_minutes, minute, times)]

(guard, numbers, minute, times) = max(results,key=itemgetter(1))
print('Part one:', minute*int(guard))

(guard, numbers, minute, times) = max(results,key=itemgetter(3))
print('Part two:', minute*int(guard))
