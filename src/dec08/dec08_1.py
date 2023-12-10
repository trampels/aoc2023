'''Advent Of Code 2023 - Day 08'''

import sys

fname = 'dec08.data'
if len(sys.argv) > 1:
    fname = sys.argv[1]

print("Hello Advent Of Code 2023 - December 08")
print("Camel Cards part 1 - ", fname)

steps = ""
nodes = {}

def next_step(path, step):
    pos = path[-1]
    for node, to in nodes.items():
        if node == pos:
            #print(step, "next_step() from ",  node, "step ", steps[step], to)
            if steps[step] == 'L' :
                goto = to[0]
            else:
                goto = to[1]
            return goto
    return ""

datafile = open(fname, 'r')
lines = datafile.readlines()

path = ["AAA"]
steps = lines[0].strip()
for line in lines:
    move = line.strip().split('=')
    if 2 == len(move):
        where = move[0].strip()
        if 0 == len(path):
            path.append(where)
        targets = move[1].strip()
        nodes[where] = [targets[1]+targets[2]+targets[3],targets[6]+targets[7]+targets[8]]

print("steps ", steps, "len ", len(steps))
print("nodes ", len(nodes))
print("path ", path)

while len(path) < 100*len(nodes):
    goto = next_step(path, (len(path)-1)%len(steps))
    if goto == "ZZZ":
        print( "found way with ", len(path), " to ", goto )
        break;
    if 0 == len(goto):
        break;
    path.append(goto)
