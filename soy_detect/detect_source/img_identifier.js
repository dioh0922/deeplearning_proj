
var control_result = new Vue({
	el: "#result_area",
	data:{
		text: "ファイルを選んでください"
	}
});

var control_file_select = new Vue({
	el: "#load_img",
	methods:{
		selected: load_local_Image
	}
});

function load_local_Image(e){
	var file = e.target.files[0];
	if(!file.type.match("image.*")){
		alert("画像でない");
		return;
	}

	var blob = window.URL.createObjectURL(file);

	$("#img_preview").attr("src", blob);
	control_result.text = "識別しています";
	get_img_class()
}

function get_img_class(){

	var formdata = new FormData($("#img_form").get(0));

	$.ajax({
		type: "POST",
		url: "http://localhost/python_test/img_identifier.php",
		cacha:false,
		contentType: false,
		processData: false,
		data: formdata,
		dataType: "html"
	})
	.done(function(ajax_data){
		control_result.text = ajax_data;
	})
	.fail(function(){
		control_result.text = "PHPへの通信が失敗しました。";
	});
}


//起動時の処理
(window.onload = function(){
	//get_img_class();
});
