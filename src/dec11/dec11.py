'''Advent Of Code 2023 - Day 11'''

import sys

fname = 'dec11.data'
if len(sys.argv) > 1:
    fname = sys.argv[1]

print("Hello Advent Of Code 2023 - December 11")
print("Cosmic Expansion parts 1 and 2 - ", fname)

def expansion(o, s, t):
    res = 0
    remin = min(s,t)
    odist = abs(s-t)
    if odist > 1:
        for off in range(odist-1):
            if 0 == o[remin+1+off]:
                res += 1
    #print("expansion()", o, s, t, ":", res)
    return res

# main
datafile = open(fname, 'r')
lines = datafile.readlines()

rows = [0 for r in range(len(lines))]
cols = [0 for c in range(len(lines[0]))]
stars = []

result = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        # count stars per row and col for expansion 
        # remember star positions for calculation
        if '#' == lines[row][col]:
            rows[row] += 1
            cols[col] += 1
            stars.append( [row,col] )
            
#print("rows", rows)
#print("cols", cols)
#print("stars", stars)

result1 = 0
result2 = 0
# expansion ratio
# part 1: 1
# part 2: 1000000
for star in range(len(stars)):
    for stgt in range(len(stars)-star-1):
        tgt = star+stgt+1
        #print("stars", stars[star], stars[tgt])
        dist = abs(stars[star][0]-stars[tgt][0]) \
             + abs(stars[star][1]-stars[tgt][1]) 
        exp = expansion(rows,stars[star][0],stars[tgt][0]) \
            + expansion(cols,stars[star][1],stars[tgt][1])
        result1 += (dist+exp)
        result2 += (dist+999999*exp)

print("Puzzle result: part 1", result1)
print("Puzzle result: part 2", result2)
