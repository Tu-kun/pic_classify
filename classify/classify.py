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

        print('总共有{}条主题数据'.format(len(sort_list)))
        final_list = [i for i in sort_list if i[1] > 50]
        print('出现次数在50次以上的数据有{}条'.format(len(final_list)))
        for i in final_list:
            print(i[0], end='  |  ')
        print()

    @staticmethod
    def count_frequrency(raw_list):
        #传递一个list，返回一个字典，字典的key是list中的每个元素，value是每个元素出现的次数
        dict = {}
        for item in raw_list:
            dict[item] = dict.get(item, 0) + 1
        return dict

    @staticmethod
    def quchong(raw_list):
        final_kew_words = []
        if len(raw_list) > 0:
            # 去重，如关键词中为 ['爱国主义教育'， '爱国主义'] 舍弃重复的’爱国主义‘
            final_kew_words.append(raw_list[0])  # 先将第一个元素添加进去
            for index in range(len(raw_list) - 1, -1, -1):
                for j in raw_list[:index]:
                    if raw_list[index] not in j:  # 后面的元素在前面未出现过则添加
                        final_kew_words.append(raw_list[index])
                        continue
                    else:  # 后面的元素在前面出现过就舍弃
                        break
            final_kew_words = list(set(final_kew_words))

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
        # TODO(kun): 以摄影师姓名分类
        pass

    def classify_byPlace(self):
        places = []
        for i in self.loc:
            for l in eval(i):
                places.append(l)
        places_dict = self.count_frequrency(places)
        sort_list = sorted(places_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        final_list = [i for i in sort_list if i[1] > 20]
        print('地点分类如下(仅显示出现次数在20次以上的数据)：共{}个'.format(len(final_list)))
        for place in final_list:
            print(place[0], end='  |  ')
        print()

    def show(self):
        self.get_tag1()
        self.classify_bytime()
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
