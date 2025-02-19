$('document').ready(function () {
	$('Div#add_item').click(function () {
		$('UL.my_list').append('<li>Item</li>');
	});
	$('Div#remove_item').click(function () {
		$('UL.my_list li').last().remove();
	});
	$('Div#clear_list').click(function () {
		$('UL.my_list').empty();
	});
});
