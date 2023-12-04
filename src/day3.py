def readData(file):
    map = []
    coordsmap = {}
    # list of part number and grid reference, e.g. 256,1,1
    numbers = []
    gearcoords = []
    # list of symbols and grid reference, e.g. #,2,1
    symbols = {}
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        x = 1
        for line in myfile:  # For each line of text,
            myline = line.replace("\n", "")
            map.append(myline)
            number = ''
            numcoords = []
            y = 1
            for char in myline:
                coordsmap[str(x)+ ',' +str(y)] = char
                if char.isdigit():
                    number = number + char
                    numcoords.append(str(x) + ',' + str(y))
                elif char == '.':
                    if number != '':
                        numbers.append([number, numcoords])
                        number = ''
                        numcoords = []
                else:
                    symbols[str(x) + ',' + str(y)] = char
                    if char == '*':
                        gearcoords.append(str(x) + ',' + str(y))
                    if number != '':
                        numbers.append([number, numcoords])
                        number = ''
                        numcoords = []
                y = y + 1
            if number != '':
                numbers.append([number, numcoords])
                number = ''
                numcoords = []
            x = x + 1
    numbersdict = {}
    for num in numbers:
        for n in num[1]:
            numbersdict[n] = num[0]
    # for each number in numbers list look around and see if I have adjacent symbol
    count = 0
    for num in numbers:
        for ref in num[1]:
            if checkaround(ref, symbols):
                count = count + int(num[0])
                break
    # loop through the symbols, if * then if two numbers linked then times together and sum
    gears = 0
    for gear in gearcoords:
        gears = gears + checkifgear(gear, coordsmap, numbersdict)
    print(gears)
    return map

def checkifgear(pos, coords, numbers):
    # check all positions around gear position and see if two numbers exist
    # if two numbers exist,find what they are and times them together and return
    sx,sy = pos.split(',')
    x,y = int(sx), int(sy)
    gearnums = []
    # check to the left
    if coords[str(x-1) + ',' + str(y-1)].isdigit():
        gearnums.append(str(x-1) + ',' + str(y-1))
    if coords[str(x-1) + ',' + str(y)].isdigit():
        gearnums.append(str(x-1) + ',' + str(y))
    if coords[str(x-1) + ',' + str(y+1)].isdigit():
        gearnums.append(str(x-1) + ',' + str(y+1))
    # check to the right
    if coords[str(x+1) + ',' + str(y-1)].isdigit():
        gearnums.append(str(x+1) + ',' + str(y-1))
    if coords[str(x+1) + ',' + str(y)].isdigit():
        gearnums.append(str(x+1) + ',' + str(y))
    if coords[str(x+1) + ',' + str(y+1)].isdigit():
        gearnums.append(str(x+1) + ',' + str(y+1))
    # check to the above and below
    if coords[str(x) + ',' + str(y-1)].isdigit():
        gearnums.append(str(x) + ',' + str(y-1))
    if coords[str(x) + ',' + str(y+1)].isdigit():
        gearnums.append(str(x) + ',' + str(y+1))
    gearnumvalues = []
    for gear in gearnums:
        gearnumvalues.append(numbers[gear])
    gearnumvalues = list(dict.fromkeys(gearnumvalues))
    answer = 0
    if len(gearnumvalues) > 1:
        answer = int(gearnumvalues[0])*int(gearnumvalues[1])
    return answer
def checkaround(pos, symbols):
    # check all positions around grid position and see if a symbol exists
    # if symbol found then return true, else false
    # 11 = check 12, 22, 21, 20, , 11, 10,
    # check above and below
    sx,sy = pos.split(',')
    x,y = int(sx), int(sy)
    # check to the left
    if str(x-1) + ',' + str(y-1) in symbols:
        return True
    if str(x-1)  + ',' + str(y) in symbols:
        return True
    if str(x-1) +  ',' +str(y+1) in symbols:
        return True
    # check to the right
    if str(x+1) +  ',' + str(y-1) in symbols:
        return True
    if str(x+1) + ',' + str(y) in symbols:
        return True
    if str(x+1) + ',' + str(y+1) in symbols:
        return True
    # check to the above and below
    if str(x) + ',' + str(y-1) in symbols:
        return True
    if str(x) + ',' + str(y+1) in symbols:
        return True
    return False

if (__name__ == "__main__"):
    myInput = readData('../data/day3_data')
    # which games possible if only 12 red cubes, 13 green cubes, and 14 blue cubes in bag
    # so loop through all games and check red green and blue highs
    # if possible then sum the game numbers and return that number
    print("myInput = " + str(myInput))
    myInput = readData('../data/day3_realdata')
    print("myInput = " + str(myInput))
