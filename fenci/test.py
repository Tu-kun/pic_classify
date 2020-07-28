# import re
#
# d = {'2019年': ['TIME'], '魏建国': ['PER'], '2018.12月': ['TIME'], '北京月讯杂志社': ['ORG'], '289张': ['m'], '（': ['w'],
#      '20172018年': ['TIME'], '拍摄': ['v'], '）': ['w'], '287张': ['m'], '故宫': ['LOC'], '角楼': ['n'], '2': ['m']}
#
# # for i in d:
# #     if d[i] == ['LOC']:
# #         print(i)
# #
# # loc = [i for i in d if d[i] == ['LOC']]
# # print(loc)
#
# # stop_words = ['拍摄', '2019年']
# # d = {k:v for k, v in d.items() if k not in stop_words}
# # print(d)
#
#
# title = r'''永通桥、御碑修15张\_DSC1206.jpg
#         通州张家湾城墙、通运乔修12张
#         周世杰-20181025炫彩世界开幕式\DSCF4551-JPG
#         乔治･多帕斯-希腊-20150521-国子监.jpg
#         佩德罗·阿巴斯卡尔-古巴-20150519-雁栖湖会议中心道路.jpg
#         佩德罗·阿巴斯卡尔-古巴-20150523-中国科技馆.jpg
#         李晓尹-中国-2016年11月18日-美丽乡村顺义马坡镇南卷村7.jpg
#         李晓尹-中国-2016年1月14日-游客在王府井猴子造型前合影留念.'''
# title = r'修雨辰 2017年5月15日 一带一路峰会 修雨辰 中国 2017年5月12日 5月15日 一带一路峰会工作照 修雨辰 中国 2017年5月12日 5月15日 一带一路峰会 (38).' \
#         r'张鑫 2017—05— 11、 12 、13 、14、 一带一路 国家会议中心 2017—05—11 一带一路 国家会议中心 张鑫—2017—05—11 一带一路 国家会议中心 (103).JPG  '
#
# from LAC import LAC
# seg = LAC(mode='seg')
# seg_result =seg.run(title)
# print('seg结果:{}'.format(seg_result))
#
# lac = LAC(mode='lac')
# lac_result = lac.run(title)
# d = {k: v for k, *v in zip(*lac_result)}  #将结果转化为字典
# print('lac结果:{}'.format(d))
# loc = [i for i in d if d[i] == ['LOC']]  # 摄影地点
# print('地点：{}'.format(loc))


# # '''
# # E:\tu\pycharmWorkplace\lac\venv\Scripts\python.exe E:/tu/pycharmWorkplace/lac/fenci/test.py
# # seg结果:['周世杰', '-', '20181025', '炫彩', '世界', '开幕式', '\\', 'DSCF4551', '-', 'JPG', "'", ' ', '\n        乔治･多帕斯', '-', '希腊', '-', '20150521', '-', '国子监', '.', 'jpg\n        ', '佩德罗·阿巴斯卡尔', '-', '古巴', '-', '20150519', '-', '雁栖湖会议中心', '道路', '.', 'jpg\n        ', '佩德罗·阿巴斯卡尔', '-', '古巴', '-', '20150523', '-', '中国科技馆', '.', 'jpg', ' ', '\n        ', '李晓尹', '-', '中国', '-', '2016年11月18日', '-', '美丽乡村', '顺义', '马坡镇', '南卷村', '7.jpg\n        ', '李晓尹', '-', '中国', '-', '2016年1月14日', '-', '游客', '在', '王府井', '猴子', '造型', '前', '合影留念', '.']
# # ["'周世杰'", "'炫彩'", "'世界'", "'开幕式'", "'希腊'", "'国子监'", "'古巴'", "'雁栖湖会议中心'", "'道路'", "'古巴'", "'中国科技馆'", "'李晓尹'", "'中国'", "'美丽乡村'", "'顺义'", "'马坡镇'", "'南卷村'", "'李晓尹'", "'中国'", "'游客'", "'在'", "'王府井'", "'猴子'", "'造型'", "'前'", "'合影留念'"]
# # lac结果:[['[', '"', "'", '周世杰', "'", '"', ',', ' ', '"', "'", '炫彩', "'", '"', ',', ' ', '"', "'", '世界', "'", '"', ',', ' ', '"', "'", '开幕式', "'", '"', ',', ' ', '"', "'", '希腊', "'", '"', ',', ' ', '"', "'", '国子监', "'", '"', ',', ' ', '"', "'", '古巴', "'", '"', ',', ' ', '"', "'", '雁栖湖', '会议', '中心', "'", '"', ',', ' ', '"', "'", '道路', "'", '"', ',', ' ', '"', "'", '古巴', "'", '"', ',', ' ', '"', "'", '中国科技馆', "'", '"', ',', ' ', '"', "'", '李晓尹', "'", '"', ',', ' ', '"', "'", '中国', "'", '"', ',', ' ', '"', "'", '美丽乡村', "'", '"', ',', ' ', '"', "'", '顺义', "'", '"', ',', ' ', '"', "'", '马坡镇', "'", '"', ',', ' ', '"', "'", '南卷村', "'", '"', ',', ' ', '"', "'", '李晓尹', "'", '"', ',', ' ', '"', "'", '中国', "'", '"', ',', ' ', '"', "'", '游客', "'", '"', ',', ' ', '"', "'", '在', "'", '"', ',', ' ', '"', "'", '王府井', "'", '"', ',', ' ', '"', "'", '猴子', "'", '"', ',', ' ', '"', "'", '造型', "'", '"', ',', ' ', '"', "'", '前', "'", '"', ',', ' ', '"', "'", '合影留念', "'", '"', ']'], ['w', 'w', 'w', 'PER', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'ORG', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'n', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'ORG', 'w', 'w', 'w', 'w', 'w', 'w', 'PER', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'PER', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'p', 'w', 'w', 'w', 'w', 'w', 'w', 'LOC', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'f', 'w', 'w', 'w', 'w', 'w', 'w', 'v', 'w', 'w', 'w']]
# #
# # Process finished with exit code 0
# # '''

