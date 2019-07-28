#!/usr/local/bin/python3
#_*_ coding: utf-8 _*__

import numpy as np
import chainer
import glob
import random
import matplotlib.pyplot as plt
from PIL import Image
from chainer import cuda, Function, \
	report, training, utils, Variable
from chainer import datasets, iterators, optimizers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
import chainer.serializers as S
from chainer.training import extensions
from chainer.datasets import LabeledImageDataset
from chainer.datasets import TransformDataset
from chainer.training import extensions
from chainer.datasets import tuple_dataset
import datetime

class MyChain(Chain):
	def __init__(self):
		super(MyChain, self).__init__(
			cn1 = L.Convolution2D(3, 16, 5, pad=2),
			cn2 = L.Convolution2D(16, 32, 5,pad=2),
			l1 = L.Linear(None, 500),
			l2 = L.Linear(None, 3),
		)

	def __call__(self, x, t):
		return F.softmax_cross_entropy(self.fwd(x), t)

	def fwd(self, x):

		h1 = F.max_pooling_2d(F.relu(self.cn1(x)), 2)
		h2 = F.max_pooling_2d(F.relu(self.cn2(h1)), 2)
		h3 = F.dropout(F.relu(self.l1(h2)))
		return self.l2(h3)

def rgb_split(img):
	img = img.resize((50, 50))
	r,g,b = img.split()
	rImgData = np.asarray(np.float32(r) / 255)
	gImgData = np.asarray(np.float32(g) / 255)
	bImgData = np.asarray(np.float32(b) / 255)

	imgData = np.asarray([rImgData, gImgData, bImgData])
	return imgData


dt_st = datetime.datetime.now()

model = MyChain()
chainer.serializers.load_npz('check_soy.net', model)

img_dir = "./test.jpg"

img = Image.open(img_dir)

split_data = rgb_split(img)

img_arr = []
class_id = []

img_arr.append(split_data)
class_id.append(0)

test = tuple_dataset.TupleDataset(img_arr, class_id)

x = Variable(np.array([test[0][0]], dtype=np.float32))

result = model.fwd(x)	#画像をモデルに通す

classifier = np.argmax(result.data)		#一番大きいものをクラスと識別する

print(classifier)
