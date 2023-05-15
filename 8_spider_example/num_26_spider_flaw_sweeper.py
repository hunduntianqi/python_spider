"""
    爬虫实现单词错题本
"""
import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
res1 = requests.get(url, headers=headers)
json_res1 = res1.json()
choice = json_res1['data']
print(choice)
num_dict = {}
link_dict = {}
z = 0
for i in choice:
    print('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=' + i[0], i[1])
    link_dict[i[1]] = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=' + i[0]
    print(z)
    num_dict[z] = [i[1]]
    print(num_dict)
    z += 1
print(num_dict)
print(link_dict)
grade0 = int(input('请输入要测试的等级(0.GMAT,1.考研,2.高考,3.四级,4.六级,5.英专,6.托福,7.GRE,8.雅思,9.任意)：'))
print(num_dict[grade0][0])
word_test = requests.get(link_dict[num_dict[grade0][0]])
print(word_test)
print(word_test.json()['data'])
data = word_test.json()['data']
word_list = []
judg_list = {}
for j in word_test.json()['data']:
    print(j['content'])
    word_list.append(j['content'])
    print(j['pk'])
    judg_list[j['content']] = j['pk']
print(word_list)
print(judg_list)
user_yes_list = []
user_no_list = []
for judg in range(len(word_list)):
    print()
    user_choice = input('第{}个单词 {} 你是否认识?请输入1 or Enter\n'.format(judg + 1, word_list[judg]))
    print()
    if user_choice == '1':
        user_yes_list.append(word_list[judg])
    else:
        user_no_list.append(word_list[judg])
print('你不认识的单词有：' + str(len(user_no_list)) + '个', '\n', user_no_list, '\n',
      '你认识的单词有：' + str(len(user_yes_list)) + '个',
      '\n', user_yes_list)
hold_list = []
nohold_list = []
userchoice_dict = {}
xuanze = []
for words in data:
    danci = words['content']
    if danci in user_yes_list:
        print(danci + ' 是什么意思？请选择:')
        right = judg_list[danci]
        xuanze = words['definition_choices']
        A1 = xuanze[0]['definition']
        userchoice_dict['A'] = xuanze[0]['pk']
        B1 = xuanze[1]['definition']
        userchoice_dict['B'] = xuanze[1]['pk']
        C1 = xuanze[2]['definition']
        userchoice_dict['C'] = xuanze[2]['pk']
        D1 = xuanze[3]['definition']
        userchoice_dict['D'] = xuanze[3]['pk']
        E1 = '不认识'
        userchoice_dict['E'] = '不认识'
        print(' A.' + A1, '\n', 'B.' + B1, '\n', 'C.' + C1, '\n', 'D.' + D1, '\n', 'E.' + E1)
        userchoice = input()
        if userchoice_dict[userchoice] == right:
            hold_list.append(danci)
        else:
            nohold_list.append(danci)
print('50个单词中,不认识的个数为:' + str(len(user_no_list)) + '个', '\n',
      '认识的单词个数为：' + str(len(user_yes_list)) + '个', '\n')
print('认识的单词中，完全掌握的有' + str(len(hold_list)) + '个', '\n', '还没有掌握的有' + str(len(nohold_list)) + '个',
      '\n')
print('不认识的单词是:', user_no_list, '\n', '认识未掌握的单词是:', nohold_list)
cuotiji = input('是否打印错题集?请输入Y或N:')
if cuotiji == 'Y' or cuotiji == 'y':
    wb = openpyxl.Workbook()
    sheet1 = wb.active
    sheet1.title = '不认识单词'
    sheet1['A1'] = '不认识单词'
    sheet2 = wb.active
    sheet2.title = '未掌握单词'
    sheet2['A1'] = '未掌握单词'
    for no in user_no_list:
        sheet1.append([no])
    for nohold in nohold_list:
        sheet2.append([nohold])
    wb.save('CUOTIJI.xlsx')
else:
    print('再见')
