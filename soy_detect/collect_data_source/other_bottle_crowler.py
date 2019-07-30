"""
醤油とめんつゆ以外のボトル画像を集めるプログラム
訓練用にサイズ変更は訓練データ作成時にする
"""

from icrawler.builtin import GoogleImageCrawler
import sys
import crowler_util as cu

args = sys.argv

#コマンドライン引数で画像に振る番号を指定する
offset = 0
if len(args) >= 2:
	offset = int(args[1])

save_dir = "./other_test_data/"

#教師データ用のその他のボトルの画像を取得する
idx = offset
crawler = GoogleImageCrawler(storage={"root_dir":"other_test_data"})
crawler.crawl(keyword="ペットボトル", max_num=40, file_idx_offset=idx)

idx += cu.get_img_len(save_dir)
crawler = GoogleImageCrawler(storage={"root_dir":"other_test_data"})
crawler.crawl(keyword="みりん ボトル", max_num=40, file_idx_offset=idx)

idx += cu.get_img_len(save_dir)
crawler = GoogleImageCrawler(storage={"root_dir":"other_test_data"})
crawler.crawl(keyword="酢 ボトル", max_num=40, file_idx_offset=idx)

cu.save_to_jpg(save_dir, offset)
