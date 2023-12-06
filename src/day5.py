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
        while len(seeds) > 0:
            start = int(seeds.pop(0))
            end = start + int(seeds.pop(0))
            print("pair of seed range" + str(end-start))
            print(start)
            print(end)
            print(seeds)
            while start < end:
                print(start)
                pos = dohfind(start, datalist[1])
                pos = dohfind(pos, datalist[2])
                pos = dohfind(pos, datalist[3])
                pos = dohfind(pos, datalist[4])
                pos = dohfind(pos, datalist[5])
                pos = dohfind(pos, datalist[6])
                pos = dohfind(pos, datalist[7])
                locations.append(pos)
                start = start + 1
    return locations

def dohfind(s,firstsecond):
    for check in firstsecond:
        if int(check[1]) <= s < (int(check[1]) + int(check[2])):
            return int(check[0]) + (s-int(check[1]))
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
    myInput.sort()
    print(myInput)
    print(myInput[0])
    print("--- %s seconds ---" % (time.time() - start_time))
    #myInput = readData('../data/day5_realdata')
    #print(myInput)
    #myInput.sort()
    #print(myInput)
    #print(myInput[0])


