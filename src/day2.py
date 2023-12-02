import re
def readData(file):
    mygames = []
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            mygames.append(line.replace("\n", "").split(': '))
        for game in mygames:
            game[0] = game[0].replace("Game ", "")
            game[1] = game[1].split('; ')
            game.append(findhigh(game[1]))
    return mygames

def findhigh(game):
    # highs of red, green, blue
    highs = [0, 0, 0]
    red = 0
    green = 0
    blue = 0
    for go in game:
        turns = go.split(", ")
        for turn in turns:
            t = turn.split(",")
            num, col = t[0].split(" ")
            num = int(num)
            if col == 'red':
                if num > red:
                    red = num
            if col == 'green':
                if num > green:
                    green = num
            if col == 'blue':
                if num > blue:
                    blue = num
        #find high of each colour and return list of highred=x,highblue=y,highgreen=z)
        highs[0] = red
        highs[1] = green
        highs[2] = blue
    return highs

if (__name__ == "__main__"):
    myInput = readData('../data/day2_realdata')
    # which games possible if only 12 red cubes, 13 green cubes, and 14 blue cubes in bag
    # so loop through all games and check red green and blue highs
    # if possible then sum the game numbers and return that number
    print("myInput = " + str(myInput))
    answer = 0
    answer2 = 0
    red = 12
    green = 13
    blue = 14
    for game in myInput:
        gamenum = int(game[0])
        gamehighs = game[2]
        answer2 = answer2 + (int(gamehighs[0]) * int(gamehighs[1]) * int(gamehighs[2]))
        if int(gamehighs[0]) > red or int(gamehighs[1]) > green or int(gamehighs[2]) > blue:
            answer = answer
        else:
            answer = answer + gamenum
    print("answerPart1 = " + str(answer))
    print("answerPart2 = " + str(answer2))
    #myInput = readData('../data/day1_realdata')
    #print("Summing the coords = " + str(answer))
