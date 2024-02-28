document.addEventListener('DOMContentLoaded', () => {
  const language = $('INPUT#language_code');
  const translateBtn = $('INPUT#btn_translate');
  translateBtn.on('click', () => {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + language.val(),
      (data) => {
        $('DIV#hello').html(data.hello);
      });
  });
});
