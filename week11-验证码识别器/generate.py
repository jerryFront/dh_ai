"""
生成验证码图片
"""

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from captcha.image import ImageCaptcha
import os
from utils import init_dir


def generate_captcha(total, captcha_length, width, height, char_set, dist_dir):
    """
    生成验证码图片
    :param total: 生成验证码图片的数量
    :param captcha_length: 验证码长度
    :param width: 图片宽度
    :param height: 图片高度
    :param char_set: 验证码字符集
    """
    init_dir(dist_dir, remove=True)

    for i in range(total):
        # 生成验证码
        chars = ''.join(map(str, random.choices(char_set, k=captcha_length)))
        # 生成验证码图片
        captcha = ImageCaptcha(width=width, height=height)
        img = captcha.generate_image(chars)
        captcha.create_noise_dots(img, '#000000', 4, 40)  # type: ignore
        captcha.create_noise_curve(img, '#000000')  # type: ignore
        img.save(os.path.join(dist_dir, f'{chars}_{i}.png'))
        print(f'generate captcha {i}')


if __name__ == '__main__':
    generate_captcha(total=2000, captcha_length=1, width=200,
                     height=100, char_set=string.digits, dist_dir='./data/train')
    generate_captcha(total=1000, captcha_length=1, width=200,
                     height=100, char_set=string.digits, dist_dir='./data/test')
