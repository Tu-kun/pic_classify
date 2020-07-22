with open('result_test.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()


dic = {}
for line in lines:
    line = line.split('\t')
    key_list = eval(line[8])

    for key in key_list:
        dic[key] = dic.get(key, 0) + 1
        # print(key)
        # if key not in dic.keys():
        #     dic[key] = 1
        # else:
        #     dic[key] += 1
# print(dic)
# print (sorted(dic, key = dic.values() )
sort_list = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
for i in sort_list:
    print(i)