# for s in sss:
#      print(s)
#      tmp = sss.remove("'"+ s+"'")
#      print(tmp)
#      break
     # for i in tmp:
     #      if s not in i:
     #           ss.append(s)
# for index, value in enumerate(sss):
#      tmp = sss
#      tmp.pop(index)
#      print(tmp)
#      for v in tmp:
#           if value not in v:
#                ss.append(value)
# print(list(set(ss)))

#  去重
# d_order = [('月讯爱国主义', 6), ('爱国主义', 4), ('教育', 2), ('月讯', 2)]
d_order = ['月讯爱国主义', '爱国主义', '教育', '月讯']
# result = []
# result.append(d_order[0])
# key_words = [('月讯爱国主义', 6), ('爱国主义', 4), ('教育', 2), ('月讯', 2)]
# result = []
# result.append(d_order[0])
#
# for index in range(len(d_order)-1, -1, -1):
#     print('index:{}'.format(index))
#     print(d_order[:index])
#     flag = 0 # 当这个元素不在其他元素中时标志加一，
#     for j in d_order[:index]:
#         print("*"*100)
#         # print(d_order[index])
#         if d_order[index] not in j:
#             print('{}不在{}中'.format(d_order[index], j))
#             flag += 1  # 当这个元素不在其他元素中时标志加一
#             print('d_order的标志:{}'.format(flag))
#             continue
#         else:
#             print('{}在{}中'.format(d_order[index], j))
#             print('d_order的标志:{}'.format(flag))
#             continue
#     print('{}的flag为{}'.format(d_order[index], flag))
#     print('index：{}'.format(index))
#     if flag == index:
#         result.append(d_order[index])
#         print('{}添加到result中'.format(d_order[index]))
# print(list(set(result)))
# key_words = ['月讯爱国主义', '爱国主义', '教育', '月讯']

#   相似度计算
# import difflib
#
#
# def string_similar(s1, s2):
#     return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
#
# str1 = r'yury-维利查卡•尤里\IMG_9511-20160524-美院-维利查卡•尤里.jpg --> 00007409.jpg'
#
# str2 = r'yury-维利查卡•尤里\IMG_9525-20160524-电影博物馆-维利查卡•尤里.jpg --> 00007410.jpg'
# print(string_similar(str1, str2))
#
# b = 2
# a = b
# a = 1
# print('a:{} b:{}'.format(a, b))

# import logging
# # logger = logging.getLogger()
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# # logger.setLevel(logging.DEBUG)
#
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')
import re
class get_time():
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

        if not month is None and len(str(month)) == 1:
            month = '0' + str(month)

        time = year, month, day
        return time


    def get_monthAndDay(self, title):
        """
        第一轮读取时间失败后调用，在年份和日期中存在间隔时调用，如2012年xxxx，4月12日，5.15,只有月份信息的情况
        :param title: 照片标题字符串
        :return: month, day 返回月份和日期
        """
        month, day = None, None
        # print("二次时间读取:{}".format(title))
        try:
            time = re.search(r'\d{1,2}月\d{1,2}', title).group()
            month = re.search(r'\d{1,2}', time).group()
            day = re.search(r'\d{1,2}', time[2:]).group()
            # print('二次读取月份和日期；{}  {}'.format(month, day))
        except Exception:
            pass
        try:
            time = re.search(r'\d{1,2}\\\d{1,2}', r'' + title).group()
            # print('此处time为：{}'.format(time))
            day = re.match(r'^\d{1,2}', time).group()
            month = re.search(r'\d{1,2}', time[2:]).group()
        except Exception:
            try:
                time = re.search(r'\d{1,2}月', title).group()
                month = re.search(r'\d{1,2}', time).group()
            except Exception:
                print("时间读取失败2")

        if month is None or int(month) > 12:
            month, day = None, None

        # Z:\yuexun\2017年外拍\闫珅\文博会911—JPG\闫珅—文博会911—JPG (973).jpg --> 00012159.jpg  这个日期无法提取，在此处手动添加
        if '文博会' in title:
            month = 9
            day = 11

        return month, day

cla = get_time()
title = '2020年4月5日 20200106 20201402'
cla.get_time(title)
title = '20200106'
cla.get_time(title)
title = '4月2日'
cla.get_time(title)