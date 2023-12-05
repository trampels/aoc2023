'''Advent Of Code 2023 - Day 05'''

# resmap list of lists of integers
# dest, src, range
class ResMap:
    def __init__(self, name):
        self.name = name
        self.dsm = []
        
    # dest, src, range
    # mapped: 52 50 48 (50-98 => 52-100) - 79=>79(+52-50): 81
    # not mapped, use val: 14 => 14
    def dest(self, val):
        for entry in self.dsm:
            if entry[1] <= val and val < entry[1] + entry[2]:
                return val + entry[0] - entry[1]
        return val

datafile = open('dec05.data', 'r')
lines = datafile.readlines()

seeds = []
sts = ResMap('seed-to-soil')
stf = ResMap('soil-to-fertilizer')
ftw = ResMap('fertilizer-to-water')
wtl = ResMap('water-to-light')
ltt = ResMap('light-to-temperature')
tth = ResMap('temperature-to-humidity')
htl = ResMap('humidity-to-location')

context = ''
count = 0
for line in lines:
    #print("line ", count, ": ", line)
    if 0 == count:
        seeds = list(map(int, line.strip().split(':')[1].split()))
        #print("seeds: ", seeds)
    elif line.strip().endswith("map:"):
        context = line.split(' ')[0]
        #print("context: ", context)
    elif 0 < len(line.strip()) and 0 < len(context):
        entry = list(map(int, line.strip().split()))
        #print("context ", context, " seed ", seed)
        if context == 'seed-to-soil':
            sts.dsm.append(entry)
        elif context == 'soil-to-fertilizer':
            stf.dsm.append(entry)
        elif context == 'fertilizer-to-water':
            ftw.dsm.append(entry)
        elif context == 'water-to-light':
            wtl.dsm.append(entry)
        elif context == 'light-to-temperature':
            ltt.dsm.append(entry)
        elif context == 'temperature-to-humidity':
            tth.dsm.append(entry)
        elif context == 'humidity-to-location':
            htl.dsm.append(entry)
    count += 1

#print(sts.name, sts.dsm)
#print(stf.name, stf.dsm)
#print(ftw.name, ftw.dsm)
#print(wtl.name, wtl.dsm)
#print(ltt.name, ltt.dsm)
#print(tth.name, tth.dsm)
#print(htl.name, htl.dsm)

locmin = -1
for seed in seeds:
    soil = sts.dest(seed)
    fert = stf.dest(soil)
    wate = ftw.dest(fert)
    ligh = wtl.dest(wate)
    temp = ltt.dest(ligh)
    humi = tth.dest(temp)
    loca = htl.dest(humi)
    #print("mapped", [seed,soil,fert,wate,ligh,temp,humi,loca])
    if locmin == -1:
        locmin = loca
    elif locmin > loca:
        locmin = loca

print("Puzzle result (min location): ", locmin)


