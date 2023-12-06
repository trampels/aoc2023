'''Advent Of Code 2023 - Day 06'''

print("Hello Advent Of Code 2023 - December 06 - part 2")

# input
time = [53837288]
dist = [333163512891532]

#sample
stime = [71530]
sdist = [940200]

print("times ", time)
print("distances ", dist)

race=0
result=1
for t in time:
    rg = [i for i in range(t)]
    rec = 0
    for i in rg:
        d = (t-i)*i
        #print("dist {} <=> load for {}s: {}".format(dist[race], i, d))  
        if d > dist[race]:
            rec += 1
    print("race {}: {} races longer {}".format(race, rec, dist[race]))
    result *= rec
    race += 1

print("Puzzle result: ", result)
