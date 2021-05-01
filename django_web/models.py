import collections
from itertools import count

import mongoengine
from django.db import models
from mongoengine import *
from django.db.models import *
#----------测试用models能读取数据库----------#
from mongoengine import connect
connect('bilibili',host='192.168.228.100',port=27017)
#----------测试用models能读取数据库----------#
# Create your models here.

class videoInfo(Document):
    aid = StringField()
    pubdate = StringField()
    view = StringField()
    like = StringField()
    danmaku = StringField()
    reply = StringField()
    favorite = StringField()
    coin = StringField()
    share = StringField()
    meta = {'collection':'b_video_stat_20210501'}

class replyInfo(Document):
    oid = StringField()
    rpid = StringField()
    uname = StringField()
    mid = StringField()
    message = StringField()
    meta = {'collection': 'b_video_reply_20210501'}


