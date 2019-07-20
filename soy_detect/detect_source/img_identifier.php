<?php

	//アップロードされたものなら「test.拡張子」の名前で保存して識別器から見るようにする
	if(is_uploaded_file($_FILES["test_img"]["tmp_name"])){
		$file_extension = pathinfo($_FILES["test_img"]["name"], PATHINFO_EXTENSION);
		if($file_extension != "jpg"){
			print("JPGを選択してください");
			exit();
		}

		$tmp_img_name = "test.".$file_extension;
		move_uploaded_file($_FILES["test_img"]["tmp_name"], $tmp_img_name);

		//ファイル名は引数で入力するように変更
		$full = "python model_test.cgi";	//環境により実行コマンドは異なる
		exec($full, $out);

		if($out[0] == "0"){
			print("醤油に見える");
		}else{
			print("めんつゆに見える");
		}

		//識別後にファイルを削除する
		unlink($tmp_img_name);
	}

?>
