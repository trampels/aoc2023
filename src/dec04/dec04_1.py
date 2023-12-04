'''Advent Of Code 2023 - Day 4'''

print("Hello Advent Of Code 2023 - December 04")

print("scratch cards - dec04.data")

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# card: winning numbers | scratch numbers
# 2^winning cards(>0)
def card_points(s):
    result = 0

    card  = s.split(':')
    numbers = card[1].split('|');
    wn = []
    for item in numbers[0].split(' '):
        if item.isdigit():
            wn.append(int(item))
    sn = []
    for item in numbers[1].split(' '):
        if item.isdigit():
            sn.append(int(item))
    #print("{}: {} | {}".format(card[0],wn,sn))
    for w in wn:
        for s in sn:
            if w == s:
                if result == 0:
                    result = 1
                else:
                    result *=2
    
    #print("res {}: {} | {}".format(result,wn,sn))
    return result


if __name__ == "__main__":
    result = 0

    datafile = open('dec04.data', 'r')
    lines = datafile.readlines()

    for line in lines:
        result += card_points(line.strip())        

print("Puzzle result: {}".format(result))
