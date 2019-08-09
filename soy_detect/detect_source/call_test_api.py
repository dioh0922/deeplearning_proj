"""
分類器を起動する処理
外部の分類器を呼び出す
"""
import model_test

result = model_test.start_test_model()

if result == 0:
	print("密閉です")
elif result == 1:
	print("昔の醤油です")
elif result == 2:
	print("めんつゆです")
else:
	print("他のボトルかも")
