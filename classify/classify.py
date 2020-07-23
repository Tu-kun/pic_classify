import os
import sys
import time

class pic_classify():
    def __init__(self, path):
        self.path = path
        self.content = ''
        self.number = []
        self.tag1 = []
        self.year = []
        self.month = []
        self.day = []
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
            self.year.append(line[2])
            self.month.append(line[3])
            self.day.append(line[4])
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
        # country = [i for i in ]
        country = list(set(self.nationality))
        all_country = []
        # print(country)
        for cou in country:
            for i in eval(cou):
                all_country.append(i)
                # print(i)
        all_country = list(set(all_country))

        print('摄影师国籍分类: 共{}个国家'.format(len(all_country)))
        for i in all_country:
            print(i, end='    ')

    def classify_byKeywords(self):
        dic = {}
        for line in self.key_words:
            key_list = eval(line)
            # print(key_list)
            for key in key_list:
                dic[key] = dic.get(key, 0) + 1

        sort_list = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

        print('总共有{}条主题数据'.format(len(sort_list)))
        final_list = [i for i in sort_list if i[1] > 50]
        print('出现次数在50次以上的数据有{}条'.format(len(final_list)))
        for i in final_list:
            print(i, end='   ')
        print()

    def show(self):
        self.get_tag1()
        self.classify_byCountry()
        self.classify_byKeywords()

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