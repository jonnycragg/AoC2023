import time

def readData(file):
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        datalist = []
        print("Read the file in")
        for line in myfile:  # For each line of text
            line = line.strip()
            llist = line.split()
            if line == '':
                continue
            if llist[0] == 'seeds:':
                seeds = llist[1:len(llist)]
                datalist.append(seeds)
                continue
            nlist = []
            for nline in myfile:
                nline = nline.strip()
                if nline == '':
                    break
                nlist.append(nline.split())
            datalist.append(nlist)
        seeds = datalist[0]
        print(seeds)
        print(datalist)
        locations = []
        found = False
        # loop backwards, start from 0 and travers backwards until we find a seed in list then stop
        start = 0
        end = 100000000
        printcounter = 0
        while start < end:
            printcounter = printcounter + 1
            if printcounter == 100000:
                print("looping through..." + str(start))
                printcounter = 0
            pos = dohfind(start, datalist[7])
            #print(pos)
            pos = dohfind(pos, datalist[6])
            #print(pos)
            pos = dohfind(pos, datalist[5])
            #print(pos)
            pos = dohfind(pos, datalist[4])
            #print(pos)
            pos = dohfind(pos, datalist[3])
            #print(pos)
            pos = dohfind(pos, datalist[2])
            #print(pos)
            pos = dohfind(pos, datalist[1])
            #print(pos)
            if str(pos) in seeds:
                found = True
                print("reverse found a seed")
                print(pos)
                break
            start = start + 1
    return pos

def dohfind(s,firstsecond):
    for check in firstsecond:
        #print(check[0] + " <= " + str(s) + " < " + str(int(check[0]) + int(check[2])))
        if int(check[0]) <= s < (int(check[0]) + int(check[2])):
            return int(check[1]) + (s-int(check[0]))
    return s


def dohfind2(s,firstsecond):
    for check in firstsecond:
        if int(check[1]) <= s < (int(check[1]) + int(check[2])):
            return int(check[0]) + (s-int(check[1]))
    return s


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
    myInput = readData('../data/day5_data')
    print(myInput)
    print("--- %s seconds ---" % (time.time() - start_time))
    myInput = readData('../data/day5_realdata')
    print(myInput)
    print("--- %s seconds ---" % (time.time() - start_time))
    #myInput.sort()
    #print(myInput)
    #print(myInput[0])