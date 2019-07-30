"""
醤油・めんつゆ・オレンジジュースの画像を収集するプログラム
"""

from icrawler.builtin import GoogleImageCrawler
import crowler_util as cu

save_dir = "./soy_noodle_test_data/"
idx = 0

#醤油の画像を収集する
crawler = GoogleImageCrawler(storage={"root_dir":save_dir})
crawler.crawl(keyword="醤油", max_num=100)

idx = cu.get_img_len(save_dir)
crawler = GoogleImageCrawler(storage={"root_dir":save_dir})
crawler.crawl(keyword="醤油 ボトル", max_num=100, file_idx_offset=idx)

idx = cu.get_img_len(save_dir)
crawler = GoogleImageCrawler(storage={"root_dir":save_dir})
crawler.crawl(keyword="醤油 キッコーマン", max_num=100, file_idx_offset=idx)

idx = cu.get_img_len(save_dir)
crawler = GoogleImageCrawler(storage={"root_dir":save_dir})
crawler.crawl(keyword="醤油 ヤマサ", max_num=100, file_idx_offset=idx)

idx = cu.get_img_len(save_dir)

#めんつゆの画像を収集する
crawler = GoogleImageCrawler(storage={"root_dir":save_dir})
crawler.crawl(keyword="めんつゆ", max_num=100, file_idx_offset=idx)

idx = cu.get_img_len(save_dir)
crawler = GoogleImageCrawler(storage={"root_dir":save_dir})
crawler.crawl(keyword="めんつゆ ボトル", max_num=100, file_idx_offset=idx)

idx = cu.get_img_len(save_dir)
crawler = GoogleImageCrawler(storage={"root_dir":save_dir})
crawler.crawl(keyword="めんつゆ キッコーマン", max_num=100, file_idx_offset=idx)

idx = cu.get_img_len(save_dir)
crawler = GoogleImageCrawler(storage={"root_dir":save_dir})
crawler.crawl(keyword="めんつゆ ヤマサ", max_num=100, file_idx_offset=idx)


#テスト用の「なんちゃってオレンジ」の画像を取得する
crawler = GoogleImageCrawler(storage={"root_dir":"orange_test_data"})
crawler.crawl(keyword="なんちゃってオレンジ", max_num=10)
