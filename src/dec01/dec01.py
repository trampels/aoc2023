'''Advent Of Code 2023 - Day 01'''

print("Hello Advent Of Code 2023 - December 01")

print("trebuchet?! - dec01.data")

# string processing, get each the first and last digit
# build line value as first * 10 + last
# sum of all values

def string_value(s):
    value = 0
    first = -1
    last = -1

    for c in s:
        if   '0' == c: value = 0;
        elif '1' == c: value = 1
        elif '2' == c: value = 2
        elif '3' == c: value = 3
        elif '4' == c: value = 4
        elif '5' == c: value = 5
        elif '6' == c: value = 6
        elif '7' == c: value = 7
        elif '8' == c: value = 8
        elif '9' == c: value = 9
        else : value = -1
        if -1 < value:
          if -1 == first : first = value
          last = value
        #print("{} => {} , f {}, l {}".format(c, value, first, last))

    value = 10 * first + last
    #print("string_value({}) {} {} => {} ".format(s, first, last, value))
    return value

result = 0
count = 0

datafile = open('dec01.data', 'r')
lines = datafile.readlines()

# Strips the newline character
for line in lines:
    value = string_value(line.strip())
    result += value
    #count += 1
    #print("Line{}: {} = {} => {} ".format(count,
    #       line.strip(), value, result))

print("Puzzle result: {}".format(result))
