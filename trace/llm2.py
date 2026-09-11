









# TODO 输出写数据的寿命情况
# TODO 主要分析的类型[R, WS], [R, WS], [RA, W], [RA, W], [RA, W]

root_dir = "/home/data/Trace/LLM/"
# files = ["md-ds-13b_1.txt", "md-ds-13b_16.txt", "md-fg-30b_1.txt", "md-fg-30b_16.txt", "kv-fg-67b_64.txt"]
files = ["md-ds-13b_1.txt"]  # TODO




for file in files:
    path = root_dir + file
    fp = open(path, "r")

    tmp_life = dict()
    all_life = []


    for eachline in fp:
        line = eachline[:-1].split(", ")
        time = int(int(line[0]) // 1e3)  # ns->us
        op = line[1]
        lba = int(int(line[3]) / 2)  # KB
        size = int(int(line[4]) / 2)  # KB

        if op == 'WS':

            if lba % 4 == 0 and size % 4 == 0:
                for offset in range(0, size, 4):
                    lba_ = lba + offset
                    if lba_ in tmp_life.keys():
                        life = time - tmp_life[lba_]
                        if life >= 0:
                            all_life.append(life)
                            tmp_life[lba_] = time

    file = open("life_4.txt", "w")

    for i in all_life:
        file.write(str(i) + "\n")


























