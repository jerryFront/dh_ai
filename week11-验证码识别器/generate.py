"""
生成验证码图片
"""

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from captcha.image import ImageCaptcha
import os
from utils import init_dir


def generate_captcha(total, captcha_length, width, height, characters, dist_dir):
    """
    生成验证码图片
    :param total: 生成验证码图片的数量
    :param captcha_length: 验证码长度
    :param width: 图片宽度
    :param height: 图片高度
    :param characters: 验证码字符集
    """
    init_dir(dist_dir, remove=True)

    for i in range(total):
        # 生成验证码
        chars = ''.join(map(str, random.choices(characters, k=captcha_length)))
        # 生成验证码图片
        captcha = ImageCaptcha(width=width, height=height)
        img = captcha.generate_image(chars)
        img.save(os.path.join(dist_dir, f'{chars}_{i}.png'))
        print(f'generate captcha {i}')


if __name__ == '__main__':
    generate_captcha(total=10000, captcha_length=4, width=200,
                     height=100, characters=string.digits, dist_dir='./data/train')
    generate_captcha(total=1000, captcha_length=4, width=200,
                     height=100, characters=string.digits, dist_dir='./data/test')
