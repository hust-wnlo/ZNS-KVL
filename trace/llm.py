











# # 689,063662099, WS, 4096, 63177040, 8; 898,445275133, R, 106496, 61292544, 208
# # 1468,198540491, WS, 4096, 63182544, 8; 1657,438961778, R, 131072, 123349728, 256
# # 182,682769108, W, 16384, 168034328, 32; 1004,797109001, RA, 61440, 167772688, 120
# # 1079,337257236, W, 16384, 168046648, 32; 1904,433331523, RA, 61440, 167772688, 120
# # 39846,376706841, W, 131072, 191889408, 256; 41331,264799772, RA, 98304, 134036800, 192

# root_dir = "/home/data/Trace/LLM/"
# files = ["md-ds-13b_1.txt", "md-ds-13b_16.txt", "md-fg-30b_1.txt", "md-fg-30b_16.txt", "kv-fg-67b_64.txt"]
# files = ["md-fg-30b_16.txt"]   # TODO



# def wsRAR(address, sizes, theta):
#     lbafre = dict()
#     rar_req, all_req = 0, 0
#     if len(address) == 0:
#         wsRARatio = 0
#     else:
#         for index, lba in enumerate(address):
#             # assert sizes[index] % 512 == 0
#             size = sizes[index]
#             for offset in range(size):
#                 if lba + offset in lbafre.keys():
#                     lbafre[lba + offset] += 1
#                 else:
#                     try:
#                         lbafre[lba + offset] = 1
#                     except:
#                         print("error", len(lbafre))

#                 if lbafre[lba + offset] >= theta:
#                     rar_req += 1
#                 all_req += 1
#         if all_req != 0:
#             wsRARatio = rar_req / all_req
#         else:
#             wsRARatio = 0
#     return wsRARatio

# def randRatio(address, sizes, theta, front):
#     if len(address) <= front:
#         return -1
#     no_rand_num = 0
#     request_pass, size_pass = [], []
#     for i in range(front):
#         request_pass.append(address[i])
#         size_pass.append(sizes[i])
#     for index, lba in enumerate(address[front:]):
#         size = sizes[front:][index]
#         for pass_index, pass_lba in enumerate(request_pass):
#             pass_size = size_pass[pass_index]
#             mm = []
#             mm.append(abs(lba - pass_lba))
#             mm.append(abs(lba + size - pass_lba))
#             mm.append(abs(lba - pass_lba - pass_size))
#             mm.append(abs(lba + size - pass_lba - pass_size))
#             if min(mm) < theta:
#                 no_rand_num += 1
#                 break
#         del request_pass[0]
#         del size_pass[0]
#         request_pass.append(lba)
#         size_pass.append(size)

#     return (len(address) - front - no_rand_num) / (len(address) - front)





# for file in files:
#     path = root_dir + file


#     all_size = dict()
#     for tt in range(1079, 1905):   # TODO
#         fp = open(path, "r")
#         addresses, sizes = [], []
#         for eachline in fp:
#             line = eachline[:-1].split(", ")
#             time = int(int(line[0]) // 1e9)  # ns->s
#             op = line[1]
#             lba = int(int(line[3]) / 2) # KB
#             size = int(int(line[4]) / 2)  # KB

#             if time == tt and op == 'W':  # TODO
#                 addresses.append(lba)
#                 sizes.append(size)

#         rar = wsRAR(addresses, sizes, 2)
#         rdm = randRatio(addresses, sizes, 128, 32)
#         print(str(tt) + "," + str(round(rar, 5)) + "," + str(round(rdm, 5)))

#         fp.close()





















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
            for offset in range(size):
                lba_ = lba + offset
                if lba_ in tmp_life.keys():
                    life = time - tmp_life[lba_]
                    if life >= 0:
                        all_life.append(life)
                        tmp_life[lba_] = time
                else:
                    tmp_life[lba_] = time

    file = open("life.txt", "w")

    all_life = set(all_life)

    for i in all_life:
        file.write(str(i) + "\n")









































