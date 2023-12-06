'''Advent Of Code 2023 - Day 06'''

print("Hello Advent Of Code 2023 - December 06")

# input
time = [53, 83, 72, 88]
dist = [333, 1635, 1289, 1532]

#sample input
stime = [7,15,30]
sdist = [9,40,200]

print("time ", time)
print("distances ", dist)

race=0
result=1
for t in time:
    rg = [i for i in range(t)]
    rec = 0
    for i in rg:
        if (t-i)*i > dist[race]:
            rec += 1
    print("race {}: {} races longer {}".format(race, rec, dist[race]))
    result *= rec
    race += 1

print("Puzzle result: ", result)
