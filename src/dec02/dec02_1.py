'''Advent Of Code 2023 - Day 02'''

from game import Game

print("Hello Advent Of Code 2023 - December 02")

print("game of colored cubes - dec02.data")

# which games could be played with 12 red, 13 green, 14 blue cubes?

if __name__ == "__main__":
    datafile = open('dec02.data', 'r')
    lines = datafile.readlines()
    games = [Game(line) for line in lines]

    # filter out all games with impossible moves wit rgb > 12,13,14
    # add all possible games
    result = 0

    for game in games:
        print("Game {}: {} moves".format(game.id, len(game.moves)))
        if not game.impossible( 12, 13, 14 ):
            result += game.id
            print("result: {}".format(result))
        else:
            print("result: {} - no change, impossible game".format(result))

    print("Puzzle result: {}".format(result))
