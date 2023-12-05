from typing import Dict, Any


def readData(file):
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        datalist = []
        seeds = []
        seed = []
        soil = []
        soil2 = []
        fertilizer = []
        fertilizer2 = []
        water = []
        water2 = []
        light = []
        light2 = []
        temperature = []
        temperature2 = []
        humidity = []
        humidity2 = []
        location = []
        location2 = []
        print("Read the file in")
        for line in myfile:  # For each line of text
            line = line.strip()
            #print("current line = " + line)
            llist = line.split()
            #print("current llist = " + str(llist))
            if line == '':
                continue
            if llist[0] == 'seeds:':
                seeds = llist[1:len(llist)]
                #print("seeds = " + str(seeds))
                datalist.append(seeds)
                continue
            groupname = llist[0]
            nlist = []
            #print("in group name = " + groupname)
            for nline in myfile:
                nline = nline.strip()
                #print("nline = " + nline)
                if nline == '':
                    break
                nlist.append(nline.split())
                #print(groupname + " = " + str(nlist))
            datalist.append(nlist)
        print("dataline list = " + str(datalist))
        seeds = datalist[0]
        # create the maps to traverse through in a bit for each of the seeds
        print("Create maps seed and soil")
        seedsoil = convert(datalist[1])
        print("Create maps soil2 and fert")
        soil2fertilizer = convert(datalist[2])
        print("Create maps fert2 and water")
        fertilizer2water = convert(datalist[3])
        print("Create maps water2 and light")
        water2light = convert(datalist[4])
        print("Create maps light2 and temp")
        light2temperature = convert(datalist[5])
        print("Create maps temp2 and humid")
        temperature2humidity = convert(datalist[6])
        print("Create maps humid and loc")
        humidity2location = convert(datalist[7])
        # for each seed traverse through maps
        print("Traverse through maps for seeds")
        print(seeds)
        locations = []
        for thisseed in seeds:
            thisseed = int(thisseed)
            print(thisseed)
            pos = findmap(thisseed, seedsoil)
            pos = findmap(pos, soil2fertilizer)
            pos = findmap(pos, fertilizer2water)
            pos = findmap(pos, water2light)
            pos = findmap(pos, light2temperature)
            pos = findmap(pos, temperature2humidity)
            pos = findmap(pos, humidity2location)
            locations.append(pos)
        print(locations)
    return locations

def findmap(s,firstsecond):
    ans = 0
    print("findmap")
    print(s)
    print(firstsecond)
    if s in firstsecond:
        #print("found this seed in the seed map")
        #print(first.index(s))
        return firstsecond[s]
    else:
        return s

def convert(datalist):
    output1 = {}
    print(datalist)
    for x in datalist:
        start = int(x[1])
        num = int(x[2])
        dest = int(x[0])
        i = 0
        print(start)
        print(num)
        print(dest)
        for y in range(num):
            output1[start+i] = dest+i
            i = i + 1
            print(i)
    print(output1)
    return output1

if (__name__ == "__main__"):
    myInput = readData('../data/day5_data')
    print(myInput)
    myInput.sort()
    print(myInput)
    myInput = readData('../data/day5_realdata')
    print(myInput)
    myInput.sort()
    print(myInput)


