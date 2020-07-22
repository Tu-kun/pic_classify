import os
import re
import sys
import time



def timmer(func):
    def wrapper(*args, **kwargs):
        print('\n函数：\033[32;1m{_funcname_}()\033[0m 开始运行：'.format(_funcname_=func.__name__))
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('函数: \033[32;1m{_funcname_}()\033[0m 运行了 {_time_}秒'
              .format(_funcname_=func.__name__, _time_=(end_time - start_time)))
        return res

    return wrapper


class pic_classify:

    def __init__(self, listDirs, result_path):
        # 添加自定义词典
        self.load_dic()
        self.listDirs = listDirs
        self.result_path = result_path


    def load_dic(self):
        """
        将jieba词典的数据加载进来，构成自己的词典
        :return:
        """
        # 添加自定义词典
        Path = os.path.dirname(os.getcwd())
        ciku_Path = Path + os.sep + "词库" + os.sep


        self.jieba_dic = self.load_Userdict(ciku_Path + 'dict_jieba.txt')
        self.user_dic = self.load_Userdict(ciku_Path + 'title.txt')
        self.places = self.load_Userdict(ciku_Path + '中国风景名胜.txt')
        self.countries = self.load_Userdict(ciku_Path + '国家和地区词库.txt')
        self.stop_words = self.load_Userdict(ciku_Path + 'stop-words.txt')
        self.names = self.load_Userdict(ciku_Path + 'names.txt')

    def load_Userdict(self, path):
        """
        加载自定义词典,字典格式为  “关键字 词性”中间用一个空格隔开
        :param path:
        :return:返回字典格式的信息
        """
        with open(path, 'r', encoding='utf-8') as f:
            user_dic = f.read().splitlines()
            dic = {}
            for i in user_dic:
                line = i.split(' ')
                dic[line[0]] = line[1]
        return dic

    def get_time(self, title):
        """
        获取图片的拍摄时间
        :param title: 图片标题
        :return: 返回year,month,day
        """
        print('开始进行时间提取：{}'.format(title))
        year, month, day = None, None, None

        pattern = re.compile(r'(20\d{2}-\d{1,2}-\d{1,2})'  # 匹配 2020-4-5 和 2020-04-05 格式
                             r'|(20\d{2}年\d{1,2}月\d{1,2}'  # 匹配 2016年11月18日格式
                             r'|(20\d{2}(([0][0-9])|([1][0-2]))\d{1,2})'  # 匹配2016021 或 2016102 20161102格式
                             r'|(20\d{2}—\d{1,2}—\d{1,2}))', re.X)  # 匹配 2020—01—10 格式，此处连接符为中文破折号的一半
        try:
            time = re.search(pattern, title).group()
            print('时间：{}'.format(time))
            year = re.search(r'20\d{2}', time).group()  # 提取年份，以20开头
            month = re.search(r'\d{1,2}', time[4:]).group()  # 提取月份
            day = re.search(r'\d{1,2}', time[-2:]).group()  # 提取日期
        except Exception:
            pass

        # 此处处理只有年份的数据，只有年份时上面的匹配规则是无法生效的
        if year is None:
            try:
                year = re.search(r'20\d{2}', title).group()  # 匹配20开头的4位数的年份
            except Exception:
                pass

        # 考虑日期格式读取错误导致月份大于12（通常为连续读取两个年份如20102012），同时统计月份为空的数据
        if month is None or int(month) > 12:
            month, day = self.get_monthAndDay(title)

        time = year, month, day
        return time

    def get_monthAndDay(self, title):
        """
        第一轮读取时间失败后调用，在年份和日期中存在间隔时调用，如2012年xxxx，4月12日，5.15,只有月份信息的情况
        :param title: 照片标题字符串
        :return: month, day 返回月份和日期
        """
        month, day = None, None
        print("二次时间读取:{}".format(title))
        try:
            time = re.search(r'\d{1,2}月\d{1,2}', title).group()
            month = re.search(r'\d{1,2}', time).group()
            day = re.search(r'\d{1,2}', time[2:]).group()
            print('二次读取月份和日期；{}  {}'.format(month, day))
        except Exception:
            pass
        try:
            print('*' * 100)
            time = re.search(r'\d{1,2}\\\d{1,2}', r'' + title).group()
            print('此处time为：{}'.format(time))
            day = re.match(r'^\d{1,2}', time).group()
            month = re.search(r'\d{1,2}', time[2:]).group()
        except Exception:
            print("时间读取失败")
        try:
            time = re.search(r'\d{1,2}月', title).group()
            month = re.search(r'\d{1,2}', time).group()
        except Exception:
            print("时间读取失败")

        # Z:\yuexun\2017年外拍\闫珅\文博会911—JPG\闫珅—文博会911—JPG (973).jpg --> 00012159.jpg  这个日期无法提取，在此处手动添加
        if '文博会' in title:
            month = 9
            day = 11

        return month, day


    def get_keyWords_byCut(self, title, seg):
        """
        获取关键字
        :param title: 图片标题
        :param name: 将作者姓名传入，作为停用词词表
        :return: 返回关键字列表
        """

        # 添加自定义词典
        jieba_dic, user_dic, locals, countries, stop_words, name_list = self.jieba_dic, self.user_dic, self.places, self.countries, self.stop_words, self.names
        print("开始对信息进行处理:{}".format(title))
        loc = []  # 拍摄地点
        names = None  # 摄影师姓名
        nationality = None  # 摄影师国籍
        key_words = []  # 关键字列表
        rule = ['ns', 'nt', 'nz', 'f', 'i', 'l', 'j', 'vn', 'n', 'Ng', 'nr', 'z']
        # 分词

        # words = jieba.cut(title)
        words = seg.run(title)

        word2 = [i for i in words if i not in stop_words]
        names = [i for i in word2 if i in name_list.keys()]  # 摄影师名
        nationality = [i for i in word2 if i in countries.keys()]  # 摄影师国籍
        loc = [i for i in word2 if i in locals.keys() and len(i) > 1]  # 地点名
        other = [i for i in word2 if i in jieba_dic.keys() and jieba_dic[i] in rule]
        loc = loc + [i for i in other if jieba_dic[i] == 'ns' and i not in nationality]
        key_words = [i for i in other if jieba_dic[i] != 'ns' and i not in name_list and len(i) > 1]
        # key_words = key_words + [i for i in word2 if i in user_dic.keys() and user_dic[i] in rule]

        loc = list(set(loc))
        print("\n地点：{}".format(loc))
        names = list(set(names))
        if len(names) > 0:
            names = names[0]
        else:
            names = None
        print("摄影师：{}".format(names))
        nationality = list(set(nationality))
        if len(nationality) > 0:  # 去除列表
            nationality = nationality[0]
        else:
            nationality = None
        print("摄影师国籍：{}".format(nationality))
        key_words = list(set(key_words))
        print("关键字：{}".format(key_words))

        return loc, key_words, names, nationality

    def get_data(self, line, seg):
        """
        读取照片标题集合的文件，进行处理
        :param line: 图片标题信息
        :return:result_output 返回每个标题提取出的信息列表
        """
        # 输出结果
        result_output = []
        # 定义字典存放每一个标题提取中的数据
        pic = {}

        # 获取年月日
        year, month, day = self.get_time(r'' + line[:-18:].replace('.', '-').replace(' ', ''))
        loc, keyWords, name, nationality = self.get_keyWords_byCut(line, seg)
        # 去除空格和连接符
        line = line.replace(' ', '').replace('-', '')
        number = line[-13::].strip('\n')  # 图片编号

        # 将图片标题分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
        title_list = line[:-18:].split('\\')
        tag_1 = title_list[2]  # 一级标签，作品来源

        print('提取出的年月日：{}  {}  {}'.format(year, month, day))

        # 获取拍摄地、关键事件名、摄影师名、摄影师国籍
        # loc, keyWords, name, nationality = self.get_keyWords_byCut(''.join(title_list[3:]))
        pic[number] = [tag_1, year, month, day, name, nationality, loc, keyWords]
        result_output.append(pic)

        print('-' * 100)
        return result_output

    def write_to_file(self, result_output, result_path):
        print(result_output)
        with open(result_path, 'w', encoding='utf-8') as f:
            for pics in result_output[0]:
                for pic in pics:
                    for key, value in pic.items():
                        f.write('{}\t'.format(key))
                        for i in value:
                            f.write('{}\t'.format(i))
                        f.write('\n')

    def multiprocess(self, listDirs, result_path):
        with open(listDirs, 'r', encoding='utf-8') as file:
            content = file.readlines()
        from multiprocessing.dummy import Pool as ThreadPool

        result_output = []
        pool = ThreadPool()
        result_output.append(pool.map(self.get_data, content))
        pool.close()
        pool.join()
        self.write_to_file(result_output, result_path)

    @timmer
    def singleprocess(self, listDirs, result_path):
        with open(listDirs, 'r', encoding='utf-8') as file:
            content = file.readlines()
        result_output = []
        from LAC import LAC
        seg = LAC(mode='seg')
        for line in content:
            result_output.append(self.get_data(line, seg))

        self.write_to_file([result_output], result_path)


if __name__ == '__main__':
    start_time = time.time()

    old = sys.stdout  # 将当前系统输出储存到一个临时变量中
    f = open('output_class.txt', 'w', encoding='utf-8')

    sys.stdout = f  # 输出重定向到文件

    Path = os.path.dirname(os.getcwd())
    dataPath = Path + os.sep + 'data'
    listDirs = os.path.join(dataPath, 'renommelog.txt')
    result = os.path.join(dataPath, 'result_test.txt')
    pic = pic_classify(listDirs, result)

    pic.singleprocess(listDirs, result)  # 单进程，方便观察输出结果
    # pic.multiprocess(listDirs, result) #多进程模式

    sys.stdout = old  # 还原原系统输出
    f.close()

    end_time = time.time()

    run_time = round(end_time - start_time, 5)
    print('运行时间为：{}'.format(run_time))
