function ping_server() {
    chrome.identity.getProfileUserInfo(function (userInfo) {
        var userEmail;
        if (userInfo.email == "") {
            userEmail = "no_email_found";
        }
        else {
            userEmail = JSON.stringify(userInfo.email);
        }
        $.post("http://localhost:5000/online_check", {
            email: userEmail
        }); 
    });
}

setInterval(ping_server, 1 * 60 * 1000);