'''Advent Of Code 2023 - Day 03'''

print("Hello Advent Of Code 2023 - December 03")

print("Gear Ratios - dec03.data")

# string processing, find index of all symbols (not (digit or dot)
# for each line
def symbol_indexes(s):
    pos = 0
    idx = []
    for c in s:
        if not '.' == c:
            if not c.isdigit():
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
def valid_value(n,v,p,idx):
    pmin = p-1
    pmax = p+len(str(v))
    
    if 0 < n:
        symtab = idx[n-1]
        for sym in symtab:
            if pmin <= sym and sym <= pmax:
                return True
    symtab = idx[n]
    for sym in symtab:
        if pmin <= sym and sym <= pmax:
            return True
    if n < len(idx)-1:
        symtab = idx[n+1]
        for sym in symtab:
            if pmin <= sym and sym <= pmax:
                return True
    return False
    
# resolve all numbers and validate these against symbols
def sum_line_numbers(n, s, idx):
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
                if valid_value(n,value,vpos,idx):
                    an = { "number": value, "row": n, "col": vpos }
                    print("active number: {}".format(an))
                    result += value
                value = 0
        pos += 1

    if 0 < value:
        if valid_value(n,value,vpos,idx):
            an = { "number": value, "row": n, "col": vpos }
            print("active number: {}".format(an))
            result += value

    return result
    
result = 0
symbol_map = []

def process_input():
    count = 0
    sum = 0
    datafile = open('dec03.data', 'r')
    lines = datafile.readlines()

    # 1st read - collect all symbols
    for line in lines:
        indexes = symbol_indexes(line.strip())
        symbol_map.append(indexes)
        count += 1

    # 2nd read - resolve all numbers attached to a symbol
    count = 0
    lastline = ''
    for line in lines:
        value = sum_line_numbers(count, line, symbol_map)
        sum += value
        count += 1

    return sum

result = process_input()

print("Puzzle result: {}".format(result))
