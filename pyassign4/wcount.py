#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Wang Yanze"
__pkuid__  = "1800011721"
__email__  = "1800011721@pku.edu.cn"
"""


import sys
import urllib.error
from urllib.request import urlopen


def check(my_str):
    """
    对字符进行检查，如果切片后的字符存在标点，则去除标点。
    return： 修正后的字符串
    """
    punctuation = [r'\n', ',', ';', '.', '?', ':', '!', '"', '&', '*', '_', '(', ')', '[', ']', '#', '@', '$', '"']
    for each in punctuation:
        my_str = my_str.replace(each, '')
    return my_str


def addiction(line, my_dict):
    """
    针对每一行进行检查计数。将所有的标点去除，并将大写字母改为小写字母
    return: 无返回值
    """

    def addi(item, ciku):
        if item in ciku:
            ciku[item] += 1
        else:
            ciku[item] = 1
        return ciku

    for word in line.split():
        word = check(word)
        if '--' in word:
            for sub in word.split('--'):
                my_dict = addi(sub.lower(), my_dict)
        else:
            my_dict = addi(word.lower(), my_dict)
    return my_dict


def top_n(argv):
    """
    获取用户给出的top_n参数，并判断合法性
    :return: 返回合法的参数
    """
    try:
        number = int(argv)
    except ValueError:
        print('无法执行！')
        number = 0
    while not isinstance(number, int) or number <= 0:
        try:
            number = int(input('您输入的数值不符合规则，请重新输入一个正整数!（不需要再次输入网址！）'))
        except ValueError:
            print('无法执行！')
    return number


def print_words(word_list, topn):
    '''
    打印所得到的列表中的单词和单词的个数
    '''
    print('\n', '单词：'.center(8), '出现次数：'.center(8), '\n')
    for (word, num) in word_list[0:topn]:
        print(word.center(10), str(num).center(15))
    print('\n打印完毕！')
    return


def wcount(my_dict, topn=10):
    """count words from lines of text string, then sort by their counts
       in reverse order, output the topn (word count), each in one line.
       """
    result = sorted(my_dict.items(), key=lambda each: each[1], reverse=True)
    print_words(result, min(topn, len(result)))
    return


def main():
    """
    实现单词的统计，同时检测了输入的合法性，对网络异常和输入的合法性做出了初步的判断
    """
    global repository

    try:
        with urlopen(sys.argv[1]) as target:
            text = target.read().decode()
            while text:
                repository = addiction(text, repository)
                text = target.readline().decode()
    except urllib.error.URLError as err:
        print('出错啦！(URLError)：无法访问此网站,({})'.format(err))
        print('''
    您可以尝试一下方案：
        1. 请检查网络是否正常连接；
        2. 请检查输入网址是否正确；
        3. 如果有网线，请检查网线是否插好；
        4. 请检查代理服务器或防火墙设置！
        5. 请检查您的输入格式是否有误，请不要将数字直接输入在网址后面，需要空格隔开！
    
    检查后，请重新使用命令行完成任务！
        ''')

    except ValueError as err:
        print('出错啦！(ValueError):', err)
        print('请输入正确格式类型的网址！')
    except TimeoutError as err:
        print('出错啦！(TimeoutError):', err)
        print('运行超时，请检查网址是否正确！')

    except:
        print('出现了未知错误……')

    else:
        try:
            wcount(repository, top_n(sys.argv[2]))
        except IndexError:
            wcount(repository)

    return


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print(' topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    repository = {}
    main()



