import time

def readData(file):
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        datalist = []
        print("Read the file in")
        for line in myfile:  # For each line of text
            llist = line.split()
            datalist.append(llist)
        print(datalist)
        hand = ''
        bet = ''
        count = 0
        rank = []
        for go in datalist:
            hand = go[0]
            bet = go[1]
            print(hand)
            print(bet)
            # find hand type
            go.append(findhand(hand))
    return datalist

def findhand(hand):
    hands = set(hand)
    print(hands)
    d = {x: hand.count(x) for x in hand}
    print(d)
    a, b = list(d.keys()), list(d.values())
    print(a)
    print(b)
    b.sort(reverse=True)
    print(b)
    if len(set(hands)) == 1:
        return 'FK'
    if len(set(hands)) == 5:
        return 'HC'
    if len(set(hands)) == 2:
        return 'FH'
    return '??'

def convert(datalist):
    output1 = {}
    for x in datalist:
        start = int(x[1])
        num = int(x[2])
        dest = int(x[0])
        i = 0
        for y in range(num):
            output1[start+i] = dest+i
            i = i + 1
    return output1

if (__name__ == "__main__"):
    start_time = time.time()
    myInput = readData('../data/day7_data')
    print(myInput)
    #myInput = readData('../data/day7_realdata')
    #print(myInput)


