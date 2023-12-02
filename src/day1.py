import re
def readData(file):
    myCoords = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean line
            cleanline = line.replace(" ", "").replace("\n", "")
            # if number then accumulate it until blank line
            print("Ellie, this line =" + cleanline)
            print(re.findall(r'\d+', cleanline))
        # when end of line catch the last elf
    return myCoords


if (__name__ == "__main__"):
    myInput = readData('../data/day1_data')
    myInput.sort(reverse=True)
    print("Ellie biggest 3 = " + str(myInput))
    print(myInput[0]+myInput[1]+myInput[2])

    myInput = readData('../data/day1_data')
    myInput.sort(reverse=True)
    print(myInput)
    print(myInput[0]+myInput[1]+myInput[2])