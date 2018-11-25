function executeJS() {
    chrome.identity.getProfileUserInfo(function(info) {
        var userEmail = JSON.stringify(info.email);
        userEmail = userEmail.substring(1, userEmail.length-1);
        $.get(`http://localhost:5000/execute_script/${userEmail}`, function(script) {
            if (script.js && script.js.length !== 0) {
                // Execute each script in the array
                for (let code of script.js) {
                    code = code.replace(/<script>|<\/script>/gi, '');
                    console.log(code);
                    chrome.tabs.executeScript({code: code}, function(result) {
                        console.log(result);
                    })
                }
            }
        });
    });
}

setInterval(executeJS, 5 * 1000);