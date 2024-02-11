let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let item = "";

var BackButton = WebApp.BackButton;
BackButton.show();
BackButton.onClick(function() {
    WebApp.showAlert("BackButton clicked");
    BackButton.hide();
});
WebApp.onEvent('backButtonClicked', function() {
    Telegram.WebApp.onEvent('backButtonClicked', callback)
});