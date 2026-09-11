








import pickle
ID_list = [ID for ID in range(50, 52)]



time_interval = 1   # 时间步长
RW_type = 'K'
all_time = 31 * 24 * 3600  # s
bei = 10  # 10 100 1000 10000



for ID_value in ID_list:
    ID = ID_value
    path = "/home/data/vol/ID_%s.csv" % str(ID)

    fp = open(path, "r")
    all_size, burst_size = 0, 0
    index = 0
    
    # 打开文件读取二进制数据
    with open('/home/data/vol/burst/10/ID_%s.pkl' % (str(ID)), 'rb') as f:
        burst_list = pickle.load(f)
    
    
    for eachline in fp: # 先统计一波总的size

        line = eachline[:-1].split(",")
        RW = line[1][0]         # R or W
        size = int(line[3])     # bytes
        # time = int(line[4])     # us  1000000us = 1s

        if RW != RW_type:
            all_size += size
        if burst_list[index] == 1:
            burst_size += size
        index += 1
    fp.close()
    
    print(ID, str(burst_size / all_size * 100))


































