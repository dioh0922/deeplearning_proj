import numpy as np
import glob
import codecs
from PIL import Image
import matplotlib.pyplot as plt

#ファイルの読み込み自体の処理 Nameにしていしたファイル名を開く
def readImg(Name):
	try:
		img_src = Image.open(Name)
		print("読み込み")
	except:
		print("読み込み失敗")
		img_src = 1

	return img_src

#画像変換と保存の処理 file:開くファイル名 file_no:変換後の通し番号
def transform_img(file, file_no):
	file_name = "./valid_data/"
	read = readImg(file_name + file)

	if read == 1:
		print("変換に失敗しました")
		return file_no
	else:
		trans_no = file_no		#変換後の通し番号
		identifier = file[-3:]	#拡張子を振りなおすために切り出す

		resizedImg = read.resize((50,50))
		dir_name = "trans_valid/" + format(trans_no, "06")
		resizedImg.save(dir_name + "." + identifier)
		save_detail_list(format(trans_no, "06") + "." + identifier, trans_no)
		print("変換終了=>",file)
		trans_no += 1

		tmp = resizedImg.transpose(Image.FLIP_TOP_BOTTOM)	#上下反転させる
		dir_name = "trans_valid/" + format(trans_no, "06")
		tmp.save(dir_name + "." + identifier)
		save_detail_list(format(trans_no, "06") + "." + identifier, trans_no)
		trans_no += 1

		tmp = resizedImg.transpose(Image.ROTATE_90)			#左に傾ける
		dir_name = "trans_valid/" + format(trans_no, "06")
		tmp.save(dir_name + "." + identifier)
		save_detail_list(format(trans_no, "06") + "." + identifier, trans_no)
		trans_no += 1

		tmp = resizedImg.transpose(Image.ROTATE_270)		#右に傾ける
		dir_name = "trans_valid/" + format(trans_no, "06")
		tmp.save(dir_name + "." + identifier)
		save_detail_list(format(trans_no, "06") + "." + identifier, trans_no)
		trans_no += 1

		tmp = resizedImg.transpose(Image.FLIP_LEFT_RIGHT)	#左右反転させる
		dir_name = "trans_valid/" + format(trans_no, "06")
		tmp.save(dir_name + "." + identifier)
		save_detail_list(format(trans_no, "06") + "." + identifier, trans_no)
		trans_no += 1

		return trans_no

#教師データの名前とクラスを記録する
def save_detail_list(data_name, data_no):
	class_id = 0

	if data_no <= 1500:
		class_id = 1
	else:
		class_id = 2

	class_str = str(class_id) + "\r\n"
	print(data_name,class_str,end="",file=codecs.open("valid_transform_list.txt", "a", "utf-8"))


list = glob.glob("./valid_data/*")
file_no = 1
#元データのフォルダから順に読み出し、変換して別フォルダに保存して各クラスを記録する
for i in list:

	file_no = transform_img(i[13:], file_no)