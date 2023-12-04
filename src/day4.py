def readData(file):
    mygames = []
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            mygames.append(line.replace("\n", "").split(': '))
        winnings = 0
        for game in mygames:
            game[0] = game[0].replace("Card ", "")
            game[1] = game[1].split(' | ')
            game[1][0] = game[1][0].split(" ")
            game[1][1] = game[1][1].split(" ")
            game.append(findwinner((game[1])))
            #winnings = winnings + findwinner(game[1])
        #print(winnings)
    return mygames
def findwinner(game):
    # check numbers in first list exist in second and if so then calc value and return
    wins = 0
    value = 0
    mygo = game[0]
    checks = game[1]
    print(mygo)
    print(checks)
    for go in mygo:
        for num in checks:
            if go != '':
                if go == num:
                    wins = wins + 1
    return wins

if (__name__ == "__main__"):
    myInput = readData('../data/day4_data')
    # which games possible if only 12 red cubes, 13 green cubes, and 14 blue cubes in bag
    # so loop through all games and check red green and blue highs
    # if possible then sum the game numbers and return that number
    print("myInput = " + str(myInput))
    #myInput = readData('../data/day4_realdata')
    #print("myInput = " + str(myInput))
