'''Advent Of Code 2023 - Day 02'''

# Moves # <color> comma separated
# 3 blue, 4 red
# 1 red, 2 green, 6 blue
# 2 green
class Move:
    def __init__(self, data):
        self.red = int('0')
        self.green = 0
        self.blue = 0
        colors = data.split(',')
        for color in colors:
            parts = color.strip().split(' ')
            if 'red' == parts[1]:
                self.red = int(parts[0]) 
            elif 'green' == parts[1]:
                self.green = int(parts[0])
            elif 'blue' == parts[1]:
                self.blue = int(parts[0])
            else:
                print("unexpected color {}".format(parts[1]))

    def impossible(self, maxr, maxg, maxb):
        if maxr < self.red or maxg < self.green or maxb < self.blue:  
            #print("Impossible move (r: {} g:{} b:{})".format( self.red, self.green, self.blue))
            return True
        return False

    def __str__(self):
       
        s = 'Move(r,g,b): (' + str(self.red) + ',' + str(self.green) + ',' + str(self.blue) + ')' 
        print(s)
        return s

# Game #: <moves>
# Moves separated by ;
class Game:
    def __init__(self, data):
        #print("Game({})".format(data))
        values = data.split(':')
        self.id = int(values[0][5:])
        moves = values[1].split(';')
        self.moves = [Move(move) for move in moves]

    def impossible(self, maxr, maxg, maxb):
        for move in self.moves:
            if move.impossible( maxr, maxg, maxb ):
                return True
        return False

    def __str__(self):
        s = 'Game ' + self.id + ': Moves : '
        for move in self.moves:
            s+= '\n\t' + str(move)
        return s
        #return 'Game ' + self.id +': Moves : ' + str(self.moves)
