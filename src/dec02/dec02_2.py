'''Advent Of Code 2023 - Day 02'''

from game import Game

print("Hello Advent Of Code 2023 - December 02")

print("game of colored cubes - dec02.data")

class PowerGame(Game):

    def power(self):
        minr = 1
        ming = 1
        minb = 1
        for move in self.moves:
            #print("{}".format(move))
            if minr < move.red:
                minr = move.red
            if ming < move.green:
                ming = move.green
            if minb < move.blue:
                minb = move.blue
        print("PowerCubes (r,g,b): ( {},{},{})".format(minr, ming, minb))
        return minr * ming * minb

if __name__ == "__main__":
    datafile = open('dec02.data', 'r')
    lines = datafile.readlines()
    games = [PowerGame(line) for line in lines]

    # add power of all games
    # power = product of minimal necessary rgb cubes of all moves in^ game
    result = 0

    for game in games:
        power = game.power()
        result += power
        print("PowerGame {}: power {} result {}".format(game.id, power, result))

    print("Puzzle result: {}".format(result))
