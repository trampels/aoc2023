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
                result += 1
    
    #print("{}: {}".format(card[0],result))
    return result


if __name__ == "__main__":
    result = 0
    count = 0

    datafile = open('dec04.data', 'r')
    lines = datafile.readlines()

    wins = {}
    cards = {}
    for line in lines:
        wins.update({str(count): card_points(line.strip()) })        
        # initially each card once
        cards.update({str(count): 1})
        count += 1
    #print(wins)

    for key, value in wins.items():
        # run len of additional cards, prevent overrun
        run = value
        if int(key)+run > len(cards)-1:
            run = len(cards)-int(key)-1
        # increment is number of cards
        inc = cards[str(key)]
        for i in range(1, run+1):
            idx = str(int(key)+i)
            val = inc + cards[str(idx)]
            cards.update({str(idx): val})   
            #print("update", idx, " to ", val)

    for key, value in cards.items():
        #print("cards ", key, " value ", value)
        result += value

    print("Puzzle result: {}".format(result))
