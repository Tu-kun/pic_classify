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

# d_order = [('月讯爱国主义', 6), ('爱国主义', 4), ('教育', 2), ('月讯', 2)]
d_order = ['月讯爱国主义', '爱国主义', '教育', '月讯']
# result = []
# result.append(d_order[0])
# key_words = [('月讯爱国主义', 6), ('爱国主义', 4), ('教育', 2), ('月讯', 2)]
result = []
result.append(d_order[0])

for index in range(len(d_order)-1, -1, -1):
    print('index:{}'.format(index))
    print(d_order[:index])
    flag = 0 # 当这个元素不在其他元素中时标志加一，
    for j in d_order[:index]:
        print("*"*100)
        # print(d_order[index])
        if d_order[index] not in j:
            print('{}不在{}中'.format(d_order[index], j))
            flag += 1  # 当这个元素不在其他元素中时标志加一
            print('d_order的标志:{}'.format(flag))
            continue
        else:
            print('{}在{}中'.format(d_order[index], j))
            print('d_order的标志:{}'.format(flag))
            continue
    print('{}的flag为{}'.format(d_order[index], flag))
    print('index：{}'.format(index))
    if flag == index:
        result.append(d_order[index])
        print('{}添加到result中'.format(d_order[index]))
print(list(set(result)))
# key_words = ['月讯爱国主义', '爱国主义', '教育', '月讯']

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
