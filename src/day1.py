import re
def readData(file):
    allCoords = []  # Declare an empty list
    allNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            myCoords = []  # Declare an empty list
            # clean line
            cleanline = line.replace(" ", "").replace("\n", "")
            # start at beginning of string, check all digits and list of worded numbers from start of string
            # if find a match then add this number to coords and remove this number fron start of string and repeat
            # if no match then discard the single char fron start of string and repeat
            while cleanline != '':
                for number in allNumbers:
                    if cleanline.startswith(number):
                        # as we populate the coords convert from alpha to digit
                        myCoords.append(convert(number))
                        cleanline.removeprefix(number)
                        break
                # nothing matches so remove 1 char from start of string and repeat
                cleanline = cleanline[1:]

            #print("Ellie, this line =" + cleanline)
            #print("myCoords = " + str(myCoords))
            # concatentate first and last digit in myCoords
            allCoords.append(myCoords[0] + myCoords[len(myCoords)-1])
            #print("allCoords = " + str(allCoords))
    return allCoords

def convert(no):
    # if found 1-9 then simply return it
    if no.isdigit():
        return no
    else:
        if (no == 'one'):
            return '1'
        elif (no == 'two'):
            return '2'
        elif (no == 'three'):
            return '3'
        elif (no == 'four'):
            return '4'
        elif (no == 'five'):
            return '5'
        elif (no == 'six'):
            return '6'
        elif (no == 'seven'):
            return '7'
        elif (no == 'eight'):
            return '8'
        elif no == 'nine':
            return '9'
        else:
            return no
    return no

if (__name__ == "__main__"):
    myInput = readData('../data/day1_data2')
    answer = 0
    for coord in myInput:
        answer = answer + int(coord)
    print("Summing the coords = " + str(answer))

    myInput = readData('../data/day1_realdata')
    answer = 0
    for coord in myInput:
        answer = answer + int(coord)
    print("Summing the coords = " + str(answer))
