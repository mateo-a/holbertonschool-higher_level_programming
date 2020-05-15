$(document).ready(function () {
  $('div#add_item').click(function () {
    $('<LI>Item</LI>').appendTo('UL.my_list');
  });
  $('div#remove_item').click(function () {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list li').remove();
  });
});
