var $DOM = $(document);
$DOM.on('click', '#wiki_info_submit', function() {

	console.log("login clicked");
    data = {}
    data["topic"] = $(".topic").val();
    data["article"] = $(".article").val()
	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/wikiinfo',
		success: function(result) {
            if (result.success) {
                window.location.href = "/";
            }
            else {
                alertify.set('notifier', 'position', 'top-right');
                alertify.error(result.message);
            }
		}
	});
});

