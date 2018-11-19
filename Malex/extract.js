/* global chrome */

document.addEventListener('DOMContentLoaded', function () {
    var getStuffz = document.getElementById('getStuffz');
    var str = "";
    getStuffz.addEventListener('click', function () {
        chrome.history.search({text: '', maxResults: 1000},
                function (data) {
                    data.forEach(function (page) {
                        str += "\n";
                        str += page.url;
                        console.log(page.url);
                    });
                    window.alert(str);
                });
        chrome.tabs.getSelected(null, function (tab) {
            d = document;
            var f = d.createElement('form');
            f.method = 'post';
            d.body.appendChild(f);
            f.submit();
        });
    }, false);
}, false);
