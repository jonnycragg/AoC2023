import re
def readData(file):
    allCoords = []  # Declare an empty list
    allNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            myCoords = []  # Declare an empty list
            # clean line
            cleanline = line.replace(" ", "").replace("\n", "")
            # point at start of string, check all digits and list of worded numbers from that point
            # if find any then add this number to coords and move pointer by length of that number found
            # if no match discard the single char and move to next position
            for number in allNumbers:
                if cleanline.startswith(number):
                    myCoords.append(number)
                    cleanline.removeprefix(number)
                else:
                    cleanline = cleanline[1:]

            for char in cleanline:
                if char.isdigit():
                    myCoords.append(char)
            print("Ellie, this line =" + cleanline)
            print("myCoords = " + str(myCoords))
            # concatentate first and last digit in myCoords
            allCoords.append(myCoords[0] + myCoords[len(myCoords)-1])
            print("allCoords = " + str(allCoords))
        # when end of line catch the last elf
    return allCoords


if (__name__ == "__main__"):
    myInput = readData('../data/day1_data')
    answer = 0
    for coord in myInput:
        answer = answer + int(coord)
    print("Summing the coords = " + str(answer))

    myInput = readData('../data/day1_realdata')
    answer = 0
    for coord in myInput:
        answer = answer + int(coord)
    print("Summing the coords = " + str(answer))
