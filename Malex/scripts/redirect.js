chrome.webRequest.onBeforeRequest.addListener(
    function(req) {
        chrome.identity.getProfileUserInfo(function(info) {
            if (req.initiator !== 'chrome-extension://' + chrome.runtime.id) {
                // Fetch the secure and redirect urls
                userEmail = JSON.stringify(info.email);
                userEmail = userEmail.substring(1, userEmail.length-1);
                $.get(`http://localhost:5000/get_secure/${userEmail}`, function(data1) {
                    if (info.url in data1.s) {
                        $.get(`http://localhost:5000/get_random/${userEmail}`, function(data2) {
                            redirectURL = data2.r[Math.floor(Math.random() * data2.r.length)];
                            console.log("Redirect to: " + redirectURL);
                            return { redirectUrl: redirectURL }; // Fix
                        });
                    }
                });
            }
        });
    }, 
    {
        urls: ["<all_urls>"],
        types: ["main_frame"] //Document loaded on top level frame (not interested in inside the frame)
    },
    ["blocking"]
);