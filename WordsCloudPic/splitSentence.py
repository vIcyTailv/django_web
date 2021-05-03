import jieba
import re
from django_web import models
from django_web.models import ReplyInfo
from mongoengine import connect

connect('bilibili', host='192.168.228.100', port=27017)


# 获取停用词
def stopword_list():
    stop_word = []
    fd = open("stopwords.txt", "r", encoding='utf-8')
    for line in fd.readlines():
        stop_word += str(line).strip('\n').split(',')
        fd.close()
    # print(stop_word)
    return stop_word


# 匹配Unicode编码，并对照分词stopword文档进行分词
pattern = re.compile(r'[\u4e00-\u9fa5]')


# 将需要分词的句子列表list从参数导入
def split(reply_list):
    seg_list = ''
    # 设置自定义词库
    jieba.load_userdict('./userdict.txt')
    # 分词、去除停用词，导出有意义短语的列表seg_list
    for i in range(len(reply_list)):
        words_list = jieba.cut(reply_list[i], cut_all=False)
        # 遇到停用词，用' '替换
        for i in words_list:
            if pattern.match(i) and i not in stopword_list():
                seg_list += i
                seg_list += ' '
    return seg_list


def get_message(oid_list):
    # oid = 460363247
    reply_list = []
    for oid_ in oid_list:
        reply_info = ReplyInfo.objects.all()
        for i in reply_info:
            reply_list.append(i.message)
        phrase_list = split(reply_list)
        # print(phrase_list)
    return phrase_list
