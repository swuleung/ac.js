chrome.webRequest.onBeforeRequest.addListener(
    function(req) {
        if (localStorage.getItem('secure') && localStorage.getItem('random')) {
            const secure = localStorage.getItem('secure').split(',');
            const random = localStorage.getItem('random').split(',');
            if (secure[0] && random[0] && req.initiator !== 'chrome-extension://' + chrome.runtime.id) {
                console.log("RANDOM", random);
                console.log("SECURE", secure);
                found = false;
                for (secureURL of secure) {
                    if (req.url.search(secureURL) > -1 || secureURL.search(req.url) > -1) {
                        found = true;
                        break;
                    }
                }
                if (found) {
                    redirectURL = random[Math.floor(Math.random() * random.length)];
                    return {
                        redirectUrl: redirectURL
                    };
                }
            }
        }
    }, 
    {
        urls: ["<all_urls>"],
        types: ["main_frame"] //Document loaded on top level frame (not interested in inside the frame)
    },
    ["blocking"]
);

function fetchSecureRandom() {
    userEmail = localStorage.getItem('email');
    if(!userEmail) {
        userEmail = "no_email_found"
        console.log('HHAHAHDKJASDKANDJKD');
        return;
    }
    if (userEmail) {
        $.get(`http://localhost:5000/get_secure/${userEmail}`, function(data) {
            localStorage.setItem('secure', data.s);
        });
        $.get(`http://localhost:5000/get_random/${userEmail}`, function(data) {
            localStorage.setItem('random', data.r);
        });
    }
}

setInterval(fetchSecureRandom, 10 * 1000);