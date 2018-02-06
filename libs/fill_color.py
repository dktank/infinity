# coding:utf-8


import random

import numpy as np

import skimage
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb
import cv2


def fill_color_ski(src, tar, config=None):
    img = data.imread(src, 1)
    thresh = threshold_otsu(img)
    bw = closing(img > thresh, square(1))

    cleared = bw.copy()
    clear_border(cleared)

    label_image = label(cleared)
    borders = np.logical_xor(bw, cleared)

    label_image[borders] = -1
    colors = np.random.rand(300, 3)
    background = np.random.rand(3)
    image_label_overlay = label2rgb(label_image, image=img, colors=colors, bg_color=background)
    output = image_label_overlay * 255

    cv2.imwrite(tar, output)


def fill_color_cv2(src, tar, config=None ):
    # cv2 读取文件
    original = cv2.imread(src)
    output = original.copy()

    # 转灰度图
    bgr2gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)  # 转灰度图

    # 二值化
    ret, threshold = cv2.threshold(bgr2gray, 170, 255, cv2.THRESH_BINARY)

    # 01化
    bitwise_not = cv2.bitwise_not(threshold)

    # 检测轮廓
    image, cnts, hierarchy = cv2.findContours(bitwise_not, cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_NONE)
    # cv2.CHAIN_APPROX_SIMPLE)

    # (bitwise_not, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for cnt in cnts:
        # 上色
        color = cv2.cvtColor(
            np.uint8([[[random.randint(0, 170), random.randint(150, 250), random.randint(150, 255)]]]),
            cv2.COLOR_HSV2BGR)[0, 0]

        cv2.drawContours(output, [cnt], 0, [int(i) for i in color], -1)

    cv2.imwrite(tar, output)

