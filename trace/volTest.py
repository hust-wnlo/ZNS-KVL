# TODO 统计在访问频率中各个固定的访问频率下的随机率变化

file = open("Result.csv", "a+")

import math, pickle

ID_list = [ID for ID in range(0, 1000)]


for ID_value in ID_list:
    ID = ID_value
    path = "/home/data/vol/ID_%s.csv" % str(ID)
    fp = open(path, "r")

    with open('/home/data/vol/rand/ID_%s.pkl' % str(ID), 'rb') as f:
        rand_flag = pickle.load(f)
    rand_index = 0
    frequency = {1:0, 2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0, 512:0, 1024:0}
    frequency_rand = {1:0, 2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0, 512:0, 1024:0}
    obj = dict()

    for eachline in fp:

        line = eachline[:-1].split(",")
        lba = int(line[2])
        RW = line[1][0]
        end = lba + int(line[3])
        lba = lba // 4096
        size = math.ceil(end / 4096) - lba
        rf = rand_flag[rand_index]
        rand_index += 1


        for offset in range(size):
            address = lba + offset
            if address in obj:
                if RW == 'R':
                    obj[address] += 1
                    
                else:  # 含义是如果读着读着被写覆盖了 就需要重新统计
                    del obj[address]
            else:
                if RW == 'R':
                    obj[address] = 1
                    frequency[obj[address]] += 1
                    if rf == 1:   # 属于随机请求
                        frequency_rand[obj[address]] += 1
                    
    ss = str(ID) + ","
    
    if rand_index != len(rand_flag):
        print("error!!!")
        ss = str(ID) + "!!!,"
    
    for i in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        if frequency[i] != 0:
            ratio = round(frequency_rand[i] / frequency[i] * 100, 6)
        else:
            ratio = "-"
        ss += str(ratio) + ","
    file.write(ss[:-1] + "\n")
    file.flush()
    
    fp.close()
    print(str(ID))


file.close()




# TODO 统计访问频率

file = open("Result.csv", "a+")

import math

ID_list = [ID for ID in range(0, 1000)]

mm = 10000



for ID_value in ID_list:
    ID = ID_value
    path = "/home/data/vol/ID_%s.csv" % str(ID)
    fp = open(path, "r")

    frequency = [0 for _ in range(mm + 1)]
    obj = dict()
    all_R = 0

    for eachline in fp:

        line = eachline[:-1].split(",")
        lba = int(line[2])
        RW = line[1][0]
        end = lba + int(line[3])
        lba = lba // 4096
        size = math.ceil(end / 4096) - lba


        for offset in range(size):
            address = lba + offset
            if address in obj:
                if RW == 'R':
                    obj[address] += 1
                    all_R += 1
                else:  # 含义是如果读着读着被写覆盖了 就需要重新统计
                    if obj[address] >= mm:
                        frequency[-1] += 1
                    else:
                        frequency[obj[address]] += 1
                    del obj[address]

    for i in obj.keys():
        if obj[i] >= mm:
            frequency[-1] += 1
        else:
            frequency[obj[i]] += 1
    
    
    ss = str(ID) + ","
    for i in frequency[1:]:
        ss += str(i) + ","
    ss += str(all_R) + ","
    file.write(ss[:-1] + "\n")
    file.flush()
    
    fp.close()
    print(str(ID))


file.close()







# TODO 统计读写带宽

ID_list = [ID for ID in range(800, 1000)]


for ID_value in ID_list:
    ID = ID_value
    path = "/home/data/vol/ID_%s.csv" % str(ID)
    fp = open(path, "r")

    sizes_R = 0
    sizes_W = 0

    for eachline in fp:
        line = eachline[:-1].split(",")
        RW = line[1][0]
        size = int(line[3])

        if RW == 'R':
            sizes_R += size
        elif RW == 'W':
            sizes_W += size
        else:
            print("error!!!")

    bandwidth_R = str(round(sizes_R / 1024 / (31 * 24 * 3600), 2)) + str('KB/s')
    bandwidth_W = str(round(sizes_W / 1024 / (31 * 24 * 3600), 2)) + str('KB/s')
    print(bandwidth_R, bandwidth_W)
    fp.close()

