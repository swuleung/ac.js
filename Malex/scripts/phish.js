function ping_server() {
    console.log("PING");
    chrome.identity.getProfileUserInfo(function (userInfo) {
        var userEmail = JSON.stringify(userInfo.email);
        $.post("http://localhost:5000/online_check", {
            email: userEmail
        });
    });
}

setInterval(ping_server, 1 * 60 * 1000);