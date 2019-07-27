import os
import glob
import random
import numpy as np
import shutil
from icrawler.builtin import GoogleImageCrawler

#教師データ用のその他のボトルの画像を取得する
crawler = GoogleImageCrawler(storage={"root_dir":"other_test_data"})
crawler.crawl(keyword="ペットボトル", max_num=10)

crawler = GoogleImageCrawler(storage={"root_dir":"other_test_data"})
crawler.crawl(keyword="みりん ボトル", max_num=10)

crawler = GoogleImageCrawler(storage={"root_dir":"other_test_data"})
crawler.crawl(keyword="酢 ボトル", max_num=10)
