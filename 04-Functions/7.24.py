def check_password(password):
    password = password.replace(" ", "")
    pass_set = set(password)
    
    return len(pass_set) >= 6
