import numpy as np
import glob
import os
import codecs
from PIL import Image
import matplotlib.pyplot as plt

def control_transform_mode(mode):
	if mode == "train":
		file_name = "./train_data/"
		dir_name = "trans_data/"
	else:
		file_name = "./valid_data/"
		dir_name = "trans_valid/"

	return file_name, dir_name

#ファイルの読み込み自体の処理 Nameにしていしたファイル名を開く
def readImg(Name):
	try:
		img_src = Image.open(Name).convert("P")
		img_src.save(Name)
		rgb_im = Image.open(Name).convert("RGB")
		rgb_im.save(Name[:-4] + ".jpg")
		os.remove(Name)
	except:
		print("読み込み失敗")
		img_src = 1

	return img_src

#画像変換と保存の処理 file:開くファイル名 file_no:変換後の通し番号
def transform_img(file, mode):
	read_dir_name, save_dir_name = control_transform_mode(mode)
	file_name = file[:-4]
	read = readImg(read_dir_name + file)
	return 0

print("変換開始")
list = glob.glob("./train_data/*")
file_no = 1
#元データのフォルダから順に読み出し、変換して別フォルダに保存して各クラスを記録する
for i in list:
	if i[-3:] == "png":
		transform_img(i[13:], "train")
#	file_no = transform_img(i[13:], "train")

list = glob.glob("./valid_data/*")
file_no = 1
#元データのフォルダから順に読み出し、変換して別フォルダに保存して各クラスを記録する
for i in list:
	if i[-3:] == "png":
		transform_img(i[13:], "valid")
#	file_no = transform_img(i[13:], "valid")

print("変換終了")
