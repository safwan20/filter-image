
$('form').on('submit', function(event) {
		console.log("sahi hai")
		console.log($("#hok"));
		var form_data = new FormData(document.getElementById("hok"));		
		console.log("hello")
		console.log(form_data)
		$.ajax({
				data  : form_data,
				type : 'POST',
				url : '/process',
				processData: false,
				contentType: false,
				beforeSend : function () {
						$("#ol")
							.css('visibility',"visible")
				},
				complete : function () {
						$("#ol")
							.css('visibility',"hidden")
				},
		})
		.done(function(data) {
			if(data.error) {
				console.log("error");
			}
			else {
				console.log("send",data.filename);
				$("#filter")
					.attr('src','../static/Filters_images/' + data.filename)
					.width(500)
					.height(400)
				$("a")
					.attr('href','../static/Filters_images/' + data.filename)
			}
		});
	event.preventDefault();
});



function readURL(input) {
console.log(input)
	$("#filter")
					.attr('src','../static/noimage.png')
					.width(500)
					.height(400)
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
             $('#blah')
                .attr('src', e.target.result)
                .width(500)
                .height(400);
        };
        reader.readAsDataURL(input.files[0]);
     }
}