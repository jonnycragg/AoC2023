def readData(file):
    mygames = []
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            mygames.append(line.replace("\n", "").split(': '))
        cardwins = []
        for num in mygames:
            cardwins.append(1)
        count = 0
        for game in mygames:
            current = count
            count = count + 1
            game[0] = game[0].replace("Card ", "")
            game[1] = game[1].split(' | ')
            game[1][0] = game[1][0].split(" ")
            game[1][1] = game[1][1].split(" ")
            winnings = findwinner((game[1]))
            game.append(winnings)
            index = count
            for y in range(cardwins[current]):
                if winnings > 0:
                    for x in range(winnings):
                        cardwins[index] = cardwins[index]+1
                        index = index + 1
                index = count
        print(cardwins)
        sumit = 0
        for n in cardwins:
            sumit = sumit + n
        print(sumit)
    return mygames
def findwinner(game):
    # check numbers in first list exist in second and if so then calc value and return
    wins = 0
    mygo = game[0]
    checks = game[1]
    for go in mygo:
        for num in checks:
            if go != '':
                if go == num:
                    wins = wins + 1
    return wins

if (__name__ == "__main__"):
    myInput = readData('../data/day4_data')
    print("myInput = " + str(myInput))
    myInput = readData('../data/day4_realdata')
    print("myInput = " + str(myInput))
