#! /usr/bin/env python
# coding:utf-8
import numpy as np
import cv2

def ColorConstancy(img_file):
    img = cv2.imread(img_file)
    # ガンマ補正
    gamma = 2.2
    look_up_table = np.ones((256, 1), dtype = 'uint8' ) * 0
    for i in range(256):
        look_up_table[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)
    img = cv2.LUT(img, look_up_table)
    # カラー補正
    img_p3 = np.power(img.astype(np.float32), 3)
    rgb_vec = np.power(np.mean(img_p3, (0, 1)), 1.0/3.0)
    rgb_norm = np.sqrt(np.mean(np.power(rgb_vec, 2.0)))
    rgb_vec = rgb_vec / rgb_norm
    rgb_vec = 1.0 / rgb_vec
    img = np.multiply(img.astype(np.float32), rgb_vec)
    return img.astype(np.uint8)

if __name__ == '__main__':
    cv2.imwrite('ISIC_0012221_adjusted.jpg', ColorConstancy('ISIC_0012221.jpg'))
    cv2.imwrite('ISIC_0012222_adjusted.jpg', ColorConstancy('ISIC_0012222.jpg'))
