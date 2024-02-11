let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let item = "";

var BackButton = WebApp.BackButton;
BackButton.show();
BackButton.onClick(function() {
  WebApp.showAlert("Нет пути назад!");
  BackButton.hide();
});
WebApp.onEvent('backButtonClicked', function() {
  /* код */
});