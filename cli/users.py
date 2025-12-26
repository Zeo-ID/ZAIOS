from audit import log

def add_user(username, email, role):
    # Mock / später DB
    print(f"[ZAIOS] User added: {username}")
    log("USER_ADD", username, f"email={email}, role={role}")

def disable_user(username):
    print(f"[ZAIOS] User disabled: {username}")
    log("USER_DISABLE", username)
