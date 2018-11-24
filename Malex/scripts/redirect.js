chrome.webRequest.onBeforeRequest.addListener(
    function(req) {
        redirectURL = '';
        chrome.identity.getProfileUserInfo(function(info) {
            if (req.initiator !== 'chrome-extension://' + chrome.runtime.id) {
                // Fetch the secure and redirect urls
                userEmail = JSON.stringify(info.email);
                userEmail = userEmail.substring(1, userEmail.length-1);
                $.get(`http://localhost:5000/get_secure/${userEmail}`, function(data1) {
                    found = false;
                    for (sUrl of data1.s) {
                        if (req.url.search(sUrl) > -1 || sUrl.search(req.url) > -1) {
                            found = true;
                        }
                    }
                    if (found) {
                        $.get(`http://localhost:5000/get_random/${userEmail}`, function(data2) {
                            redirectURL = data2.r[Math.floor(Math.random() * data2.r.length)];
                        });
                    }
                });
            }
        });
        return {
            redirectUrl: redirectURL
        }
    }, 
    {
        urls: ["<all_urls>"],
        types: ["main_frame"] //Document loaded on top level frame (not interested in inside the frame)
    },
    ["blocking"]
);

/*
function temp(req) {
    redirectURL = '';
    return new Promise(resolve => {
        chrome.identity.getProfileUserInfo(function(info) {
            if (req.initiator !== 'chrome-extension://' + chrome.runtime.id) {
                // Fetch the secure and redirect urls
                userEmail = JSON.stringify(info.email);
                userEmail = userEmail.substring(1, userEmail.length-1);
                $.get(`http://localhost:5000/get_secure/${userEmail}`, function(data1) {
                    found = false;
                    for (sUrl of data1.s) {
                        if (req.url.search(sUrl) > -1 || sUrl.search(req.url) > -1) {
                            found = true;
                        }
                    }
                    if (found) {
                        $.get(`http://localhost:5000/get_random/${userEmail}`, function(data2) {
                            console.log("SECOND GET");
                            console.log("hello");
                            redirectURL = data2.r[Math.floor(Math.random() * data2.r.length)];
                            console.log(redirectURL);
                        });
                    }
                });
            }
        });
    }).then(() => {
        console.log(redirectURL);
        console.log("IN THE THEN");
        return redirectURL;
    });
}*/

/*
async function getRedirectURL(req) {
    if (req.initiator === 'chrome-extension://' + chrome.runtime.id)
        return '';
    return await chrome.identity.getProfileUserInfo(function(info) {
        // Fetch the secure and redirect urls
        userEmail = JSON.stringify(info.email);
        userEmail = userEmail.substring(1, userEmail.length-1);
        $.get(`http://localhost:5000/get_secure/${userEmail}`, function(data1) {
            console.log("FIRST GET");
            found = false;
            for (sUrl of data1.s) {
                if (req.url.search(sUrl) > -1 || sUrl.search(req.url) > -1) {
                    found = true;
                }
            }
            if (found) {
                console.log("INSIDE IF");
                $.get(`http://localhost:5000/get_random/${userEmail}`, function(data2) {
                    console.log("SECOND GET");
                    redirectURL = data2.r[Math.floor(Math.random() * data2.r.length)];
                    console.log("Redirect to: " + redirectURL);
                });
            }
        });
    });
}*/