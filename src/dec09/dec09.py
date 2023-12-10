'''Advent Of Code 2023 - Day 09'''

import sys

fname = 'dec09.data'
if len(sys.argv) > 1:
    fname = sys.argv[1]

print("Hello Advent Of Code 2023 - December 09")
print("Mirage Maintenance parts 1 and 2 - ", fname)

def prognose(data):
    pnext = data[-1]
    values = [ data ]
    #print("prognose() ", data)
    zerodiff = False
    while not zerodiff:
        zerodiff = True
        data = values[-1]
        diffs = []
        for i in range(len(data)-1):
            d = data[i+1] - data[i]
            diffs.append(d)
            if not d==0:
                zerodiff = False
        pnext += diffs[-1]
        #print("diffs ", diffs, zerodiff, pnext)
        values.append(diffs)
    pprev = 0
    for i in reversed(range(len(values)-1)):
        pprev = values[i][0] - pprev

    return [pprev, pnext]

# main
datafile = open(fname, 'r')
lines = datafile.readlines()

# read turn on nodes
result = 0
history = 0

for line in lines:
    px = prognose(list(map(int, line.strip().split())))
    history += px[0]
    result += px[1]

print("Puzzle result: ", result, "history:", history)
