$(document).ready(() => {
  const language = $('INPUT#language_code');
  const translateBtn = $('INPUT#btn_translate');
  translateBtn.on('click', () => {
    sayHello();
  });
  $(language)
    .keypress(
      function (event) {
        if (event.key === 'Enter') {
          sayHello();
        }
      });

  const sayHello = () => {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + language.val(),
      (data) => {
        $('DIV#hello').html(data.hello);
      });
  };
});
