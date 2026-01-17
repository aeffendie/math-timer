

boolean compare_eval(String: server_verified) {
    String user_result = document.getElementById("user_input").value;
    if (user_result == server_verified) {
        return true;
    }
    return false;
}


