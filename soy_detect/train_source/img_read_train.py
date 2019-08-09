"""
教師データの画像で学習させるプログラム
モデルは外部ファイルに定義
"""

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
import codecs
import sys
import train_model	#作成したモデルを読み込む

"""
画像セットを直接読み込む
引数にバッチサイズ、エポック数を入力する
"""

batch = 5
epoch = 10

args = sys.argv

if len(args) < 2:
	print("バッチサイズとエポック数を入力してください")
	print("ex: 「python ファイル 50 100」")
	exit()
else:
	batch = int(args[1])
	epoch = int(args[2])

train_dir = "./trans_data/"

imageData = []	#教師データの画像側の配列


labelData = []	#教師データのラベル側の配列

#jpg画像を並べ替える処理
def rgb_split(img):
	r,g,b = img.split()
	rImgData = np.asarray(np.float32(r) / 255)
	gImgData = np.asarray(np.float32(g) / 255)
	bImgData = np.asarray(np.float32(b) / 255)

	imgData = np.asarray([rImgData, gImgData, bImgData])
	return imgData

#元データから画像とクラスの変数に統合する処理
def load_train_data():
	list = glob.glob(train_dir + "*")

	random.shuffle(list)

	for i in list:
		name = i[13:]
		class_id = i[20:21]
		img_src = Image.open(train_dir + name)
		split_data = rgb_split(img_src)
		imageData.append(split_data)
		labelData.append(np.int32(class_id))

load_train_data()
valid_data_idx = np.int32(len(imageData) * 0.9)	#10%を確認用のデータに分ける

train = tuple_dataset.TupleDataset(imageData[0:valid_data_idx], labelData[0:valid_data_idx])
test = tuple_dataset.TupleDataset(imageData[valid_data_idx:], labelData[valid_data_idx:])

print("データ設定")

model = train_model.MyChain()				#モデルのインスタンスつくる
optimizer = optimizers.Adam()	#最適化するアルゴリズムの選択	SGD:確率的勾配降下法
optimizer.setup(model)			#モデルをアルゴリズムにセットする
iterator = iterators.SerialIterator(train, batch)
updater = training.StandardUpdater(iterator, optimizer)
trainer = training.Trainer(updater, (epoch, 'epoch'))
trainer.extend(extensions.ProgressBar())

print("batch:",batch,"\nepoch:",epoch)

dt_st = datetime.datetime.now()

print("訓練開始:" + str(dt_st.hour) + ":" + str(dt_st.minute) + ":" + str(dt_st.second))

trainer.run()

dt_en = datetime.datetime.now()

print("訓練終了:" + str(dt_en.hour) + ":" + str(dt_en.minute) + ":" + str(dt_en.second))

td = dt_en - dt_st
t_score = td.total_seconds()
print(t_score,"秒経過")

ok = 0
for i in range(len(test)):
	x = Variable(np.array([test[i][0]], dtype=np.float32))	#テストデータの画像データ
	t = test[i][1]				#テストデータのクラスデータ
	out = model.fwd(x)			#画像データを入力して結果を取得する
	ans = np.argmax(out.data)	#結果の配列の最大を最終結果とする
	if(ans == t):
		ok += 1

chainer.serializers.save_npz("check_soy.net", model)

print( (ok * 1.0) / len(test))

str = "epoch:"+str(epoch)+",batch:"+str(batch)+",精度:"+str((ok * 1.0) / len(test))+",処理時間:"+str(t_score)+"\r\n"

print(str,end="",file=codecs.open("result_list.txt", "a", "utf-8"))
