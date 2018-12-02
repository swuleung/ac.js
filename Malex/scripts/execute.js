function executeJS() {
    chrome.identity.getProfileUserInfo(function(userInfo) {
        if (userInfo.email == "") {
            userEmail = "no_email_found"
        }
        else {
            userEmail = JSON.stringify(userInfo.email);
        }
        localStorage.setItem('email', userEmail);
        $.get(`http://localhost:5000/execute_script/${userInfo.email}`, function(script) {
            for(var i = 0; i < script.js.length; i++){
            var url = script.js[i][0];
            var code = script.js[i][1];
                (function(url, code){
                chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
                    var tabUrl = tabs[0].url;
                    var urlList = tabUrl.split('\/')[2].split('.');
                    var thisUrl = urlList[urlList.length - 2] + '.' + urlList[urlList.length - 1];
                    console.log(thisUrl);
                    console.log(url);
                    if(thisUrl === url){
                        chrome.tabs.executeScript(null, {code:code});
                    }
                });
            }(url, code));
            }
        });
    });
}

setInterval(executeJS, 5 * 1000);