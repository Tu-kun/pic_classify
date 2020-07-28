with open('result.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

def isNone(item, count = 0):
    #判断数据是否为空，并统计空值个数
    if item == 'None' or item == '[]':
        count += 1

    return count

year_none = 0
month_none = 0
day_none = 0
auth_none = 0
nationality_none = 0
loc_none = 0
key_words_none = 0

for line in lines:
    line = line.split('\t')
    year = line[2]
    month = line[3]
    day = line[4]
    name = line[5]
    nationality = line[6]
    loc = line[7]
    key_words = line[8]

    year_none = isNone(year, year_none)
    month_none = isNone(month, month_none)
    day_none = isNone(day, day_none)
    auth_none = isNone(name, auth_none)
    nationality_none = isNone(nationality, nationality_none)
    loc_none = isNone(loc, loc_none)
    key_words_none = isNone(key_words, key_words_none)


print('年份为空的数据个数:{}'.format(year_none))
print('月份为空的数据个数:{}'.format(month_none))
print('日期为空的数据个数:{}'.format(day_none))
print('摄影师为空的数据个数:{}'.format(auth_none))
print('国家为空的数据个数:{}'.format(nationality_none))
print('拍摄地点为空的数据个数:{}'.format(loc_none))
print('关键字为空的数据个数:{}'.format(key_words_none))

