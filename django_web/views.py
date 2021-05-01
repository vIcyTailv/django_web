import configparser
from django.db.models import Sum
from django.shortcuts import render
from django_web.models import videoInfo


# Create your views here.

def scanboard(request):
    videos_info = videoInfo.objects.all()
    all_view = 0
    all_like = 0
    all_danmaku = 0
    all_reply = 0
    all_favorite = 0
    all_coin = 0
    all_share = 0
    for i in videos_info:
        all_view = all_view + i.view
        all_danmaku = all_danmaku + i.danmaku
        all_like = all_like + i.like
        all_reply = all_reply + i.reply
        all_favorite = all_favorite + i.favorite
        all_coin = all_coin + i.coin
        all_share = all_share + i.share
    context = {
        'all_video_num': len(videos_info),
        'all_view_num': all_view,
        'all_danmaku_num': all_danmaku,
        'all_reply_num': all_reply,
        'all_favorite_num': all_favorite,
        'all_coin_num': all_coin,
        'all_share_num': all_share,
    }

    return render(request, 'scanboard.html', context)


def index(request):
    return render(request, 'index.html')
