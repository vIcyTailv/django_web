import wordcloud
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from splitSentence import get_message
import random

# 测试用
test_oid_list = [460363247, 460363248]


def generate_pic(oid_list):
    text = get_message(oid_list)
    # 读取mask图
    mask_image = Image.open('./Mask_IMG/{}'.format('pre_picture.png'))
    mask = np.array(mask_image)
    # 设置词云图对象属性, 添加中文字体文件
    wc = wordcloud.WordCloud(font_path='./HGDH2_CNKI.TTF', max_words=2000, mask=mask, height=1200, width=1200, background_color=None,
                             repeat=False, mode='RGBA', min_font_size=4)
    # 生成词云图
    wc.generate(text)

    # store default colored image
    default_colors = wc.to_array()
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
               interpolation="bilinear")

    # 存储词云图
    wc.to_file('../static/images/after_picture.png')


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


generate_pic(test_oid_list)
