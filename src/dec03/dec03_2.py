'''Advent Of Code 2023 - Day 03'''

print("Hello Advent Of Code 2023 - December 03")

print("Gear Ratios - dec03.data")

# string processing, find index of all stars for each line,
# each star with exaclty 2 numbers attached is a gear
def star_indexes(s):
    pos = 0
    idx = []
    for c in s:
        if '*' == c:
            idx.append(pos)
        pos+=1
    #print("indexes: {}".format(idx))
    #for i in idx:
    #    print("{}: {}".format(i, s[i]))
    return idx

# value is valid when it attaches to a symbol
# within this, prev or next line, diag also
# .......+.............%
# .23.....456....-345...
# ...#........@.........
# number of line
# value (length matters)
# pos of value in line
# symbol index
#def valid_value(n,v,p,idx,an):
def valid_value(n,v,p,idx,ans):
    pmin = p-1
    pmax = p+len(str(v))
    
    if 0 < n:
        symtab = idx[n-1]
        for sym in symtab:
            if pmin <= sym and sym <= pmax:
                an = { "row": int(n-1), "col": int(sym), "number": v }
                #print("attached number: {}".format(an))
                ans.append(an)
                return ans
    symtab = idx[n]
    for sym in symtab:
        if pmin <= sym and sym <= pmax:
            an = { "row": int(n), "col": int(sym), "number": v }
            #print("attached number: {}".format(an))
            ans.append(an)
            return ans
    if n < len(idx)-1:
        symtab = idx[n+1]
        for sym in symtab:
            if pmin <= sym and sym <= pmax:
                an = { "row": int(n+1), "col": int(sym), "number": v }
                #print("attached number: {}".format(an))
                ans.append(an)
                return ans
    return ans
    
# resolve all numbers and validate these against symbols
def find_gear(n, s, idx, ans):
    pos = 0
    nd = False
    value = 0
    vpos = 0
    result = 0

    for c in s:
        if c.isdigit():
            if not nd:
                nd = True
                vpos = pos
                value = int(c)
            else:
                value *= 10
                value += int(c)
        else:
            nd = False
            if 0 < value:
                ans = valid_value(n,value,vpos,idx,ans)
                value = 0
        pos += 1

    if 0 < value:
        ans = valid_value(n,value,vpos,idx,ans)

    return ans
    
result = 0
star_map = []

def process_input():
    count = 0
    sum = 0
    ans = []
    datafile = open('dec03.data', 'r')
    lines = datafile.readlines()

    # 1st read - collect all stars
    for line in lines:
        indexes = star_indexes(line.strip())
        star_map.append(indexes)
        count += 1

    # 2nd resolve all star arrached values
    count = 0
    lastline = ''
    for line in lines:
        ans = find_gear(count, line, star_map, ans)
        count += 1

    # 3rd 
    # sum all multiplied pairs of star attached values
    keyrow = 0
    keycol = 0
    keycount = 0
    gearval = 0
    newans = sorted(ans, key=lambda an:(an['row'],an['col']))
    for an in newans:
        if not keyrow == an['row'] or not keycol == an['col']:
            if gearval > 0:
                print("gearval {} of {} values".format(gearval, keycount))
            if keycount == 2:
                sum += gearval
                print("gearval {} new sum {}".format(gearval, sum))
            keyrow = an['row']
            keycol = an['col']
            keycount = 1
            gearval = int(an['number'])
        else:
            keycount += 1
            gearval *= int(an['number'])
        print("attached number: {}".format(an))       
            
    if gearval > 0:
        print("gearval {} of {} values".format(gearval, keycount))
    if keycount == 2:
        sum += gearval
        print("gearval {} new sum {}".format(gearval, sum))
    return sum

result = process_input()

print("Puzzle result: {}".format(result))
