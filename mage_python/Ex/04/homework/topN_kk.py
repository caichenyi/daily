# encoding: utf-8
# Author: Cai Chenyi
path = 'www_access_20140823.log'
rt_path = 'top.txt'
stat = {}
topn = 10

fhandler = open(path, 'rt')
for line in fhandler:
    nodes = line.split()
    if len(nodes) < 9:
        continue
    key = (nodes[0], nodes[6], nodes[8])
    stat[key] = stat.get(key, 0) + 1
fhandler.close()

stat_list = list(stat.items())
print(stat_list)

for j in range(topn):
    for i in range(len(stat_list) - 1):
        if stat_list[i][1] > stat_list[i + 1][1]:
            stat_list[i], stat_list[i + 1] = stat_list[i + 1], stat_list[i]



fhandler = open(rt_path, 'wt')
for line in stat_list[-1:-11:-1]:
    fhandler.write('{},{},{},{}\n'.format(line[0][0], line[0][1], line[0][2], line[1]))
fhandler.close()