import os
import sys
import time


class pic_classify():
    def __init__(self, path):
        self.path = path
        self.content = ''
        self.number = []
        self.tag1 = []
        self.create_time = []
        # self.year = []
        # self.month = []
        # self.day = []
        self.name = []
        self.nationality = []
        self.loc = []
        self.key_words = []
        self.load_file()

    def load_file(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.read().splitlines()
        for line in content:
            line = line.split('\t')
            # print(line)
            self.number.append(line[0])
            self.tag1.append(line[1])
            create_time = [line[2], line[3], line[4]]
            self.create_time.append(create_time)
            self.name.append(line[5])
            self.nationality.append(line[6])
            self.loc.append(line[7])
            self.key_words.append(line[8])

    @staticmethod
    def de_duplication(keyWords):
        keyWords = [list(i) for i in keyWords]
        result = []
        for index in range(len(keyWords) - 1, -1, -1):
            flag = 0  # 当这个元素不在其他元素中时标志加一，
            add = 0
            for j in keyWords[:index]:
                if keyWords[index][0] not in j[0]:
                    flag += 1  # 当这个元素不在其他元素中时标志加一
                    continue
                else:
                    j[1] = int(j[1]) + keyWords[index][1]  # 合并出现次数
                    continue
            if flag == index:
                result.append(keyWords[index])
        return result


    def get_tag1(self):
        tags = list(set(self.tag1))
        print('一级标签（共{}个一级标签）：'.format(len(tags)))
        for tag in tags:
            print(tag, end='    ')
        print()

    def classify_byCountry(self):
        root_Path = os.path.dirname(os.getcwd())
        ciku_Path = root_Path + os.sep + "词库" + os.sep
        with open(ciku_Path+'国家和地区词库.txt', 'r', encoding='utf-8') as f:
            all_continents = f.read().splitlines()
            country_to_continents = {}
            for i in all_continents:
                line = i.split(' ')
                country_to_continents[line[0]] = line[1]   # 国家和洲的对应字典
        # print(country_to_continents)
        print('带国家信息的数据共{}条'.format(len(self.nationality)))
        country = list(set(self.nationality))  # 所有出现的国家信息
        all_country = []
        for cou in country:
            for i in eval(cou):
                all_country.append(i)
                # print(i)
        all_country = list(set(all_country))  # 去重后的所有国家信息
        # print(all_country)
        result = {k: [v[1] for v in country_to_continents.items() if v[0] == k][0] for k in all_country}  # 将每个国家匹配对应的洲
        continents = set([cont for cont in result.values()])  # 获取所有出现的洲
        result1 = {v: [i[0] for i in result.items() if i[1] == v] for v in continents}   # 统计每个洲出现的国家
        print('按国家分类: 共{}个国家'.format(len(all_country)))
        for i in result1.items():
            print(i[0]+':', end='  ')
            [print(item, end='   ') for item in i[1]]
            print()

    def classify_byKeywords(self):
        dic = {}
        for line in self.key_words:
            for key in eval(line):
                dic[key] = dic.get(key, 0) + 1

        sort_list = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        sort_list = self.de_duplication(sort_list)
        print('总共有{}条主题数据'.format(len(sort_list)))
        final_list = [i for i in sort_list if i[1] > 50]
        print('出现次数在50次以上的数据有{}条'.format(len(final_list)))
        for i in final_list[::-1]:
            # print('{} {}'.format(i[0], i[1]))
            print(i, end='    ')
        print()

    @staticmethod
    def count_frequrency(raw_list):
        #传递一个list，返回一个字典，字典的key是list中的每个元素，value是每个元素出现的次数
        dict = {}
        for item in raw_list:
            dict[item] = dict.get(item, 0) + 1
        return dict

    def classify_bytime(self):
        years = [date[0] for date in self.create_time]
        year_dict = self.count_frequrency(years)

        print('时间分类如下：')
        for year in sorted(set(years)):
            months = [date[1] for date in self.create_time if date[0] == year]
            month_dict = self.count_frequrency(months)
            print('{}年的照片共{}张'.format(year, year_dict[year]))
            for month in sorted(set(months)):
                print('\t{}月份的照片共{}张'.format(month, month_dict[month]))

    def classify_byName(self):
        print('摄影师姓名统计如下：')
        names = self.name
        names_dict = self.count_frequrency(names)
        sort_list = sorted(names_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        for name in sort_list:
            # print('{} {}'.format(name[0], name[1]))
            print(name, end='  ')
        print()

    def classify_byPlace(self):
        places = []
        for i in self.loc:
            for l in eval(i):
                places.append(l)
        places_dict = self.count_frequrency(places)
        sort_list = sorted(places_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        final_list = [i for i in sort_list if i[1] > 30]
        final_list = self.de_duplication(final_list)
        print('地点分类如下(仅显示出现次数在30次以上的数据)：共{}个'.format(len(final_list)))
        for place in final_list[::-1]:
            # print('{} {}'.format(place[0], place[1]))
            print(place, end='  ')
        print()

    def show(self):
        self.get_tag1()
        self.classify_bytime()
        self.classify_byName()
        self.classify_byCountry()
        self.classify_byKeywords()
        self.classify_byPlace()


if __name__ == '__main__':
    start_time = time.time()

    Path = os.path.dirname(os.getcwd())
    dataPath = Path + os.sep + 'data'
    result = os.path.join(dataPath, 'result.txt')
    claaify = pic_classify(result)
    claaify.show()

    end_time = time.time()
    run_time = round(end_time - start_time, 5)
    print('运行时间为：{}'.format(run_time))
