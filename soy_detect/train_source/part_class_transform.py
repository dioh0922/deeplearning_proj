"""
教師用画像の前処理するプログラム
元データにクラスを付与(密閉ボトル/旧ボトル/めんつゆ)
リサイズした後に教師データ水増しに反転させて別ディレクトリに保存
"""

import glob
import codecs
from PIL import Image

#ファイルの読み込み自体の処理 Nameにしていしたファイル名を開く
def readImg(Name):
	try:
		img_src = Image.open(Name)
		#print(Name)
	except:
		print("読み込み失敗")
		img_src = 1

	return img_src

#画像変換と保存の処理 file:開くファイル名 file_no:変換後の通し番号
def transform_img(file, file_no, mode):
	#file_name = "./valid_data/"
	file_name = "./train_data/"
	save_dir_name = "trans_data/"
	read = readImg(file_name + file)
	identifier = file[-3:]	#拡張子を振りなおすために切り出す

	if read == 1:
		print("変換に失敗しました")
		return file_no
	else:
		trans_no = file_no		#変換後の通し番号

		class_id = file[-5]		#ファイル名にクラス識別子を埋め込んでおく

		resizedImg = read.resize((50, 50))
		dir_name = save_dir_name + format(trans_no, "06")
		resizedImg.save(dir_name + "_" + str(class_id) + "." + identifier)
		trans_no += 1

		tmp = resizedImg.transpose(Image.FLIP_TOP_BOTTOM)	#上下反転させる
		dir_name = save_dir_name + format(trans_no, "06")
		tmp.save(dir_name + "_" + str(class_id) + "." + identifier)
		trans_no += 1

		tmp = resizedImg.transpose(Image.ROTATE_90)			#左に傾ける
		dir_name = save_dir_name + format(trans_no, "06")
		tmp.save(dir_name + "_" + str(class_id) + "." + identifier)
		trans_no += 1

		tmp = resizedImg.transpose(Image.ROTATE_270)		#右に傾ける
		dir_name = save_dir_name + format(trans_no, "06")
		tmp.save(dir_name + "_" + str(class_id) + "." + identifier)
		trans_no += 1

		tmp = resizedImg.transpose(Image.FLIP_LEFT_RIGHT)	#左右反転させる
		dir_name = save_dir_name + format(trans_no, "06")
		tmp.save(dir_name + "_" + str(class_id) + "." + identifier)
		trans_no += 1

		return trans_no

#読み込んだファイルをクラス番号を付けて保存し直す
def set_classifier_img(file, class_id):

	read = readImg(file)
	identifier = file[-3:]	#拡張子を振りなおすために切り出す
	file_str = "./train_data/" + file[-10:-4] + "_" + str(class_id) + "." + identifier

	if read == 1:
		print("変換に失敗しました")
	else:
		read.save(file_str)

#元データは各ディレクトリに入れておき、統一でぅれくとりにコピーする
print("教師データ前処理開始")
list = glob.glob("./new_soy/*")
for i in list:
	set_classifier_img(i, 0)

list = glob.glob("./noodle/*")
for i in list:
	set_classifier_img(i, 2)

list = glob.glob("./old_soy/*")
for i in list:
	set_classifier_img(i, 1)

list = glob.glob("./other/*")
for i in list:
	set_classifier_img(i, 3)

print("リネーム終了")

#統一ディレクトリに対して前ファイルに水増し
list = glob.glob("./train_data/*")
file_no = 1
#元データのフォルダから順に読み出し、変換して別フォルダに保存して各クラスを記録する
for i in list:

	file_no = transform_img(i[13:], file_no, "train")

print("変換終了")
