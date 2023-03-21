# coding: utf-8
import sys, os

sys.path.append(os.pardir)  # 追加父级路径，这个技巧有用 在当前目录执行比较有用
import numpy as np
# 如果不是当前目录执行，需要设置python_path
from dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)  # 5

print(img.shape)  # (784,) flatten 会将数据读取为一个列向量
img = img.reshape(28, 28)  # 重新将新装读取为28x28
print(img.shape)  # (28, 28)

img_show(img)