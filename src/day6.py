import time

def readData(file):
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        datalist = []
        print("Read the file in")
        for line in myfile:  # For each line of text
            llist = line.split()
            datalist.append(llist)
        tlist = datalist[0][1:len(datalist[0])]
        dlist = datalist[1][1:len(datalist[1])]
        tdlist = []
        count = 0
        while count < len(tlist):
            tdlist.append((tlist[count], dlist[count]))
            count = count + 1
        print(tdlist)
        answerl = []
        answer = 1
        totalcount = 1
        for el in tdlist:
            winscount = 0
            duration = int(el[0])
            record = int(el[1])
            print(duration)
            print(record)
            distances = []
            for hold in range(duration):
                if hold == 0:
                    continue
                if hold == duration:
                    continue
                distances.append((duration-hold)*hold)
            print(distances)
            for el in distances:
                if el > record:
                    winscount = winscount + 1
            answerl.append(winscount)
        for e in answerl:
            answer = answer * e
    return answer

def dohfind(s,firstsecond):
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
    myInput = readData('../data/day6_data')
    print(myInput)
    myInput = readData('../data/day6_realdata')
    print(myInput)


