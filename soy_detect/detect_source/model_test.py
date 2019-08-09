"""
画像(固定のファイル名)を分類器に通す
.cgiと異なり、関数を提供し外部から呼び出される
"""
import numpy as np
import chainer
import matplotlib.pyplot as plt
from PIL import Image
from chainer import Variable
from chainer import datasets
#from chainer import Link, Chain, ChainList
from chainer.datasets import tuple_dataset
import sys
sys.path.append("..")
from train_source import train_model

def rgb_split(img):
	img = img.resize((50, 50))
	r,g,b = img.split()
	rImgData = np.asarray(np.float32(r) / 255)
	gImgData = np.asarray(np.float32(g) / 255)
	bImgData = np.asarray(np.float32(b) / 255)

	imgData = np.asarray([rImgData, gImgData, bImgData])
	return imgData

#別ファイルから呼ばれて識別結果を返す処理
def start_test_model():

	model = train_model.MyChain()
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

	return classifier
