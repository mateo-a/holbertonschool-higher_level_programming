document.addEventListener('DOMContentLoaded', function () {
  $('input#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      $('input#btn_translate').click();
    }
  });
  $('input#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=' + $('input#language_code').val(), function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
