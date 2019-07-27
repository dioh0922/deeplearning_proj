import os
import glob
import random
import numpy as np
import shutil
import codecs
from icrawler.builtin import GoogleImageCrawler

#指定した分類の画像群を訓練データとテストデータに分割する関数
def split_data(target_name):
	dir_name = "./" + target_name + "/*"
	image_list = glob.glob(dir_name)
	random.shuffle(image_list)
	t_list, v_list = np.split(np.array(image_list), [int(len(image_list)*0.9)])
	t_list = list(t_list)
	v_list = list(v_list)

	for i in t_list:
		shutil.move(i, "./"+ target_name + "_train/")
	for i in v_list:
		shutil.move(i, "./"+target_name + "_valid/")

#指定したディレクトリの画像の個数を取得する関数
def max_file_idx(train_dir):
	max_idx = 0
	image_files = os.listdir(train_dir)	#ディレクトリの中身を取得

	for f_name in image_files:
		try:
			#拡張子より前を取得する(連番で振ってるはず)
			idx = int(os.path.splitext(f_name)[0])
		except ValueError:
			continue
		if idx > max_idx:
			max_idx = idx
	return max_idx

#醤油の画像を収集する
crawler = GoogleImageCrawler(storage={"root_dir":"soy"})
crawler.crawl(keyword="醤油", max_num=100)

idx = max_file_idx("soy")

crawler = GoogleImageCrawler(storage={"root_dir":"soy"})
crawler.crawl(keyword="醤油 ボトル", max_num=100, file_idx_offset=idx)

idx = max_file_idx("soy")

crawler = GoogleImageCrawler(storage={"root_dir":"soy"})
crawler.crawl(keyword="醤油 キッコーマン", max_num=100, file_idx_offset=idx)

idx = max_file_idx("soy")

crawler = GoogleImageCrawler(storage={"root_dir":"soy"})
crawler.crawl(keyword="醤油 ヤマサ", max_num=100, file_idx_offset=idx)

idx = max_file_idx("soy")
soy_idx = idx

#split_data("soy")	#訓練データとテスト用に分割 (醤油)

#めんつゆの画像を収集する
crawler = GoogleImageCrawler(storage={"root_dir":"noodle"})
crawler.crawl(keyword="めんつゆ", max_num=100, file_idx_offset=idx)

idx = max_file_idx("noodle")

crawler = GoogleImageCrawler(storage={"root_dir":"noodle"})
crawler.crawl(keyword="めんつゆ ボトル", max_num=100, file_idx_offset=idx)

idx = max_file_idx("noodle")

crawler = GoogleImageCrawler(storage={"root_dir":"noodle"})
crawler.crawl(keyword="めんつゆ キッコーマン", max_num=100, file_idx_offset=idx)

idx = max_file_idx("noodle")

crawler = GoogleImageCrawler(storage={"root_dir":"noodle"})
crawler.crawl(keyword="めんつゆ ヤマサ", max_num=100, file_idx_offset=idx)

idx = max_file_idx("noodle")
noodle_idx = idx

#split_data("noodle")	#訓練データとテスト用に分割 (醤油)

#テスト用の「なんちゃってオレンジ」の画像を取得する
crawler = GoogleImageCrawler(storage={"root_dir":"test_data"})
crawler.crawl(keyword="なんちゃってオレンジ", max_num=10)

#print("醤油の画像No:",soy_idx,"\r\n","めんつゆの画像No:",noodle_idx,"\r\n", file=codecs.open("data_memo.txt", "w", "utf-8"))
