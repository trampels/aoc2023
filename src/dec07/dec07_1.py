'''Advent Of Code 2023 - Day 07'''

print("Hello Advent Of Code 2023 - December 07")

# camel cards a poker alike game

# card => value
cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

# value => card
values = {
    14: "A",
    13: "K",
    12: "Q",
    11: "J",
    10: "T",
    9 : "9",
    8 : "8",
    7 : "7",
    6 : "6",
    5 : "5",
    4 : "4",
    3 : "3",
    2 : "2",
}

# handvalue = rank*16^5 + cardrank(16^4*a+16^3*b+16^2*c+16^1i*d+16^0*e)
hands = [
    { "name": "Five of a kind", "layout": 11111, "rank": 7 },
    { "name": "Four of a kind", "layout": 11112, "rank": 6 },
    { "name": "Full House",     "layout": 11122, "rank": 5 },
    { "name": "Three of a kind","layout": 11123, "rank": 4 },
    { "name": "Two pair",       "layout": 11223, "rank": 3 },
    { "name": "One pair",       "layout": 11234, "rank": 2 },
    { "name": "High card",      "layout": 12345, "rank": 1 },
]

# game and bid
games = [
    [ "32T3K", 765 ],
    [ "T55J5", 684 ],
    [ "KK677",  28 ],
    [ "KTJJT", 220 ],
    [ "QQQJA", 483 ],
]

class Game:
    #def __init__(self, cards, bid):
    #    self.cards = cards
    #    self.bid = bid
    #    self.hand = Hand(cards)  

    def __init__(self, line):
        l = line.strip().split(' ')
        self.cards = l[0]
        self.bid = int(l[1])
        self.hand = Hand(l[0])  

    def compare(self, game):
        if self.rank < game.rank: return -1
        if self.rank > game.ramk: return 1
        for i in range(len(cards)):
            if self.cards[i] < game.cards[i]: return -1
            if self.cards[i] > game.cards[i]: return 1
        return 0 

class Hand:
    def __init__(self, data):
        self.data = data
        self.hand = ""
        self.rank = 0
        self.value = 0
        self.weight(data)

    def weight(self, data):
        weightedcards = []
        cardsofweight = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for c in data:
            weightedcards.append( cards[c] )
            cardsofweight[cards[c]] += 1
            self.value *= 16
            self.value += cards[c]
        scx = sorted( [(count, index) for index, count in enumerate(cardsofweight) if 0 < count ], reverse=True)
        sc = []
        for count, weight in scx:
            for x in range(count):
                sc.append( [k for k, v in cards.items() if v == weight][0] )
        lastc = sc[0]
        lasti = 1
        whand = 0
        for i in sc:
            if not lastc == i:
                lasti += 1
            whand *= 10
            whand += lasti 
            lastc = i
        for hand in hands:
            if hand["layout"] == whand:
                self.hand = hand["name"]
                self.rank = hand["rank"]
                self.value += hand["rank"]*1048576 
                print(self.hand, "cards ", self.data, " value ", self.value)

# read all games
#sample data
#plays = []
#for pcards, pbid in games.items():
#   plays.append( Game(pcards, pbid) )

datafile = open('dec07.data', 'r')
lines = datafile.readlines()
plays = [Game(line) for line in lines]

#
solver = []
for play in plays:
    solver.append( (play.hand.value, play.bid) )

count = 1
result = 0
#print(solver)
for v, b in sorted(solver):
    result += (int(b) * count) 
    count += 1

print("result ", result)
