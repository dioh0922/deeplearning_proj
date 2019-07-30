"""
クロウラー関係の共通処理
"""
from PIL import Image
import imghdr
import glob
import os
import imghdr

#jpgのみにする処理
def save_to_jpg(save_dir, offset):
	#保存先のディレクトリ内にすべて変換を適用する
	list = glob.glob(save_dir + "*")
	cnt = offset
	for i in list:
		cnt += 1
		rename_str = save_dir + format(cnt, "06") + ".jpg"

		#拡張子によって保存方法を変える
		identifier = imghdr.what(i)
		if identifier == "bmp":
			transform_image(i, rename_str)
		elif identifier == "gif":
			transform_image(i, rename_str)
		elif identifier == "png":
			transform_image(i, rename_str)
		elif identifier == "jpeg":
			try:
				img = Image.open(i)
				img.save(rename_str)
				if i[-4:] == "jpeg":
					os.remove(i)
			except:
				print("読み込み失敗")

#画像取得後の番号を取得する処理
def get_img_len(save_dir):
	list = glob.glob(save_dir + "*")
	return len(list)

#保存したディレクトリでjpgのみにする処理
def transform_image(src_path, target):
	try:
		img_src = Image.open(src_path).convert("P")
		img_src.save(src_path)
		rgb_im = Image.open(src_path).convert("RGB")
		rgb_im.save(target)
		os.remove(src_path)
	except:
		print("読み込み失敗")

#画像取得後の番号を取得する処理
def get_img_len(save_dir):
	list = glob.glob(save_dir + "*")
	return len(list)
